# Promta (*promta*)

**An engineered, minimalist, English-friendly constructed language for generative AI, neural architectures, and human-AI workflows.**

Promta is designed for unambiguous, compact communication between engineers, researchers, and AI agents. Every word uses a strict **12-letter alphabet** and a regular **final-vowel part-of-speech system**, making it trivial for English speakers to learn and effortless for parsers or LLMs to tokenize deterministically.

---

## Quick Overview

* **12-Letter Alphabet:** 4 vowels (`a, e, i, u`) + 8 consonants (`p, t, k, s, m, n, l, r`)
* **Syllable Template:** Strictly `(C)V(N)` — no consonant clusters; only `m` or `n` may close a syllable
* **Word Order:** Strict **SVO** (Subject – Verb – Object); modifiers always precede heads
* **Parts of Speech:**
  * `-a` → Noun (*toka* = token, *proma* = prompt)
  * `-i` → Verb (*toki* = to tokenize, *promi* = to prompt)
  * `-e` → Adjective / Adverb (*toke* = tokenized, *prome* = prompted)
* **Inflectional Prefixes:** `mi-` (plural), `pa-` (past), `fu-` (future)
* **Core Particles:** `ne` (not), `kan` (can), `ka` (yes/no question), `si ... ten ...` (if ... then ...)

### Sample Sentences

```text
Moda empi mitoka in latempa an teni mipona in lere neta.
(Model embeds tokens into latent-embedding and attends-to weights in layered network.)
"The model embeds the tokens into latent embeddings and attends to weights in the layered network."

Tule moda tuli mitula via modkontekpotokola.
(Tool-assisted model invokes tools via Model-Context-Protocol.)
"The agentic model invokes tools via Model Context Protocol."
```

---

## Repository Structure

```text
promta-lang/
├── README.md                        # Project overview & quickstart
├── LICENSE                          # CC BY-SA 4.0 (spec) / MIT (tools)
├── .gitignore                       # Standard ignores
├── spec/
│   ├── 01-phonology.md              # 12-letter inventory, orthography & (C)V(N) rules
│   └── 02-grammar.md                # Syntax, morphology, questions, commands & conditionals
├── lexicon/
│   ├── lexicon.json                 # Machine-readable root dictionary with POS forms & tags
│   └── compounds.json               # Established head-final compound terms
├── examples/
│   ├── conversation-log.md          # Annotated parallel English <-> Promta dialogue log
│   └── agent-system-prompt.promta   # Sample AI agent system prompt in Promta + gloss
└── tools/
    └── validate_promta.py           # Zero-dependency CLI validator for alphabet & syllable rules
```

---

## Getting Started

1. **Read the Language Spec:** Start with [`spec/01-phonology.md`](spec/01-phonology.md) and [`spec/02-grammar.md`](spec/02-grammar.md).
2. **Explore the Lexicon:** Browse [`lexicon/lexicon.json`](lexicon/lexicon.json) and [`lexicon/compounds.json`](lexicon/compounds.json).
3. **Validate New Words or Texts:**
   ```bash
   python3 tools/validate_promta.py examples/agent-system-prompt.promta
   ```
