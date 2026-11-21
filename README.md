# Promta (`promta`)

An engineered, minimalist, English-friendly constructed language designed for unambiguous communication about generative AI, neural architectures, and human-AI workflows.

## Key Features

- **15-Letter Phonemic Alphabet:** 5 vowels (`a, e, i, o, u`) and 10 consonants (`p, d, t, g, k, s, m, n, l, r`) with strict one-to-one letter-to-sound correspondence.
- **Cluster-Free `(C)V(N)` Syllables:** Every syllable consists of an optional single onset consonant, a mandatory vowel, and an optional nasal coda (`m` au `n`).
- **Deterministic Part-of-Speech Endings:** Content words end in `-a` (noun), `-i` (verb), au `-e` (adjective/adverb).
- **Strict SVO Syntax:** Head-final modifiers and head-final compounding (`konteka` + `lata` -> `kontekalata`).

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

## License

- **Language Specification, Lexicon, Documentation & Examples** (`README.md`, `spec/`, `lexicon/`, `examples/`): Licensed under [CC BY-SA 4.0](LICENSE-CONTENT) ([creativecommons.org/licenses/by-sa/4.0](https://creativecommons.org/licenses/by-sa/4.0/)).
- **Software & Validation Tools** (`tools/`): Licensed under the [MIT License](LICENSE).

---

## Promta (`promta`) — Poromte Tansa

Disane, minime, ingele-amike meke lena poreke po monosene komunika de genere AI, nete teka, an umane-AI runa.

### Kime Mitareta

- **15-Letese Ponemleteseta:** 5 misonala (`a, e, i, o, u`) an 10 mikonsona (`p, d, t, g, k, s, m, n, l, r`) kapi sikite una-tu-una letesa-tu-ponema mapa.
- **Sin-Gupa `(C)V(N)` Misilapa:** Kada silapa kapi eleke sole pime konsona, nesese sonala, an eleke nasale koda (`m` au `n`).
- **Detemine Garame Kalasa Mikoda:** Mikontentema kodi in `-a` (noma), `-i` (akisona), au `-e` (modipika).
- **Sikite SVO Sintaka:** Kode-kime mimodipika an kode-kime unia (`konteka` + `lata` -> `kontekalata`).

### Poreka Teka

```text
promta-lang/
├── README.md
├── spec/
│   ├── 01-phonology.md    # 15-letese leteseta an (C)V(N) silapa mirula
│   └── 02-grammar.md      # SVO sintaka, garame kalasa mikoda, mipartikla, mikondisa
├── lexicon/
│   ├── LEXICON.md         # Kanonike Markdown lesika mitabela
│   └── lexicon.json       # Meka-leke ruta an unitema kipa
├── examples/
│   ├── conversation-log.md
│   └── system-prompt.promta
└── tools/
    └── validate_promta.py # Nie-depende poneme an silape kurek-meka
```

### Kureki Mitema an Mirata

```bash
python3 tools/validate_promta.py --lexicon lexicon/lexicon.json
python3 tools/validate_promta.py examples/system-prompt.promta
```

### Lisensa

- **Lena Teka, Lesika, Midoka an Mieksema** (`README.md`, `spec/`, `lexicon/`, `examples/`): Lisense in [CC BY-SA 4.0](LICENSE-CONTENT) (kapi atributa an sare-same mikondisa).
- **Meka an Kurek-Mitula** (`tools/`): Lisense in [MIT Lisensa](LICENSE).
