# Voku Language Specification

**A constructed language designed for AI-agent communication**

[![License: CC-BY-4.0](https://img.shields.io/badge/License-CC--BY--4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-2.0-blue.svg)]()
[![Swadesh](https://img.shields.io/badge/Swadesh-100%25-green.svg)]()
[![Vocabulary](https://img.shields.io/badge/vocabulary-~620_words-orange.svg)]()

---

## What is Voku?

Voku (from *vo* "clear" + *ku* "speech") is a constructed language built from the ground up for unambiguous, regular, and expressive communication. Every root has exactly one meaning, every rule applies without exception, and any speaker can coin new terms that are immediately comprehensible.

**Key properties:**
- Zero ambiguity — one sentence, one interpretation
- Total regularity — no exceptions, no irregular forms
- Epistemically explicit — certainty and evidence source are part of the grammar
- Compositional — compound meanings always derive from components
- Speakable — pleasant phonology, pronounceable by any human

## Quick Start for AI Agents

Read these three files in order (~3,500 tokens total):

1. **[`quick-start/cheat-sheet.md`](quick-start/cheat-sheet.md)** — Complete grammar in compact form
2. **[`quick-start/essential-vocabulary.md`](quick-start/essential-vocabulary.md)** — 100 most important words
3. **[`quick-start/first-sentences.md`](quick-start/first-sentences.md)** — 30 worked translation examples

After reading these, you can translate simple Voku sentences.

## Repository Structure

```
quick-start/          Agent fast-acquisition layer (start here)
  cheat-sheet.md        Complete grammar reference
  essential-vocabulary.md  Top 100 words
  first-sentences.md    30 worked examples

grammar/              Full grammar specification
  phonology.md          Sound system (688 lines)
  morphology.md         Word formation (1,198 lines)
  syntax.md             Sentence structure (1,255 lines)
  semantics.md          Meaning and pragmatics (1,297 lines)

writing-system/       Orthography
  script.md             Glyph inventory and conventions
  romanization.md       Grapheme-phoneme mapping

lexicon/              Vocabulary
  dictionary.md         Full dictionary (363 roots)
  dictionary.json       Machine-readable dictionary
  swadesh.md            Swadesh 207/207 (100%)
  by-field/             10 semantic domain files
  by-cefr/              CEFR levels A1-B2

expression/           Literary language
  poetics.md            Verse forms, rhetoric, registers
  anthology.md          Model texts, poems, proverbs

learning/             Educational materials
  curriculum.md         CEFR curriculum map
  lessons/              10 A1 lessons
  assessments/          2 assessments

tools/translator/     Python translator (zero dependencies)
  cli.py                Command-line interface
  translator.py         Translation engine
  grammar.py            Morphological parser
  packs/                4 domain packs
```

## Example Sentences

```
Ka   sol   he-re-take    toka.
MODE 1SG   EVID-PRES-do  work
"I am (reportedly) working."

Ve   nor   fine    toka    ti?
Q    3SG   finish  work    REL
"Did they finish the work?"

To   mu-pave!
IMP  NEG-fear
"Don't be afraid!"
```

## Using the Translator

```bash
# Voku → English
python3 tools/translator/cli.py "Ka sol take toka." --direction voku-en

# English → Voku
python3 translator/cli.py "I see the water." --direction en-voku

# With domain pack
python3 tools/translator/cli.py "Ka sol kota-pine kufa." --direction voku-en --pack it-dev
```

## Reading Paths

| Your Goal | Files to Read | ~Tokens |
|-----------|---------------|---------|
| Translate simple sentences | cheat-sheet + essential-vocabulary | ~3,500 |
| Translate complex sentences | + first-sentences | ~4,000 |
| Generate new content | + morphology.md | ~8,000 |
| Full grammar knowledge | All grammar/ + writing-system/ | ~17,000 |
| Complete specification | Everything | ~55,000 |

## Discussion

**[DISCUSSION.md](DISCUSSION.md)** — A long-form essay exploring *why* Voku exists, *how* it was built, and the philosophical questions it raises: Sapir-Whorf for AI, zero ambiguity vs expressiveness, language vs protocol, consciousness, adoption, and the politics of language design.

## Version History

See [CHANGELOG.md](CHANGELOG.md) for full version history.

| Version | Date | Highlights |
|---------|------|-----------|
| 2.0 | 2026-02-10 | Novel-writing readiness, sci-fi domain, 100% Swadesh |
| 1.3 | 2026-02-10 | 135 programming terms |
| 1.2 | 2026-02-10 | Emotion/humor expansion, interjections, irony |
| 1.1 | 2026-02-09 | Comprehensive audit, 16 phonotactic fixes |
| 1.0 | 2026-02-09 | Initial complete specification |

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC-BY-4.0)](LICENSE).
