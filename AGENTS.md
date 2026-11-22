# AGENTS.md

Instructions for AI coding agents working on `promta-lang`.

## Project Overview

Promta is a minimalist constructed language designed for unambiguous communication about generative AI, neural architectures, and human-AI workflows.

- **Alphabet (15 letters):** Vowels `a, e, i, o, u` and consonants `p, d, t, g, k, s, m, n, l, r`.
- **Forbidden letters in native words:** `b, c, f, h, j, q, v, w, x, y, z`.
- **Syllable structure:** Strict `(C)V(N)`—an optional single onset consonant, a mandatory vowel nucleus, and an optional nasal coda (`m` or `n`). No consonant clusters or non-nasal codas.
- **Parts of speech (content words):** `-a` (noun), `-i` (verb), `-e` (adjective/adverb).
- **Syntax & compounding:** Strict SVO word order with head-final modifiers and head-final compounds.

## Repository Layout

- `README.md` — Project overview, validation commands, licensing, and Promta translation section.
- `AGENTS.md` — Guidance and project invariants for AI coding agents.
- `spec/01-phonology.md` — Alphabet, forbidden letters, and `(C)V(N)` syllable rules.
- `spec/02-grammar.md` — SVO word order, POS endings, prefixes/particles, compounding, questions, imperatives, and conditionals.
- `lexicon/lexicon.json` — Canonical machine-readable lexicon (`roots`, `particles`, `compounds`).
- `lexicon/LEXICON.md` — Canonical Markdown lexicon tables and lists kept in sync with `lexicon/lexicon.json`.
- `examples/conversation-log.md` — Annotated example exchanges.
- `tools/validate_promta.py` — Zero-dependency Python validator for phonology and `(C)V(N)` syllable structure.

## Lexicon & Editing Rules

1. **Validate every Promta form:** Every new or edited Promta root form, particle, compound, or example span must use only the 15-letter alphabet and satisfy `(C)V(N)`.
2. **Alphabetical ordering:** Keep entries sorted alphabetically (case-insensitive) within each section of `lexicon/lexicon.json` and `lexicon/LEXICON.md`:
   - Each category under `roots` (`core_logic`, `ai_architecture`, `human_ai_workflows`) sorted by `root`.
   - `particles` sorted by `word`.
   - `compounds` sorted by `word`.
3. **Keep JSON and Markdown in sync:** Whenever you update `lexicon/lexicon.json`, update `lexicon/LEXICON.md` (and any affected spec/example/README snippets) to match.
4. **Do not alter English glosses to fit Promta rules:** The validator (`tools/validate_promta.py`) separates Promta tokens from English definitions and prose—keep English definitions natural and accurate.

## Validation

Run the validator from the repository root after making changes:

```bash
python3 tools/validate_promta.py --lexicon lexicon/lexicon.json lexicon/LEXICON.md README.md spec/02-grammar.md examples/conversation-log.md
```

All checks must exit with `0` and report `0 error(s)`.

## Attribution & Licensing

- **Language & docs (`README.md`, `spec/`, `lexicon/`, `examples/`, `AGENTS.md`):** CC BY-SA 4.0.
- **Tools (`tools/`):** MIT License.
- **AI assistance:** Document Gemini assistance transparently in `README.md` or commit trailers (such as `Assisted-by:`) when applicable, while keeping human review and sign-off clear.