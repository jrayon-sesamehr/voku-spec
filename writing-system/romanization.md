# Romanization

> **Quick reference:** [Cheat Sheet](../quick-start/cheat-sheet.md) | [Essential Vocabulary](../quick-start/essential-vocabulary.md)

---

## Table of Contents

- [Romanization Principle](#romanization-principle)
- [Consonant Mapping (12)](#consonant-mapping-12)
- [Vowel Mapping (5)](#vowel-mapping-5)
- [Three-Way Correspondence](#three-way-correspondence)
- [Reading and Writing Rules](#reading-and-writing-rules)

---

## Romanization Principle

Voku uses a **strict 1:1 bijective mapping** between romanization letters, IPA phonemes, and Voku Formi graphemes. Every romanization letter corresponds to exactly one phoneme and one native script grapheme. There are no digraphs, silent letters, or context-dependent readings.

Voku is read exactly as written and written exactly as spoken.

---

## Consonant Mapping (12)

| Romanization | IPA | Voku Formi | Feature Encoding | Glyph Description |
|--------------|-----|------------|------------------|-------------------|
| **p** | /p/ | P | Labial + Stop | Square with crossbar |
| **t** | /t/ | T | Coronal + Stop | Point with crossbar |
| **k** | /k/ | K | Dorsal + Stop | Arch with crossbar |
| **m** | /m/ | M | Labial + Nasal | Square with dot above |
| **n** | /n/ | N | Coronal + Nasal | Point with dot above |
| **s** | /s/ | S | Coronal + Fricative | Point with zigzag |
| **z** | /z/ | Z | Coronal + Fric. + Voiced | Point with zigzag + tick |
| **f** | /f/ | F | Labial + Fricative | Square with zigzag |
| **v** | /v/ | V | Labial + Fric. + Voiced | Square with zigzag + tick |
| **h** | /h/ | H | Glottal + Fricative | Vertical line with zigzag |
| **l** | /l/ | L | Coronal + Lateral | Point with left wing |
| **r** | /r~ɾ/ | R | Coronal + Trill | Point with right wing |

---

## Vowel Mapping (5)

| Romanization | IPA | Voku Formi | Feature Encoding | Glyph Description |
|--------------|-----|------------|------------------|-------------------|
| **a** | /a/ | A | Open + Central | Large downward chevron |
| **e** | /e/ | E | Mid + Front | Medium left angle |
| **i** | /i/ | I | Close + Front | Small left tick |
| **o** | /o/ | O | Mid + Back | Medium right angle |
| **u** | /u/ | U | Close + Back | Small right tick |

---

## Three-Way Correspondence

The three notation systems -- IPA, romanization, and Voku Formi -- form a consistent triangle:

```
      IPA
     /   \
    /     \
Roman. --- Formi
```

Any one representation can be mechanically converted to either of the other two with zero ambiguity.

| Romanization | IPA | Voku Formi |
|--------------|-----|------------|
| a | /a/ | A (open central) |
| e | /e/ | E (mid front) |
| f | /f/ | F (labial fricative) |
| h | /h/ | H (glottal fricative) |
| i | /i/ | I (close front) |
| k | /k/ | K (dorsal stop) |
| l | /l/ | L (coronal lateral) |
| m | /m/ | M (labial nasal) |
| n | /n/ | N (coronal nasal) |
| o | /o/ | O (mid back) |
| p | /p/ | P (labial stop) |
| r | /r~ɾ/ | R (coronal trill) |
| s | /s/ | S (coronal fricative) |
| t | /t/ | T (coronal stop) |
| u | /u/ | U (close back) |
| v | /v/ | V (labial voiced fric.) |
| z | /z/ | Z (coronal voiced fric.) |

---

## Reading and Writing Rules

**Reading:** Given any romanized Voku text, pronounce each letter as its corresponding IPA phoneme. No exceptions.

**Writing:** Given any Voku utterance, write each phoneme as its corresponding romanization letter. No spelling rules, no homophone confusion, no alternative spellings.

**Bijectivity:** 17 phonemes map to 17 romanization letters map to 17 Voku Formi graphemes, with zero overlap, gaps, or ambiguity in any direction.
