# Script

> **Quick reference:** [Cheat Sheet](../quick-start/cheat-sheet.md) | [Essential Vocabulary](../quick-start/essential-vocabulary.md)

---

## Table of Contents

- [Script Type](#script-type)
  - [Name](#name)
  - [Classification](#classification)
  - [Design Principles](#design-principles)
  - [Comparison to Other Featural Systems](#comparison-to-other-featural-systems)
  - [Learnability](#learnability)
  - [Summary](#summary)
- [Glyph Chart](#glyph-chart)
  - [Design System Overview](#design-system-overview)
  - [Consonant Glyphs (12)](#consonant-glyphs-12)
  - [Vowel Glyphs (5)](#vowel-glyphs-5)
  - [Feature Summary Table](#feature-summary-table)
  - [Systematic Relationships](#systematic-relationships)
- [Grapheme-Phoneme Mapping](#grapheme-phoneme-mapping)
  - [Mapping Principle](#mapping-principle)
  - [Complete Mapping Table](#complete-mapping-table)
  - [Mapping Properties](#mapping-properties)
  - [Correspondence with Romanization](#correspondence-with-romanization)
  - [Unicode Private Use Area Assignment](#unicode-private-use-area-assignment)
- [Orthographic Conventions](#orthographic-conventions)
  - [Writing Direction](#writing-direction)
  - [Word Spacing](#word-spacing)
  - [Capitalization](#capitalization)
  - [Punctuation Marks](#punctuation-marks)
  - [Numeral Representation](#numeral-representation)
  - [Example Text](#example-text)
  - [Formatting Conventions Summary](#formatting-conventions-summary)
  - [Disambiguation Conventions in Speech](#disambiguation-conventions-in-speech)
  - [Quality Gate G5 Checklist](#quality-gate-g5-checklist)

---

## Script Type

### Name

**Voku Formi** (*foma* = structure + final *-i* reanalyzed as "of Voku") -- "The Voku Script"

In Voku: *Ka Voku Formi eni| foma |de-voku kela-sena.* (The Voku Script is the structural form of Voku's written source.)

---

### Classification

**Type:** Featural alphabet

A featural alphabet is a writing system in which the shapes of graphemes systematically encode the phonetic features of the sounds they represent. Glyphs that share phonetic features share visual components. The canonical example is Korean Hangul (1443 CE), designed by King Sejong and his scholars to mirror the articulatory phonetics of Korean.

Voku Formi belongs to this tradition but adapts the principle for Voku's specific inventory of 12 consonants and 5 vowels.

---

### Design Principles

#### Principle 1: Features Map to Components

Every consonant glyph is composed of two visual components:

1. **Place component** -- a base shape shared by all consonants at the same place of articulation
2. **Manner component** -- a modifier shared by all consonants with the same manner of articulation

To read or write an unknown consonant glyph, a learner decomposes it: "I see the labial base with the fricative modifier -- this must be /f/."

#### Principle 2: Vowels Encode Height and Backness

Every vowel glyph is a single form whose shape encodes:

1. **Height** -- the vertical extent of the glyph (open vowels are taller/wider, close vowels are shorter/narrower)
2. **Backness** -- the orientation or horizontal position of the distinguishing element (front vowels face left, back vowels face right, central /a/ is symmetric)

#### Principle 3: One Phoneme, One Grapheme

Voku Formi is a strict 1:1 system:
- Every phoneme has exactly one grapheme
- Every grapheme represents exactly one phoneme
- No digraphs, no silent letters, no context-dependent readings
- Total count: 17 graphemes (12 consonant + 5 vowel)

#### Principle 4: Economy Through Frequency

Frequent phonemes receive simpler glyphs (fewer strokes). Rare phonemes (/z/, /h/) may have more complex forms. This follows the cross-linguistic principle that common symbols should be fast to write.

#### Principle 5: Visual Cohesion

All glyphs share:
- A consistent stroke weight
- A modular grid basis (designed on a 5x5 unit grid)
- Consistent proportions (all consonants fit in the same bounding box, all vowels fit in a slightly narrower box)
- Angular-geometric motif with occasional curves for the liquid and nasal classes

---

### Comparison to Other Featural Systems

#### Korean Hangul

Hangul encodes place of articulation in the base consonant shape and aspiration/tenseness through added strokes. Voku Formi follows the same structural principle -- place determines the base, manner determines the modifier -- but differs in:

- **No syllable blocks.** Hangul groups consonants and vowels into syllable-square compositions. Voku Formi writes glyphs linearly, left to right, like a standard alphabet. This matches Voku's (C)V(C) syllable structure without requiring complex block composition.
- **Manner as primary modifier.** Hangul uses added strokes mainly for aspiration and tenseness. Voku Formi uses manner modifiers more broadly (stop, fricative, nasal, liquid) because Voku's consonant system is organized primarily by manner classes.
- **Vowel design.** Hangul vowels use combinations of vertical/horizontal strokes and dots. Voku Formi vowels encode height and backness through shape geometry (openness and directionality).

#### Tolkien's Tengwar

Tengwar encodes manner of articulation in the base shape (bow shape and direction) and place of articulation through stem modifications. This is the inverse of Voku Formi's approach (where place is the base and manner is the modifier). Voku Formi chose place-as-base because Voku's place categories (labial, coronal, dorsal, glottal) have unequal sizes, and grouping by place creates more visually distinctive base families.

#### Visible Speech (Alexander Melville Bell)

Visible Speech directly represents articulatory positions -- lip shape, tongue position, voicing. It prioritizes phonetic transparency over aesthetic writing. Voku Formi takes a middle path: the features encoded are phonetic (place, manner, voicing, height, backness), but the visual forms are designed for practical handwriting and aesthetic harmony, not for articulatory diagrams.

---

### Learnability

The featural design makes Voku Formi exceptionally learnable:

1. **Learn 4 place bases + 4 manner modifiers = decode all 12 consonants.** Instead of memorizing 12 arbitrary shapes, a learner masters 8 components and combines them systematically.
2. **Learn the vowel geometry principle = decode all 5 vowels.** Height maps to vertical extent, backness maps to horizontal orientation.
3. **No exceptions.** Every glyph follows the rules. There are no historical irregularities, borrowed shapes, or special cases.
4. **Predicted learning time:** A learner who understands the feature system can read all 17 graphemes within a single lesson. Compare: Latin alphabet requires memorizing 26 arbitrary letter-sound correspondences. Hangul is learnable in hours due to its featural principle. Voku Formi, with only 17 graphemes and a consistent featural system, should be learnable in under an hour.

---

### Summary

| Property | Value |
|----------|-------|
| Script name | Voku Formi |
| Type | Featural alphabet |
| Total graphemes | 17 (12 consonant + 5 vowel) |
| Consonant design | Place base + manner modifier |
| Vowel design | Height + backness geometry |
| Grid basis | 5x5 modular unit grid |
| Mapping | Strict 1:1 phoneme-grapheme |
| Design motif | Angular-geometric, modular |
| Inspiration | Hangul (featural principle), adapted for Voku |

---

## Glyph Chart

### Design System Overview

All Voku Formi glyphs are designed on a **5x5 unit grid**. Consonant glyphs occupy the full grid. Vowel glyphs occupy a narrower 3x5 portion, giving them a visually distinct, lighter profile that naturally separates them from consonants in running text.

#### Consonant Architecture

Each consonant glyph is built from two components:

1. **Place Base** -- the foundational shape, determined by place of articulation
2. **Manner Modifier** -- an added element, determined by manner of articulation

Additionally, **voicing** is encoded by a small tick mark at the bottom-left of the glyph. Only voiced consonants (/z/, /v/) carry this mark; all other consonants are voiceless (or sonorants, where voicing is not contrastive).

#### Place Bases (4)

| Place | Members | Base Shape | Description |
|-------|---------|------------|-------------|
| **Labial** | p, m, f, v | Square/box | An open or closed rectangular frame -- lips form a closed shape |
| **Coronal** | t, n, s, z, l, r | Upward point/chevron | A pointed peak or upward wedge -- tongue tip rises to the alveolar ridge |
| **Dorsal** | k | Arch/dome | A rounded arch -- the tongue dorsum rises toward the velum |
| **Glottal** | h | Vertical line | A bare stem -- the open glottis, the simplest articulator |

#### Manner Modifiers (5)

| Manner | Members | Modifier | Description |
|--------|---------|----------|-------------|
| **Stop** | p, t, k | Horizontal bar (closed) | A crossbar seals the base shape -- airflow is fully blocked |
| **Fricative** | f, v, s, z, h | Wave/zigzag on side | A wavy or angled stroke alongside the base -- turbulent airflow |
| **Nasal** | m, n | Dot above | A dot placed above the base -- air escapes through the nose |
| **Lateral** | l | Horizontal wing (left) | A horizontal stroke extending from the left side of the base -- air flows around the tongue sides |
| **Trill/Tap** | r | Horizontal wing (right) | A horizontal stroke extending from the right side of the base -- vibration of the tongue tip |

#### Voicing Mark

| Feature | Mark | Description |
|---------|------|-------------|
| **Voiced** (/z/, /v/) | Small diagonal tick at bottom-left | A short stroke at the lower-left corner of the glyph |
| **Voiceless / Sonorant** | (none) | No additional mark |

---

### Consonant Glyphs (12)

#### Stops: /p/, /t/, /k/

##### /p/ -- Voiceless bilabial stop

- **Romanization:** p
- **Features:** voiceless + labial + stop
- **Components:** Labial base (square) + stop modifier (crossbar)
- **Description:** A square frame with a horizontal crossbar through the middle, creating two stacked rectangular chambers. Resembles a window frame.

```
+---+
|   |
+---+
|   |
+---+
```

- **Mnemonic:** The square = lips, the sealed crossbar = complete closure of airflow.

##### /t/ -- Voiceless alveolar stop

- **Romanization:** t
- **Features:** voiceless + coronal + stop
- **Components:** Coronal base (upward point) + stop modifier (crossbar)
- **Description:** An upward-pointing chevron (like an inverted V) with a horizontal crossbar cutting through the lower portion. The tip points upward like the tongue tip.

```
  /\
 /  \
+----+
|    |
```

- **Mnemonic:** The upward point = tongue tip rising, the crossbar = complete closure.

##### /k/ -- Voiceless velar stop

- **Romanization:** k
- **Features:** voiceless + dorsal + stop
- **Components:** Dorsal base (arch) + stop modifier (crossbar)
- **Description:** A rounded dome or arch shape with a horizontal crossbar through the lower portion. The arch represents the tongue dorsum humping toward the velum.

```
 _____
/     \
+-----+
|     |
```

- **Mnemonic:** The dome = tongue dorsum, the crossbar = velar closure.

---

#### Nasals: /m/, /n/

##### /m/ -- Bilabial nasal

- **Romanization:** m
- **Features:** sonorant + labial + nasal
- **Components:** Labial base (square) + nasal modifier (dot above)
- **Description:** A simple square frame with a dot centered above it. The square = lips, the dot = air escaping through the nose.

```
  .
+---+
|   |
|   |
+---+
```

- **Mnemonic:** Lips (square) with nasal airflow (floating dot above).

##### /n/ -- Alveolar nasal

- **Romanization:** n
- **Features:** sonorant + coronal + nasal
- **Components:** Coronal base (upward point) + nasal modifier (dot above)
- **Description:** An upward-pointing chevron with a dot centered above the peak. The point = tongue tip at the alveolar ridge, the dot = nasal airflow.

```
  .
  /\
 /  \
/    \
```

- **Mnemonic:** Tongue tip (point) with nasal airflow (dot above the peak).

---

#### Fricatives: /s/, /z/, /f/, /v/, /h/

##### /s/ -- Voiceless alveolar fricative

- **Romanization:** s
- **Features:** voiceless + coronal + fricative
- **Components:** Coronal base (upward point) + fricative modifier (zigzag on right side)
- **Description:** An upward-pointing chevron with a small zigzag stroke descending along the right edge. The zigzag = turbulent airflow passing the alveolar ridge.

```
  /\
 /  \~
/    ~
     ~
```

- **Mnemonic:** Tongue tip (point) with turbulent air (zigzag).

##### /z/ -- Voiced alveolar fricative

- **Romanization:** z
- **Features:** voiced + coronal + fricative
- **Components:** Coronal base (upward point) + fricative modifier (zigzag on right side) + voicing tick (bottom-left)
- **Description:** Identical to /s/ but with a small diagonal tick at the bottom-left corner indicating voicing.

```
  /\
 /  \~
/    ~
/    ~
```

- **Mnemonic:** Same as /s/ + voicing tick -- the voiced counterpart.

##### /f/ -- Voiceless labiodental fricative

- **Romanization:** f
- **Features:** voiceless + labial + fricative
- **Components:** Labial base (square) + fricative modifier (zigzag on right side)
- **Description:** A square frame with a zigzag stroke descending along the right edge. Lips (square) with turbulent airflow (zigzag).

```
+---+
|   |~
|   ~
+--+~
```

- **Mnemonic:** Lips (square) with friction (zigzag).

##### /v/ -- Voiced labiodental fricative

- **Romanization:** v
- **Features:** voiced + labial + fricative
- **Components:** Labial base (square) + fricative modifier (zigzag on right side) + voicing tick (bottom-left)
- **Description:** Identical to /f/ but with a small diagonal tick at the bottom-left corner indicating voicing.

```
+---+
|   |~
|   ~
/--+~
```

- **Mnemonic:** Same as /f/ + voicing tick -- the voiced counterpart.

##### /h/ -- Voiceless glottal fricative

- **Romanization:** h
- **Features:** voiceless + glottal + fricative
- **Components:** Glottal base (vertical line) + fricative modifier (zigzag on right side)
- **Description:** A single vertical stroke with a zigzag descending along its right side. The bare stem = open glottis (simplest articulator), the zigzag = turbulent air.

```
|
|~
~
~
```

- **Mnemonic:** Open throat (bare line) with breath turbulence (zigzag).

---

#### Liquids: /l/, /r/

##### /l/ -- Alveolar lateral approximant

- **Romanization:** l
- **Features:** sonorant + coronal + lateral
- **Components:** Coronal base (upward point) + lateral modifier (horizontal wing, left side)
- **Description:** An upward-pointing chevron with a horizontal stroke extending from the left side of the base. The left wing = airflow passing around the left side of the tongue.

```
    /\
   /  \
--/    \
```

- **Mnemonic:** Tongue tip (point) with lateral airflow (wing going left).

##### /r/ -- Alveolar trill/tap

- **Romanization:** r
- **Features:** sonorant + coronal + trill
- **Components:** Coronal base (upward point) + trill modifier (horizontal wing, right side)
- **Description:** An upward-pointing chevron with a horizontal stroke extending from the right side of the base. The right wing = vibration at the tongue tip. Mirror image of /l/.

```
  /\
 /  \
/    \--
```

- **Mnemonic:** Tongue tip (point) with vibration energy (wing going right). Mirror of /l/ makes the pair easy to remember.

---

### Vowel Glyphs (5)

#### Vowel Design System

Vowel glyphs are built on a different principle than consonants. Instead of component composition, each vowel is a single geometric form whose shape encodes two features:

1. **Height** (close, mid, open): Encoded by the vertical extent and openness of the glyph
   - Close vowels (/i/, /u/): Small, compact forms -- a short mark
   - Mid vowels (/e/, /o/): Medium-sized forms -- a half-open shape
   - Open vowel (/a/): Large, wide form -- a fully open shape

2. **Backness** (front, central, back): Encoded by the direction or orientation of the glyph
   - Front vowels (/i/, /e/): Shape opens or leans to the left
   - Central vowel (/a/): Symmetric, opens in both directions or downward
   - Back vowels (/u/, /o/): Shape opens or leans to the right

#### Vowel Triangle in Glyph Space

```
Front                          Back
        (small, left)  (small, right)
Close    /i/                  /u/

        (medium, left) (medium, right)
Mid      /e/                  /o/

              (large, center)
Open              /a/
```

---

##### /a/ -- Open central unrounded

- **Romanization:** a
- **Features:** open + central
- **Description:** A wide downward-pointing chevron or open angle -- the widest vowel glyph, symmetric, opening downward. Represents the maximally open jaw.

```
\      /
 \    /
  \  /
   \/
```

- **Mnemonic:** Wide open mouth, symmetric -- the most open vowel.

##### /e/ -- Mid front unrounded

- **Romanization:** e
- **Features:** mid + front
- **Description:** A leftward-opening angle bracket of medium size. The medium size = mid height, the leftward opening = front position.

```
\
 \
 /
/
```

- **Mnemonic:** Medium-sized opening facing left = mid front vowel.

##### /i/ -- Close front unrounded

- **Romanization:** i
- **Features:** close + front
- **Description:** A small leftward-pointing tick or acute angle. The smallest vowel glyph, pointing left. Compact form = close height, leftward = front.

```
\
/
```

- **Mnemonic:** Small, sharp, pointing left = close front vowel. The smallest glyph for the highest vowel.

##### /o/ -- Mid back rounded

- **Romanization:** o
- **Features:** mid + back
- **Description:** A rightward-opening angle bracket of medium size. Mirror image of /e/. The medium size = mid height, the rightward opening = back position.

```
  /
 /
 \
  \
```

- **Mnemonic:** Medium-sized opening facing right = mid back vowel. Mirror of /e/.

##### /u/ -- Close back rounded

- **Romanization:** u
- **Features:** close + back
- **Description:** A small rightward-pointing tick or acute angle. Mirror image of /i/. Compact form = close height, rightward = back.

```
/
\
```

- **Mnemonic:** Small, sharp, pointing right = close back vowel. Mirror of /i/.

---

### Feature Summary Table

#### Consonants

| Phoneme | IPA | Roman. | Place | Manner | Voiced | Base Shape | Modifier | Voicing Mark |
|---------|-----|--------|-------|--------|--------|------------|----------|--------------|
| p | /p/ | p | Labial | Stop | No | Square | Crossbar | -- |
| t | /t/ | t | Coronal | Stop | No | Point | Crossbar | -- |
| k | /k/ | k | Dorsal | Stop | No | Arch | Crossbar | -- |
| m | /m/ | m | Labial | Nasal | (sonorant) | Square | Dot above | -- |
| n | /n/ | n | Coronal | Nasal | (sonorant) | Point | Dot above | -- |
| s | /s/ | s | Coronal | Fricative | No | Point | Zigzag right | -- |
| z | /z/ | z | Coronal | Fricative | Yes | Point | Zigzag right | Tick bottom-left |
| f | /f/ | f | Labial | Fricative | No | Square | Zigzag right | -- |
| v | /v/ | v | Labial | Fricative | Yes | Square | Zigzag right | Tick bottom-left |
| h | /h/ | h | Glottal | Fricative | No | Vertical line | Zigzag right | -- |
| l | /l/ | l | Coronal | Lateral | (sonorant) | Point | Wing left | -- |
| r | /r~ɾ/ | r | Coronal | Trill/tap | (sonorant) | Point | Wing right | -- |

#### Vowels

| Phoneme | IPA | Roman. | Height | Backness | Shape | Size | Direction |
|---------|-----|--------|--------|----------|-------|------|-----------|
| a | /a/ | a | Open | Central | Downward chevron | Large | Symmetric |
| e | /e/ | e | Mid | Front | Left angle bracket | Medium | Left-opening |
| i | /i/ | i | Close | Front | Left tick | Small | Left-pointing |
| o | /o/ | o | Mid | Back | Right angle bracket | Medium | Right-opening |
| u | /u/ | u | Close | Back | Right tick | Small | Right-pointing |

---

### Systematic Relationships

The featural design creates transparent relationships that aid learning and recognition:

#### Same Place, Different Manner

All labials share the **square base**:
- p (square + crossbar), m (square + dot), f (square + zigzag), v (square + zigzag + tick)

All coronals share the **upward point base**:
- t (point + crossbar), n (point + dot), s (point + zigzag), z (point + zigzag + tick), l (point + wing left), r (point + wing right)

#### Same Manner, Different Place

All stops share the **crossbar modifier**:
- p (square + crossbar), t (point + crossbar), k (arch + crossbar)

All fricatives share the **zigzag modifier**:
- f (square + zigzag), s (point + zigzag), h (line + zigzag)

All nasals share the **dot above modifier**:
- m (square + dot), n (point + dot)

#### Voiced-Voiceless Pairs

Voiced consonants are identical to their voiceless counterparts plus the **voicing tick**:
- /s/ vs. /z/: same glyph, /z/ adds bottom-left tick
- /f/ vs. /v/: same glyph, /v/ adds bottom-left tick

#### Vowel Mirrors

Front-back vowel pairs are horizontal mirror images:
- /i/ and /u/: same size, opposite direction
- /e/ and /o/: same size, opposite direction
- /a/ stands alone as the symmetric center

---

## Grapheme-Phoneme Mapping

### Mapping Principle

Voku Formi uses a **strict 1:1 bijective mapping** between graphemes and phonemes:

- Every phoneme has exactly **one** grapheme
- Every grapheme represents exactly **one** phoneme
- No digraphs (two letters for one sound)
- No silent letters
- No context-dependent readings
- No ambiguity in either direction (reading or writing)

This means Voku is read exactly as written and written exactly as spoken. The grapheme-phoneme correspondence is **total, exceptionless, and bidirectional**.

---

### Complete Mapping Table

#### Consonants (12)

| # | Phoneme (IPA) | Romanization | Voku Formi Grapheme | Feature Encoding | Glyph Description |
|---|---------------|--------------|---------------------|------------------|-------------------|
| 1 | /p/ | p | **P** | Labial + Stop | Square with crossbar |
| 2 | /t/ | t | **T** | Coronal + Stop | Point with crossbar |
| 3 | /k/ | k | **K** | Dorsal + Stop | Arch with crossbar |
| 4 | /m/ | m | **M** | Labial + Nasal | Square with dot above |
| 5 | /n/ | n | **N** | Coronal + Nasal | Point with dot above |
| 6 | /s/ | s | **S** | Coronal + Fricative | Point with zigzag |
| 7 | /z/ | z | **Z** | Coronal + Fric. + Voiced | Point with zigzag + tick |
| 8 | /f/ | f | **F** | Labial + Fricative | Square with zigzag |
| 9 | /v/ | v | **V** | Labial + Fric. + Voiced | Square with zigzag + tick |
| 10 | /h/ | h | **H** | Glottal + Fricative | Vertical line with zigzag |
| 11 | /l/ | l | **L** | Coronal + Lateral | Point with left wing |
| 12 | /r~ɾ/ | r | **R** | Coronal + Trill | Point with right wing |

#### Vowels (5)

| # | Phoneme (IPA) | Romanization | Voku Formi Grapheme | Feature Encoding | Glyph Description |
|---|---------------|--------------|---------------------|------------------|-------------------|
| 13 | /a/ | a | **A** | Open + Central | Large downward chevron |
| 14 | /e/ | e | **E** | Mid + Front | Medium left angle |
| 15 | /i/ | i | **I** | Close + Front | Small left tick |
| 16 | /o/ | o | **O** | Mid + Back | Medium right angle |
| 17 | /u/ | u | **U** | Close + Back | Small right tick |

---

### Mapping Properties

#### Bijectivity Proof

| Test | Result |
|------|--------|
| Total phonemes | 17 (12 C + 5 V) |
| Total graphemes | 17 (12 C + 5 V) |
| Phonemes without grapheme | 0 |
| Graphemes without phoneme | 0 |
| Phonemes with multiple graphemes | 0 |
| Graphemes with multiple phonemes | 0 |
| Digraphs required | 0 |
| Diacritics required | 0 (the voicing tick is part of the base glyph, not a separable diacritic) |

The mapping is a **perfect bijection**: 17 phonemes map to 17 graphemes with no overlap, gaps, or ambiguity.

#### Reading Algorithm

Given any Voku Formi text, the reading procedure is:

1. Identify each grapheme (no grapheme is a prefix of another; every grapheme occupies its own discrete space)
2. Map each grapheme to its unique phoneme using the table above
3. Pronounce each phoneme in sequence

There is no step that requires context, look-ahead, or disambiguation. The mapping is **locally decodable**: each grapheme can be read in isolation.

#### Writing Algorithm

Given any Voku utterance:

1. Segment the utterance into phonemes
2. Map each phoneme to its unique grapheme using the table above
3. Write the graphemes in sequence, left to right

There are no spelling rules, no homophone confusion, and no choice between alternative spellings.

---

### Correspondence with Romanization

The romanization system (documented in `phonology/inventory.md`) and Voku Formi are in perfect alignment:

| Romanization letter | Voku Formi grapheme | Phoneme |
|---------------------|---------------------|---------|
| a | A (open central) | /a/ |
| e | E (mid front) | /e/ |
| f | F (labial fricative) | /f/ |
| h | H (glottal fricative) | /h/ |
| i | I (close front) | /i/ |
| k | K (dorsal stop) | /k/ |
| l | L (coronal lateral) | /l/ |
| m | M (labial nasal) | /m/ |
| n | N (coronal nasal) | /n/ |
| o | O (mid back) | /o/ |
| p | P (labial stop) | /p/ |
| r | R (coronal trill) | /r~ɾ/ |
| s | S (coronal fricative) | /s/ |
| t | T (coronal stop) | /t/ |
| u | U (close back) | /u/ |
| v | V (labial voiced fric.) | /v/ |
| z | Z (coronal voiced fric.) | /z/ |

The three systems -- IPA, romanization, and Voku Formi -- form a consistent triangle:

```
      IPA
     /   \
    /     \
Roman. --- Formi
```

Any one representation can be mechanically converted to either of the other two with zero ambiguity.

---

### Unicode Private Use Area Assignment

For digital encoding, Voku Formi graphemes are assigned to the Unicode PUA (Basic Multilingual Plane):

#### Consonant Block (U+E000 - U+E00B)

| Code Point | Grapheme | Phoneme | Romanization |
|------------|----------|---------|--------------|
| U+E000 | P | /p/ | p |
| U+E001 | T | /t/ | t |
| U+E002 | K | /k/ | k |
| U+E003 | M | /m/ | m |
| U+E004 | N | /n/ | n |
| U+E005 | S | /s/ | s |
| U+E006 | Z | /z/ | z |
| U+E007 | F | /f/ | f |
| U+E008 | V | /v/ | v |
| U+E009 | H | /h/ | h |
| U+E00A | L | /l/ | l |
| U+E00B | R | /r~ɾ/ | r |

#### Vowel Block (U+E020 - U+E024)

| Code Point | Grapheme | Phoneme | Romanization |
|------------|----------|---------|--------------|
| U+E020 | A | /a/ | a |
| U+E021 | E | /e/ | e |
| U+E022 | I | /i/ | i |
| U+E023 | O | /o/ | o |
| U+E024 | U | /u/ | u |

#### Punctuation Block (U+E040 - U+E04F)

| Code Point | Mark | Function |
|------------|------|----------|
| U+E040 | Sentence-end (declarative) | Period equivalent |
| U+E041 | Interrogative mark | Question mark |
| U+E042 | Imperative mark | Command/exclamation mark |
| U+E043 | Clause opener | Subordinate clause start (*ta*) |
| U+E044 | Clause closer | Subordinate clause end (*ti*) |

#### Numeral Block (U+E060 - U+E069)

| Code Point | Digit | Value |
|------------|-------|-------|
| U+E060 | Voku 0 | 0 (*no*) |
| U+E061 | Voku 1 | 1 (*un*) |
| U+E062 | Voku 2 | 2 (*du*) |
| U+E063 | Voku 3 | 3 (*ti*) |
| U+E064 | Voku 4 | 4 (*ka*) |
| U+E065 | Voku 5 | 5 (*pe*) |
| U+E066 | Voku 6 | 6 (*se*) |
| U+E067 | Voku 7 | 7 (*he*) |
| U+E068 | Voku 8 | 8 (*ok*) |
| U+E069 | Voku 9 | 9 (*na*) |

Reserved ranges: U+E00C-U+E01F (future consonants), U+E025-U+E03F (future vowels/diacritics), U+E050-U+E05F (future punctuation), U+E06A-U+E07F (future numerals), U+E080-U+E0FF (ligatures, special forms).

---

## Orthographic Conventions

### Writing Direction

**Direction:** Left-to-right (LTR), top-to-bottom

- Lines begin at the left margin and proceed to the right
- New lines begin below the previous line
- This matches the world's most common writing direction and ensures compatibility with digital systems without requiring bidirectional text handling

---

### Word Spacing

**Between words:** A standard space separates words, identical in function to the Latin space character.

**Compounds:** Compound words (modifier + nucleus) are written as a single unit with a **hyphen** between components:

- *kela-teru* (information-system = database)
- *runa-meke* (agent-create = developer)
- *pera-tore* (error-search = debugging)

The hyphen is purely an orthographic convention; it does not represent a phoneme. In speech, compounds are pronounced as a single prosodic word with primary stress on the first syllable of the first component.

**Affixes and grammatical markers:** Prefixes and suffixes are written attached to their stem without hyphens:

- *tesene* (te-sene = past-perceive = perceived)
- *takefe* (take-fe = do-CAUS = cause to do)
- *seneen* (sene-en = perceive-PROB = probably perceive)

**Exception:** When a prefix or suffix is transparently segmentable and the combined form would be long (4+ syllables), a hyphen may optionally be used for readability. This is a stylistic option, not a rule:

- *te-du-take* or *tedutake* (was doing) -- both are correct

---

### Capitalization

**None.** Voku Formi has no uppercase/lowercase distinction. There is a single form for each grapheme regardless of position in the sentence. This is consistent with:

- Voku's design principle of zero ambiguity (no case-dependent meaning changes)
- Many natural scripts (Arabic, Hebrew, Georgian Mkhedruli, Thai, Hangul in practice)

Proper nouns are not capitalized. Sentence-initial letters are not capitalized. The mode particle at the beginning of each sentence (*ka*, *ve*, *to*, etc.) already signals sentence boundaries, making capitalization redundant.

---

### Punctuation Marks

Voku Formi has **5 punctuation marks**, each derived from the grammar's own structural requirements. They are visually distinct from all 17 graphemes and from each other.

#### Mark 1: Sentence-End Mark (Declarative) -- *fin*

- **Function:** Marks the end of declarative statements, confirmations, concessions, corrections, and other non-interrogative, non-imperative sentences. Used after sentences beginning with *ka*, *si*, *na*, *de*, *ko*, *re*, *su*.
- **Appearance:** A small filled square (block dot) at the baseline.

```
 .
[#]
```

- **Rationale:** The square motif echoes the labial base shape -- "closing" the utterance like lips closing. A solid, stable form signaling completion.
- **Usage:** Placed after the last word of the sentence, separated by a space.

#### Mark 2: Interrogative Mark -- *velin*

- **Function:** Marks the end of interrogative sentences (those beginning with *ve*).
- **Appearance:** A small upward-pointing chevron (like a miniature coronal base) at the baseline -- visually "raising" toward the listener, evoking the rising intonation of questions.

```
/\
```

- **Rationale:** The upward point suggests the rising contour of questions and echoes the coronal base shape. Named *velin* from *ve* (interrogative mode) + *fin* (end).
- **Usage:** Placed after the last word of interrogative sentences, separated by a space.

#### Mark 3: Imperative Mark -- *tolin*

- **Function:** Marks the end of imperative and volitive sentences (those beginning with *to* or *vo*).
- **Appearance:** A small downward-pointing chevron at the baseline -- visually "pressing down" with authority.

```
\/
```

- **Rationale:** The downward point suggests force, command, direction. Named *tolin* from *to* (imperative mode) + *fin* (end).
- **Usage:** Placed after the last word of imperative/volitive sentences, separated by a space.

#### Mark 4: Clause Opener -- *taka*

- **Function:** Marks the opening of a subordinate clause. Corresponds to the grammatical particle *ta* (and its typed variants *ta-mot*, *ta-kes*, *ta-si*, *ta-tem*, *ta-pen*).
- **Appearance:** A left-facing angle bracket -- an opening "spoken parenthesis."

```
<
```

- **Rationale:** Voku grammar already uses *ta* to open subordinate clauses and *ti* to close them. The punctuation mirrors this with visual brackets. Named *taka* from *ta* (clause opener) + *ka* (statement).
- **Usage:** Placed immediately before the subordinate clause (after *ta* or its typed variant), with a space before and after.

#### Mark 5: Clause Closer -- *tiki*

- **Function:** Marks the closing of a subordinate clause. Corresponds to the grammatical particle *ti*.
- **Appearance:** A right-facing angle bracket -- a closing "spoken parenthesis."

```
>
```

- **Rationale:** Paired with *taka* to create a visual bracketing system for clause nesting. Named *tiki* from *ti* (clause closer) + *ki* (structural).
- **Usage:** Placed immediately after *ti*, with a space before. When multiple clauses close simultaneously (multiple *ti* in sequence), each *ti* gets its own *tiki* mark: *ti > ti > ti >*

#### Punctuation Summary Table

| Mark | Name | Function | Appearance | After modes |
|------|------|----------|------------|-------------|
| *fin* | Sentence-end | Declarative termination | Filled square [#] | ka, si, na, de, ko, re, su |
| *velin* | Interrogative | Question termination | Upward chevron /\ | ve |
| *tolin* | Imperative | Command termination | Downward chevron \/ | to, vo |
| *taka* | Clause opener | Subordinate clause start | Left bracket < | (with ta) |
| *tiki* | Clause closer | Subordinate clause end | Right bracket > | (with ti) |

---

### Numeral Representation

#### Voku Numeral Glyphs

Voku Formi includes a set of 10 dedicated numeral glyphs for digits 0-9, used in base-10 positional notation. These glyphs are visually distinct from both consonant and vowel graphemes.

The numeral glyphs are designed on the same 5x5 grid but use a **circular/rounded motif** to distinguish them from the angular consonant and chevron-based vowel shapes.

| Digit | Voku Word | Glyph Description |
|-------|-----------|-------------------|
| 0 | *no* | An empty circle -- zero, nothing |
| 1 | *un* | A single vertical stroke inside a half-circle (left arc) |
| 2 | *du* | Two vertical strokes inside a half-circle |
| 3 | *nu-ti* | Three vertical strokes inside a half-circle |
| 4 | *nu-ka* | A circle with a crossbar (like a divided circle) |
| 5 | *nu-pe* | A circle with a dot at center |
| 6 | *se* | A circle with a downward stroke |
| 7 | *he* | A circle with an upward stroke |
| 8 | *ok* | A figure-eight (two stacked circles) |
| 9 | *nu-na* | A circle with a diagonal stroke |

#### Usage Rules

- Numerals are written using positional (place-value) notation, as in the Voku number system: 42 is written as the digit-4 glyph followed by the digit-2 glyph
- The decimal separator is a small horizontal dash between digits: 3.14 = digit-3 dash digit-1 digit-4
- Numerals appear inline with text at the same baseline height as vowel glyphs
- When a number is used with the *vas-* quantifier, the numeral glyphs follow *vas* directly: *vas* + digit glyphs
- Numerals do not receive any of the 5 punctuation marks; they are embedded within sentences

---

### Example Text

The following demonstrates Voku Formi conventions using romanized text with punctuation marks indicated in brackets. (Since Voku Formi glyphs cannot be rendered in plain text, the romanization stands in, and punctuation marks are shown with their names.)

#### Example 1: Simple declarative

**Romanization with punctuation:**

> ka sol zo-sene pera eno teru [fin]

**Quadrilinear format:**

```
Voku Formi:  [K][A] [S][O][L] [Z][O]-[S][E][N][E] [P][E][R][A] [E][N][O] [T][E][R][U] [#]
Romanization: ka     sol       zo-sene              pera         eno        teru          .
Gloss:        DECL   1SG      DIR.OBS-perceive      error        inside     system
Translation:  "I state: I directly observed an error in the system."
```

#### Example 2: Interrogative

> ve nor li-kele-en kela-novi [velin]

```
Romanization: ve     nor   li-kele-en           kela-novi      /\
Gloss:        Q      2SG   INFER-know-PROB      information-new
Translation:  "Do you know (probably, by inference) the new information?"
```

#### Example 3: Imperative

> to nor fu-take toka kono sol [tolin]

```
Romanization: to     nor   fu-take    toka   kono   sol    \/
Gloss:        IMP    2SG   FUT-do     task   with   1SG
Translation:  "Execute the task with me in the future."
```

#### Example 4: Nested subordinate clauses

> ka runa [taka] ta te-meke kela-foma [taka] ta eno-kele kela [tiki] ti [tiki] ti te-voke-pro sol [fin]

```
Romanization: ka  runa  < ta  te-meke  kela-foma  < ta  eno-kele  kela  > ti  > ti  te-voke-pro  sol    .
Gloss:        DECL agent  SUB PST-create info-struct  SUB  in-know   info    END    END PST-speak-BEN 1SG
Translation:  "The agent [that created the data structure [that contains the information]] communicated to me."
```

#### Example 5: Mixed sentence with numbers

> ka vas-42 runa fi-take toka [fin]

```
Romanization: ka  vas-[4][2]  runa   fi-take       toka   .
Gloss:        DECL EXACT-42   agent  CMPL-do        task
Translation:  "Exactly 42 agents completed the task."
```

---

### Formatting Conventions Summary

| Convention | Rule |
|------------|------|
| Writing direction | Left-to-right, top-to-bottom |
| Word spacing | Spaces between words |
| Compound words | Hyphen between components (*kela-teru*) |
| Affixes | Written attached to stem (*tesene*) |
| Capitalization | None (no case distinction) |
| Sentence-end (declarative) | *fin* mark [#] |
| Sentence-end (question) | *velin* mark /\ |
| Sentence-end (command) | *tolin* mark \/ |
| Clause open | *taka* mark < |
| Clause close | *tiki* mark > |
| Numerals | Dedicated glyph set, positional notation |
| Decimal separator | Horizontal dash |
| Labels (*la*) | Written in single quotes: la 'kef' |
| References (*da-*) | Written as prefix + referent: da-kef |

---

### Disambiguation Conventions in Speech

#### M/N Confusability

Both /m/ and /n/ are nasals distinguished only by place of articulation (bilabial vs alveolar). The F2 transition difference (~900 Hz vs ~1700 Hz) is brief and easily masked by noise, leading to an estimated ~15-20% confusion rate in degraded channels.

- **Known minimal pairs:** mesa/nesa, meke/neke, mute/nute, mi-/ni-
- **In writing:** The distinct Voku Formi glyphs (labial base for /m/, coronal base for /n/) provide unambiguous distinction. No change needed.
- **In speech:** In noisy or compressed channels, speakers should emphasize lip closure for /m/ -- this is a visible articulatory cue that aids disambiguation even when audio is degraded.
- **Formal/technical speech:** When the m/n contrast is critical, speakers may use emphatic articulation (slightly lengthened nasal onset) to ensure clarity.

#### S/Z Confusability

The /s/-/z/ pair is distinguished only by voicing. The phoneme /z/ devoices in final position and in whispered speech, collapsing the distinction. Additionally, /z/ has low functional load, appearing in only ~5.8% of vocabulary.

- **Known minimal pairs:** sene/zene, sela/zela, siku/ziku, soli/zoli, suma/zuma
- **Note for future versions:** Merging /z/ into /s/ would eliminate this confusion with minimal vocabulary disruption. For v1.0, /z/ remains distinct.
- **Practical tolerance:** Speakers from languages without /z/ (e.g., Spanish, Japanese) may substitute /s/ in casual speech without critical misunderstanding, given the low functional load and context-dependent disambiguation.

#### L/R Distinction

The /l/-/r/ contrast is a manner distinction (lateral approximant vs trill/tap) that is robust for most L1 backgrounds. However, speakers with East Asian L1 backgrounds (particularly Japanese, Korean, and some Chinese dialects) may merge /l/ and /r/.

- **Functional load:** These are high-functional-load phonemes with 29 minimal pairs -- merging them would cause significant ambiguity.
- **Recommendation:** Explicit L/R pronunciation practice should be included in didactic materials (A1 level). Visual articulatory guides (tongue position diagrams) are recommended.
- **No orthographic mitigation needed:** The distinct romanization letters and Voku Formi glyphs maintain written clarity regardless of spoken merger.

---

### Quality Gate G5 Checklist

| Requirement | Status |
|-------------|--------|
| Every phoneme has a grapheme (17/17) | PASS |
| Writing direction defined (LTR) | PASS |
| At least 3 punctuation marks | PASS (5 marks: fin, velin, tolin, taka, tiki) |
| Mapping is 1:1 and unambiguous | PASS |
| Example text provided | PASS |
