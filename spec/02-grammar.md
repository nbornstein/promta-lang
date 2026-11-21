# 02. Core Grammar Rules

## 1. Word Order & Modification

- **Strict SVO (Subject – Verb – Object):** Mirrors English sentence order (*Mia promi moda* = "I prompt the model").
- **Head-Final Modification:** Adjectives and adverbs always precede the word they modify (*kalare repa* = "clear response").

## 2. Parts of Speech (Final Vowel Marking)

Every content word ends in a vowel indicating its grammatical class:

| Ending | Part of Speech | Examples |
| :--- | :--- | :--- |
| **`-a`** | Noun | *toka* (token), *proma* (prompt), *moda* (model) |
| **`-i`** | Verb | *toki* (to tokenize), *promi* (to prompt), *modi* (to model) |
| **`-e`** | Adjective / Adverb | *toke* (tokenized), *prome* (prompted), *kalare* (clear/clearly) |

## 3. Inflectional Prefixes & Particles

- **Plural (`mi-`):** Attached before a noun (*mitoka* = tokens, *miproma* = prompts).
- **Past Tense (`pa-`):** Attached before a verb (*patoki* = tokenized, *papromi* = prompted).
- **Future Tense (`fu-`):** Attached before a verb (*futoki* = will tokenize, *fupromi* = will prompt).
- **Negation (`ne`):** Standalone particle placed immediately before a verb or adjective (*ne halui* = does not hallucinate).
- **Modal Ability (`kan`):** Standalone particle placed before a verb (*kan meki* = can make/compute).

## 4. Compounding (Head-Final)

Combine two or more roots by dropping the final vowel of each modifier root:

- *konteka* (context) + *lata* (space) -> **konteklata** (context window)
- *mema* (memory) + *neta* (network) -> **memneta** (RAG / retrieval-augmented network)
- *moda* (model) + *konteka* (context) + *potokola* (protocol) -> **modkontekpotokola** (Model Context Protocol)

## 5. Questions, Commands & Conditionals

- **Yes/No Questions (`ka`):** Place `ka` at the start of a statement without changing SVO word order (*Ka moda patoki texta?* -> *Ka moda patoki rata?* = "Did the model tokenize the text?").
- **Open-Ended Wh-Questions (`kua`):** Keep SVO word order and place `kua` ("what/which") in the slot of the missing information, or front it (*Moda parepi kua?* / *Kua moda parepi?* = "What did the model output?").
  - Compound interrogatives: **kuamanera** (how), **kuatempa** (when), **kualoka** (where), **kuakausa** (why).
- **Imperatives (Bare Verb / `plis`):** Drop the subject (`tua`) and start directly with the bare `-i` verb (*Tansi rata in Promta!* = "Translate the text into Promta!"). Prepend `plis` for polite/softened requests (*Plis kalari repa* = "Please clarify the response").
- **Conditionals (`si ... ten ...`):** Use `si` ("if") to introduce the condition clause and `ten` ("then") to introduce the result clause (*Si repa esi halue, ten iteri proma* = "If the response is hallucinated, then refine the prompt").
