# Voku Language Specification — Claude Code Project Instructions

## What This Is

This repository contains the complete specification for **Voku**, a constructed language designed for AI-agent communication. It is structured for progressive disclosure: read the minimal set of files to start translating, then go deeper as needed.

## Quick Navigation

| Goal | Read These Files |
|------|-----------------|
| Translate simple sentences | `quick-start/cheat-sheet.md` + `quick-start/essential-vocabulary.md` |
| Translate complex sentences | + `quick-start/first-sentences.md` |
| Generate new Voku content | + `grammar/morphology.md` |
| Full grammar knowledge | All `grammar/*.md` + `writing-system/*.md` |
| Look up any word | `lexicon/dictionary.md` or `lexicon/dictionary.json` |
| Domain vocabulary | `lexicon/by-field/*.md` |
| Run translator tool | `python3 tools/translator/cli.py "sentence" --direction voku-en` |

## Key Conventions

- **Phonotactics:** (C)V(C) syllables only, 12 consonants (p,t,k,m,n,s,z,f,h,l,r,v), 5 vowels (a,e,i,o,u)
- **Word classes by final vowel:** -a = noun, -e = verb, -i = adjective, -o = preposition, -u = abstraction (content words only)
- **Stress:** Always first syllable of root
- **Glossing:** Leipzig Glossing Rules, quadrilinear format (script / romanization / gloss / translation)
- **Compounding:** modifier-nucleus order (left modifies right)
- **No exceptions:** Every rule applies 100% of the time

## File Structure

```
quick-start/     → Agent fast-acquisition layer (start here)
grammar/         → Full grammar (phonology, morphology, syntax, semantics)
writing-system/  → Script and romanization
lexicon/         → Dictionary, Swadesh list, by-field, by-CEFR
expression/      → Poetics, rhetoric, anthology
learning/        → Curriculum, lessons, assessments
tools/translator → Python CLI + web translator
```

## Do Not

- Do not invent new roots without checking `lexicon/dictionary.md` for collisions
- Do not use consonant clusters — always insert a vowel between consonants
- Do not use consonants outside the 12 valid ones (no b, c, d, g, j, q, w, x, y)
- Do not assume irregular forms exist — Voku has zero exceptions
