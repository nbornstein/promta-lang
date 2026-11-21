#!/usr/bin/env python3
"""Zero-dependency phonological & orthographic validator for Promta."""

import re
import sys
from pathlib import Path

VOWELS = set("aeiu")
CONSONANTS = set("ptksmnlr")
ALPHABET = VOWELS | CONSONANTS


def check_word(word: str) -> list[str]:
    """Return a list of phonological warnings for a lowercase Promta word."""
    issues = []
    bad_chars = sorted(set(word) - ALPHABET)
    if bad_chars:
        issues.append(f"non-12-letter chars {bad_chars}")

    # Check for consonant clusters of 3+ or disallowed codas
    for i in range(len(word) - 1):
        c1, c2 = word[i], word[i + 1]
        if c1 in CONSONANTS and c2 in CONSONANTS:
            if c1 not in {"m", "n"}:
                issues.append(f"non-nasal cluster '{c1}{c2}'")
    return issues


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 validate_promta.py <file.promta>")
        return 1

    path = Path(sys.argv[1])
    text = path.read_text(encoding="utf-8")
    total_words = 0
    flagged = 0

    for line_no, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.split("#", 1)[0].strip()
        if not line:
            continue
        words = re.findall(r"[A-Za-z]+", line)
        for w in words:
            total_words += 1
            # Skip capitalized proper nouns/acronyms in audit notes
            if w[0].isupper():
                continue
            issues = check_word(w.lower())
            if issues:
                flagged += 1
                print(f"Line {line_no}: '{w}' -> {', '.join(issues)}")

    print(f"Checked {total_words} tokens; {flagged} flagged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
