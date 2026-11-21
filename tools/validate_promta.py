#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Zero-dependency phonological and syllable validator for Promta (15-letter alphabet)."""

import argparse
import json
import re
import sys
from pathlib import Path

VOWELS = set("aeiou")
CONSONANTS = set("pdtgksmnlr")
NASALS = set("mn")
ALPHABET = VOWELS | CONSONANTS

# Strict (C)V(N) syllable matcher across an entire lowercase word.
SYLLABLE_PATTERN = re.compile(r"^([pdtgksmnlr]?[aeiou][mn]?)+$")


def validate_word(word: str) -> tuple[bool, str]:
    """Validate a single Promta word against the 15-letter alphabet and (C)V(N) rules."""
    w = word.strip().lower()
    if not w:
        return False, "empty token"

    bad_chars = sorted(set(w) - ALPHABET)
    if bad_chars:
        return False, f"forbidden character(s): {', '.join(bad_chars)}"

    if not SYLLABLE_PATTERN.match(w):
        return False, "violates (C)V(N) syllable structure (cluster or non-nasal coda)"

    return True, "ok"


def validate_lexicon(lexicon_path: Path) -> int:
    """Validate every word entry in lexicon.json."""
    data = json.loads(lexicon_path.read_text(encoding="utf-8"))
    words: list[tuple[str, str]] = []

    for category, entries in data.get("roots", {}).items():
        for entry in entries:
            root_id = entry.get("root", "?")
            for pos in ("noun", "verb", "modifier"):
                val = entry.get(pos)
                if val:
                    words.append((f"{category}:{root_id}:{pos}", val))

    for p in data.get("particles", []):
        words.append(("particle", p["word"]))

    for c in data.get("compounds", []):
        words.append(("compound", c["word"]))

    errors = 0
    for loc, word in words:
        ok, reason = validate_word(word)
        if not ok:
            print(f"[FAIL] {loc} -> '{word}': {reason}", file=sys.stderr)
            errors += 1

    print(f"Validated {len(words)} lexicon entries ({errors} error(s)).")
    return 1 if errors else 0


def validate_text_file(text_path: Path) -> int:
    """Validate lowercase Promta tokens in a text or .promta file."""
    content = text_path.read_text(encoding="utf-8")
    lines = [
        ln for ln in content.splitlines()
        if not ln.lstrip().startswith(("#", "//"))
    ]
    tokens = re.findall(r"[A-Za-z]+", "\n".join(lines))
    errors = 0
    checked = 0
    for tok in tokens:
        if tok[0].isupper():
            continue
        checked += 1
        ok, reason = validate_word(tok)
        if not ok:
            print(f"[FAIL] {text_path}:{tok} -> {reason}", file=sys.stderr)
            errors += 1

    print(f"Validated {checked} Promta tokens in {text_path} ({errors} error(s)).")
    return 1 if errors else 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate Promta words against the 15-letter (C)V(N) phonology."
    )
    parser.add_argument("files", nargs="*", type=Path, help="Promta text files to check")
    parser.add_argument("--lexicon", type=Path, help="Path to lexicon.json to validate")
    parser.add_argument("--word", type=str, help="Validate a single word")
    args = parser.parse_args()

    exit_code = 0
    if args.word:
        ok, reason = validate_word(args.word)
        print(f"{args.word}: {reason}")
        exit_code |= 0 if ok else 1

    if args.lexicon:
        exit_code |= validate_lexicon(args.lexicon)

    for path in args.files:
        exit_code |= validate_text_file(path)

    if not (args.word or args.lexicon or args.files):
        parser.print_help()
        return 2

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
