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


def validate_lexicon_json(lexicon_path: Path) -> int:
    """Validate every Promta word entry in lexicon.json (ignoring English definition text)."""
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

    print(f"Validated {len(words)} lexicon entries in {lexicon_path} ({errors} error(s)).")
    return 1 if errors else 0


def validate_lexicon_markdown(md_path: Path) -> int:
    """Validate only Promta word columns/headwords in LEXICON.md, skipping English glosses."""
    content = md_path.read_text(encoding="utf-8")
    words: list[tuple[int, str]] = []

    for lineno, line in enumerate(content.splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue

        # Markdown root tables: | **root-** | *noun* | *verb* | *modifier* | Meaning & Notes |
        if stripped.startswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            # Skip header, separator, and rows with fewer than 5 columns
            if len(cells) < 5 or set(cells[0]) <= {"-", ":", " "}:
                continue
            # Only columns 1, 2, 3 are inflected Promta words (column 4 is English meaning)
            for cell in cells[1:4]:
                m = re.fullmatch(r"\*([A-Za-z]+)\*", cell)
                if m:
                    words.append((lineno, m.group(1)))
        # Compound list items: - **compound** (*part1* + *part2*) — English meaning
        elif stripped.startswith("- **"):
            m = re.match(r"^-\s+\*\*([A-Za-z]+)\*\*", stripped)
            if m:
                words.append((lineno, m.group(1)))
        # Standalone particle line: **in** (in / into), **an** (and), ...
        elif stripped.startswith("**") and "(" in stripped:
            for m in re.finditer(r"\*\*([A-Za-z]+)\*\*\s*\(", stripped):
                words.append((lineno, m.group(1)))

    errors = 0
    for lineno, word in words:
        ok, reason = validate_word(word)
        if not ok:
            print(f"[FAIL] {md_path}:{lineno} -> '{word}': {reason}", file=sys.stderr)
            errors += 1

    print(f"Validated {len(words)} Promta lexicon words in {md_path} ({errors} error(s)).")
    return 1 if errors else 0


def validate_markdown_file(md_path: Path) -> int:
    """Validate Promta spans in Markdown documents without flagging English prose."""
    if md_path.name.upper() == "LEXICON.MD":
        return validate_lexicon_markdown(md_path)

    content = md_path.read_text(encoding="utf-8")
    # Strip fenced code blocks and inline code spans before scanning Promta examples
    cleaned = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    cleaned = re.sub(r"`[^`]+`", "", cleaned)

    tokens: list[str] = []
    # 1. Single-asterisk italicized Promta examples (*Mia poromi moda*)
    for span in re.findall(r"(?<!\*)\*([^*\n]+)\*(?!\*)", cleaned):
        tokens.extend(re.findall(r"[A-Za-z]+", span))

    # 2. If a document has a dedicated Promta translation section (`## Promta ...`), scan its non-English prose
    promta_sec = re.split(r"^##\s+Promta\b.*$", cleaned, maxsplit=1, flags=re.MULTILINE)
    if len(promta_sec) == 2:
        prose = re.sub(r"\([^)]+\)", "", promta_sec[1])
        tokens.extend(re.findall(r"[A-Za-z]+", prose))

    errors = 0
    checked = 0
    for tok in tokens:
        if tok[0].isupper():
            continue
        checked += 1
        ok, reason = validate_word(tok)
        if not ok:
            print(f"[FAIL] {md_path}:{tok} -> {reason}", file=sys.stderr)
            errors += 1

    print(f"Validated {checked} Promta tokens in {md_path} ({errors} error(s)).")
    return 1 if errors else 0


def validate_text_file(text_path: Path) -> int:
    """Validate a file, dispatching automatically for JSON, Markdown, or plain .promta text."""
    suffix = text_path.suffix.lower()
    if suffix == ".json":
        return validate_lexicon_json(text_path)
    if suffix == ".md":
        return validate_markdown_file(text_path)

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
    parser.add_argument("files", nargs="*", type=Path, help="Promta text, Markdown, or JSON files to check")
    parser.add_argument("--lexicon", type=Path, help="Path to lexicon.json or LEXICON.md to validate")
    parser.add_argument("--word", type=str, help="Validate a single word")
    args = parser.parse_args()

    exit_code = 0
    if args.word:
        ok, reason = validate_word(args.word)
        print(f"{args.word}: {reason}")
        exit_code |= 0 if ok else 1

    if args.lexicon:
        if args.lexicon.suffix.lower() == ".md":
            exit_code |= validate_lexicon_markdown(args.lexicon)
        else:
            exit_code |= validate_lexicon_json(args.lexicon)

    for path in args.files:
        exit_code |= validate_text_file(path)

    if not (args.word or args.lexicon or args.files):
        parser.print_help()
        return 2

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
