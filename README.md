# Promta (`promta`)

An engineered, minimalist, English-friendly constructed language designed for unambiguous communication about generative AI, neural architectures, and human-AI workflows.

## Key Features

- **15-Letter Phonemic Alphabet:** 5 vowels (`a, e, i, o, u`) and 10 consonants (`p, d, t, g, k, s, m, n, l, r`) with strict one-to-one letter-to-sound correspondence.
- **Cluster-Free `(C)V(N)` Syllables:** Every syllable consists of an optional single onset consonant, a mandatory vowel, and an optional nasal coda (`m` or `n`).
- **Deterministic Part-of-Speech Endings:** Content words end in `-a` (noun), `-i` (verb), or `-e` (adjective/adverb).
- **Strict SVO Syntax:** Head-final modifiers and head-final compounding (`konteka` + `lata` -> `konteklata`).

## Repository Structure

```text
promta-lang/
├── README.md
├── spec/
│   ├── 01-phonology.md    # 15-letter alphabet & (C)V(N) syllable rules
│   └── 02-grammar.md      # SVO syntax, POS vowel endings, particles, conditionals
├── lexicon/
│   ├── LEXICON.md         # Canonical Markdown lexicon tables
│   └── lexicon.json       # Machine-readable root & compound registry
├── examples/
│   ├── conversation-log.md
│   └── system-prompt.promta
└── tools/
    └── validate_promta.py # Zero-dependency phonological & syllable validator
```

## Validating Words & Texts

```bash
python3 tools/validate_promta.py --lexicon lexicon/lexicon.json
python3 tools/validate_promta.py examples/system-prompt.promta
```
