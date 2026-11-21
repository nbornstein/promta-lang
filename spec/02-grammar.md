# 02. Core Grammar Rules

## 1. Word Order & Modification

- **Strict SVO (Subject – Verb – Object):** Mirrors English sentence order (*Mia poromi moda* = "I prompt the model").
- **Head-Final Modification:** Adjectives and adverbs always precede the word they modify (*kalare repa* = "clear response").

## 2. Parts of Speech (Final Vowel Marking)

Every content word ends in a vowel indicating its grammatical class:

| Ending | Part of Speech | Examples |
| :--- | :--- | :--- |
| **`-a`** | Noun | *toka* (token), *poroma* (prompt), *moda* (model) |
| **`-i`** | Verb | *toki* (to tokenize), *poromi* (to prompt), *modi* (to model) |
| **`-e`** | Adjective / Adverb | *toke* (tokenized), *porome* (prompted), *kalare* (clear/clearly) |

## 3. Inflectional Prefixes & Particles

- **Plural (`mi-`):** Attached before a noun (*mitoka* = tokens, *miporoma* = prompts).
- **Past Tense (`pa-`):** Attached before a verb (*patoki* = tokenized, *paporomi* = prompted).
- **Future Tense (`pu-`):** Attached before a verb (*putoki* = will tokenize, *puporomi* = will prompt).
- **Negation (`ne`):** Standalone particle placed immediately before a verb or adjective (*ne alui* = does not hallucinate).
- **Modal Ability (`kan`):** Standalone particle placed before a verb (*kan meki* = can make/compute).

## 4. Compounding (Head-Final)

Combine two or more roots by dropping the final vowel only when the resulting boundary stays within `(C)V(N)`, or retaining the linking vowel when a consonant cluster would otherwise form:

- *konteka* (context) + *lata* (space) -> **kontekalata** (context window)
- *mema* (memory) + *neta* (network) -> **memneta** (RAG / retrieval-augmented network)
- *moda* (model) + *konteka* (context) + *potokola* (protocol) -> **modakontekapotokola** (Model Context Protocol)

## 5. Questions, Commands & Conditionals

- **Yes/No Questions (`ka`):** Place `ka` at the start of a statement without changing SVO word order (*Ka moda patoki rata?* = "Did the model tokenize the text?").
- **Open-Ended Wh-Questions (`kua`):** Keep SVO word order and place `kua` ("what/which") in the slot of the missing information, or front it (*Moda parepi kua?* / *Kua moda parepi?* = "What did the model output?").
  - Compound interrogatives: **kuamanera** (how), **kuatempa** (when), **kualoka** (where), **kuakausa** (why).
- **Imperatives (Bare Verb / `pilisa`):** Drop the subject (`tua`) and start directly with the bare `-i` verb (*Tansi rata in Poromta!* = "Translate the text into Promta!"). Prepend `pilisa` for polite/softened requests (*Pilisa kalari repa* = "Please clarify the response").
- **Conditionals (`si ... ten ...`):** Use `si` ("if") to introduce the condition clause and `ten` ("then") to introduce the result clause (*Si repa esi alue, ten iteri poroma* = "If the response is hallucinated, then refine the prompt").
