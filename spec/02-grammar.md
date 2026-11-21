# 02. Core Grammar & Syntax

## 1. Word Order & Modification
* **Strict SVO (Subject – Verb – Object):** Mirrors English syntax.
  * *Mia promi moda.* — "I prompt the model."
* **Head-Final Modification:** Adjectives and adverbs always precede the word they modify.
  * *kalare repa* — "clear response"

## 2. Parts of Speech (Final Vowel Marking)
Every content word ends in a vowel marking its grammatical category:
* **-a** = Noun (*toka* = token, *proma* = prompt)
* **-i** = Verb (*toki* = to tokenize, *promi* = to prompt)
* **-e** = Adjective / Adverb (*toke* = tokenized, *prome* = prompted)

## 3. Inflectional Prefixes & Particles
* **Plural (`mi-`):** Attached before a noun (*mitoka* = tokens, *miproma* = prompts).
* **Past Tense (`pa-`):** Attached before a verb (*patoki* = tokenized, *papromi* = prompted).
* **Future Tense (`fu-`):** Attached before a verb (*futoki* = will tokenize, *fupromi* = will prompt).
* **Negation (`ne`):** Standalone particle placed immediately before a verb or adjective (*ne halui* = does not hallucinate).
* **Modal Ability (`kan`):** Standalone particle placed before a verb (*kan meki* = can make/compute).

## 4. Compounding (Head-Final)
Combine two or more roots by dropping the final vowel of each modifier root:
* *konteka* (context) + *lata* (space) → **konteklata** (context window)
* *lima* (limit) + *rela* (rail) → **limrela** (guardrail)
* *moda* (model) + *konteka* (context) + *potokola* (protocol) → **modkontekpotokola** (Model Context Protocol)

## 5. Questions, Commands & Conditionals
* **Yes/No Questions (`ka`):** Prepend `ka` to a declarative sentence without inverting word order.
  * *Ka moda patoki texta?* — "Did the model tokenize the text?"
* **Open-Ended Wh-Questions (`kua`):** Keep SVO word order and place `kua` ("what/which") in the missing slot or at the front of the clause.
  * *Kua moda parepi?* — "What did the model output?"
  * Compound interrogatives: **kuamanera** (how), **kuatempa** (when), **kualoka** (where), **kuakausa** (why).
* **Imperative Commands (Bare `-i` Verb / `plis`):** Drop the subject (`tua`) and start directly with the bare `-i` verb. Optionally prepend `plis` for softened requests.
  * *Tansi texta in Promta!* — "Translate the text into Promta!"
* **If/Then Conditionals (`si ... ten ...`):** Introduce the condition with `si` and the consequent with `ten`.
  * *Si repa esi halue, ten iteri proma.* — "If the response is hallucinated, then refine the prompt."
