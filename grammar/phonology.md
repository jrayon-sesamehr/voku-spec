# Voku Phonology

> **Quick reference:** [Cheat Sheet](../quick-start/cheat-sheet.md) | [Essential Vocabulary](../quick-start/essential-vocabulary.md)

## Table of Contents

- [Phonemic Inventory](#phonemic-inventory)
  - [Consonant Inventory](#consonant-inventory-12-phonemes)
  - [Vowel Inventory](#vowel-inventory-5-phonemes)
  - [Final Vowel Classification System](#final-vowel-classification-system)
  - [Allophonic Rules](#allophonic-rules)
  - [Romanization](#romanization)
- [Phonotactics](#phonotactics)
  - [Syllable Template](#syllable-template)
  - [Onset Constraints](#onset-constraints)
  - [Coda Constraints](#coda-constraints)
  - [Consonant Cluster Prohibition](#consonant-cluster-prohibition)
  - [Compound Word Phonotactics](#compound-word-phonotactics)
  - [Minimal Pairs](#minimal-pairs)
  - [Syllabification Algorithm](#syllabification-algorithm)
- [Prosody](#prosody)
  - [Stress](#stress)
  - [Tone](#tone)
  - [Intonation](#intonation)
  - [Rhythm](#rhythm)
  - [Tempo and Pause](#tempo-and-pause)

---

## Phonemic Inventory

### Overview

Voku has a small, typologically conservative inventory of **12 consonants** and **5 vowels**. Every phoneme in the inventory is cross-linguistically common (found in >40% of surveyed languages). The system prioritizes maximum pronounceability and zero ambiguity over expressive phonetic diversity.

**Design rationale:** The inventory resembles Japanese or Finnish in size and character -- fluid, rhythmic, with predominantly open syllables and no esotic articulations. Any human speaker can produce every Voku sound without training.

---

### Consonant Inventory (12 phonemes)

#### Chart by Place and Manner of Articulation

|                        | Bilabial | Labiodental | Alveolar | Velar | Glottal |
|------------------------|----------|-------------|----------|-------|---------|
| **Plosive (voiceless)**| p /p/    |             | t /t/    | k /k/ |         |
| **Nasal**              | m /m/    |             | n /n/    |       |         |
| **Fricative (voiceless)**|        | f /f/       | s /s/    |       | h /h/   |
| **Fricative (voiced)** |          |             | z /z/    |       |         |
| **Lateral approximant**|          |             | l /l/    |       |         |
| **Trill / Tap**        |          |             | r /r~ɾ/  |       |         |

#### Individual Phoneme Details

| Phoneme | IPA  | Description                        | Romanization | Example Words                    |
|---------|------|------------------------------------|--------------|----------------------------------|
| p       | /p/  | Voiceless bilabial plosive         | p            | *pera* (error), *poro* (for), *puri* (complete), *pati* (partial), *pen* (despite), *pos* (enablement) |
| t       | /t/  | Voiceless alveolar plosive         | t            | *toka* (task), *take* (do), *tema* (time), *teru* (system), *tor* (all), *tan* (therefore) |
| k       | /k/  | Voiceless velar plosive            | k            | *kela* (information), *kele* (know), *ka* (declarative), *kes* (cause), *kon* (however), *ken* (because) |
| m       | /m/  | Bilabial nasal                     | m            | *mesa* (message), *meke* (create), *mute* (change), *motu* (method), *mas* (majority), *min* (minority) |
| n       | /n/  | Alveolar nasal                     | n            | *novi* (new), *nor* (you), *neke* (need), *nul* (nullity), *nu* (present tense) |
| s       | /s/  | Voiceless alveolar fricative       | s            | *sol* (I), *sene* (perceive), *sena* (source), *simi* (similar), *sino* (without), *supo* (below) |
| z       | /z/  | Voiced alveolar fricative          | z            | *zel* (third-unknown), *ze-* (cessative aspect) |
| f       | /f/  | Voiceless labiodental fricative    | f            | *foma* (structure), *fine* (finish), *finu* (end-of-turn), *fasi* (false), *fu-* (future tense) |
| h       | /h/  | Voiceless glottal fricative        | h            | *ha-* (known information), *he-* (inherited evidence), *he* (seven) |
| l       | /l/  | Alveolar lateral approximant       | l            | *loka* (place), *luke* (evaluate), *leni* (slow), *limi* (limited), *la* (label marker) |
| r       | /r~ɾ/| Alveolar trill or tap              | r            | *runa* (agent), *reku* (rule), *rapi* (fast), *ran* (range), *re* (corrective mode) |
| v       | /v/  | Voiced labiodental fricative       | v            | *voku* (this language), *voke* (communicate), *vel* (third-known), *veri* (true), *vasa* (quantity) |

**Note on /r/:** The specification does not mandate a distinction between trill [r] and tap [ɾ]. Both are acceptable realizations of the /r/ phoneme. Speakers may freely use either allophone.

**Note on /v/:** The original spec table lists 12 consonants but organizes them as "p, t, k, m, n, s, z, f, h, l, r" in the consonant chart. However, /v/ appears extensively in core vocabulary (*voku*, *voke*, *vel*, *veri*, *vasa*, *vo*, *va-*, *vet*, *ver-*). The phoneme /v/ is therefore part of the inventory, bringing the total to **12 consonants** as stated.

#### Typological Notes

- **Inventory size:** 12 consonants places Voku in the "small" category (6-14). Comparable to Hawaiian (8), Maori (~10), and Rotokas (6).
- **All phonemes are cross-linguistically common:** /p, t, k/ (>90%), /m, n/ (>90%), /s/ (>70%), /f, h, l/ (>40%), /r/ (>40%), /z/ (15-40%), /v/ (15-40%).
- **No voiced plosives:** Voku has /p, t, k/ but no /b, d, g/. This is typologically unmarked -- the implicational universal "if voiced stops, then voiceless stops" is satisfied vacuously.
- **One voicing pair:** /s/ ~ /z/ is the only voiced-voiceless contrast in fricatives. /f/ has no voiced counterpart /v/ in the same manner-class pairing, though /v/ exists independently.
- **No postalveolar, palatal, or uvular consonants:** The inventory is strictly anterior, keeping it maximally simple.
- **No affricates, no glottal stop, no velar nasal:** These common cross-linguistic phonemes are absent, consistent with the small inventory goal.

#### Natural Classes

| Class             | Members                     | Feature Bundle                          |
|-------------------|-----------------------------|-----------------------------------------|
| Plosives          | /p, t, k/                  | [-sonorant, -continuant]                |
| Nasals            | /m, n/                     | [+nasal, +sonorant]                     |
| Fricatives        | /s, z, f, v, h/            | [-sonorant, +continuant]                |
| Voiceless fricatives | /s, f, h/              | [-sonorant, +continuant, -voice]        |
| Voiced fricatives | /z, v/                     | [-sonorant, +continuant, +voice]        |
| Obstruents        | /p, t, k, s, z, f, v, h/  | [-sonorant]                             |
| Sonorants         | /m, n, l, r/               | [+sonorant]                             |
| Liquids           | /l, r/                     | [+sonorant, +consonantal, -nasal]       |
| Labials           | /p, m, f, v/               | [labial]                                |
| Coronals          | /t, n, s, z, l, r/         | [coronal]                               |
| Dorsals           | /k/                        | [dorsal]                                |
| Glottal           | /h/                        | [laryngeal]                             |

---

### Vowel Inventory (5 phonemes)

#### Vowel Triangle

```
        Front       Central       Back
Close    i /i/                    u /u/
Mid      e /e/                    o /o/
Open                 a /a/
```

#### Individual Vowel Details

| Phoneme | IPA  | Description                | Romanization | Example Words                    |
|---------|------|----------------------------|--------------|----------------------------------|
| i       | /i/  | Close front unrounded      | i            | *simi* (similar), *alati* (important), *novi* (new), *fasi* (false), *pati* (partial) |
| e       | /e/  | Mid front unrounded        | e            | *take* (do), *sene* (perceive), *meke* (create), *kele* (know), *neke* (need) |
| a       | /a/  | Open central unrounded     | a            | *runa* (agent), *kela* (information), *toka* (task), *mesa* (message), *foma* (structure) |
| o       | /o/  | Mid back rounded           | o            | *eno* (inside), *eso* (outside), *ano* (above), *supo* (below), *poro* (for), *kono* (with) |
| u       | /u/  | Close back rounded         | u            | *voku* (the language), *teru* (system), *motu* (method), *reku* (rule), *sipu* (scope) |

#### Typological Notes

- **System type:** 5-vowel triangular system /i, e, a, o, u/ -- the single most common vowel system worldwide (~30% of languages). Identical to Spanish, Japanese, Swahili, Latin, and Maori.
- **No vowel length contrast:** Short and long vowels are not distinguished.
- **No nasal vowels.**
- **No tone on vowels.**
- **No diphthongs:** Each vowel is a monophthong. Sequences of vowels across syllable boundaries (e.g., in *kela-alati*) are hiatus, not diphthongs.
- **Maximal dispersion:** The five vowels occupy the extreme corners plus center of the vowel space, maximizing perceptual distinctness.

---

### Final Vowel Classification System

The terminal vowel of each root morpheme determines its semantic category. This is the central morphological innovation of Voku.

| Final Vowel | Category       | Approximate Equivalent | Examples                                |
|-------------|----------------|------------------------|-----------------------------------------|
| **-a**      | Entities       | Nouns                  | *runa* (agent), *kela* (information), *toka* (task), *loka* (place), *pera* (error), *mesa* (message), *tema* (time), *sena* (source), *foma* (structure), *vasa* (quantity) |
| **-e**      | Actions        | Verbs                  | *take* (do), *sene* (perceive), *kele* (know), *meke* (create), *voke* (communicate), *mute* (change), *fine* (finish), *tore* (search), *luke* (evaluate), *neke* (need) |
| **-i**      | Qualities      | Adjectives             | *novi* (new), *veri* (true), *fasi* (false), *rapi* (fast), *leni* (slow), *puri* (complete), *pati* (partial), *simi* (similar), *alati* (important) |
| **-o**      | Relations      | Prepositions           | *eno* (inside), *eso* (outside), *ano* (above), *supo* (below), *poro* (for), *kono* (with), *sino* (without) |
| **-u**      | Abstractions   | Meta-concepts          | *voku* (this language), *teru* (system), *motu* (method), *reku* (rule), *sipu* (scope) |

**Phonological consequence:** Every content word in Voku ends in a vowel. The final vowel is part of the root and is never stripped or altered by inflection. Grammatical suffixes (e.g., voice markers *-pu*, *-se*, *-me*, *-fe*, *-pro*; certainty markers *-en*, *-ul*, *-os*) attach after the final vowel, creating new syllables.

---

### Allophonic Rules

Voku is designed for **total regularity**. Allophonic variation is minimal and never contrastive.

#### Rule 1: /r/ Realization

The phoneme /r/ may be realized as:
- [r] alveolar trill (default, formal)
- [ɾ] alveolar tap (casual, intervocalic)

Both are free variants. No minimal pair distinguishes them.

#### Rule 2: Voiceless Plosive Aspiration

/p, t, k/ are unaspirated by default [p, t, k]. Slight aspiration [pʰ, tʰ, kʰ] in word-initial position before a stressed vowel is a permissible free variant but is not phonemically distinctive.

#### Rule 3: No Vowel Reduction

Vowels maintain their full quality in all positions. Unstressed vowels are **not** reduced to schwa. The vowel /a/ is always [a], never [ə], regardless of stress.

#### Rule 4: No Assimilation

Adjacent consonants across morpheme boundaries do not assimilate in voicing or place. The sequence /n+k/ in a compound remains [n.k], not [ŋ.k].

**Summary:** Voku phonology is surface-transparent. What you see in the romanization is what you pronounce. There are no hidden alternations, no contextual neutralizations, and no phonological processes that obscure the underlying form.

---

### Romanization

Voku uses a **1:1 romanization** where each phoneme maps to exactly one Latin letter, and each Latin letter maps to exactly one phoneme.

#### Complete Romanization Table

| Phoneme | IPA   | Romanization | Notes                              |
|---------|-------|--------------|------------------------------------|
| p       | /p/   | p            | As in English "spin" (unaspirated) |
| t       | /t/   | t            | As in English "stop" (unaspirated) |
| k       | /k/   | k            | As in English "skip" (unaspirated) |
| m       | /m/   | m            | As in English "map"                |
| n       | /n/   | n            | As in English "nap"                |
| s       | /s/   | s            | As in English "sun"                |
| z       | /z/   | z            | As in English "zoo"                |
| f       | /f/   | f            | As in English "fun"                |
| v       | /v/   | v            | As in English "van"                |
| h       | /h/   | h            | As in English "hat"                |
| l       | /l/   | l            | As in English "lip"                |
| r       | /r~ɾ/ | r            | Trill or tap, as in Spanish "pero" |
| i       | /i/   | i            | As in Spanish "si"                 |
| e       | /e/   | e            | As in Spanish "me"                 |
| a       | /a/   | a            | As in Spanish "la"                 |
| o       | /o/   | o            | As in Spanish "no"                 |
| u       | /u/   | u            | As in Spanish "tu"                 |

#### Properties

- **No digraphs.** Every phoneme is one letter.
- **No diacritics.** Pure ASCII compatibility.
- **No ambiguity.** Every letter sequence has exactly one pronunciation.
- **IPA-adjacent.** The romanization is identical to IPA for all phonemes except /r/, which covers both [r] and [ɾ].
- **Keyboard-friendly.** All characters are on a standard QWERTY keyboard.

---

### Phoneme Attestation in Spec Vocabulary

The following table demonstrates that every phoneme in the inventory is attested in the specification vocabulary.

| Phoneme | Word-initial | Word-medial | Word-final (coda) |
|---------|-------------|-------------|-------------------|
| /p/     | *pera*, *poro*, *puri* | *rapi*, *sipu* | -- |
| /t/     | *toka*, *take*, *tema* | *mute*, *alati* | *vet* |
| /k/     | *kela*, *ka*, *ken* | *take*, *luke* | *ink*, *ok* |
| /m/     | *mesa*, *meke*, *motu* | *tema*, *foma* | -- |
| /n/     | *novi*, *nor*, *neke* | *sene*, *eno* | *ran*, *pen*, *kon*, *tan*, *ken*, *min* |
| /s/     | *sol*, *sene*, *sena* | *mesa*, *fasi* | *mas*, *kes*, *pos*, *vas* |
| /z/     | *zel*, *ze-* | -- | -- |
| /f/     | *foma*, *fine*, *finu* | -- | -- |
| /v/     | *voku*, *voke*, *vel* | *novi*, *alvi* | -- |
| /h/     | *ha-*, *he-*, *he* | -- | -- |
| /l/     | *loka*, *luke*, *la* | *kela*, *alati* | *sol*, *vel*, *zel*, *nul* |
| /r/     | *runa*, *reku*, *rapi* | *pera*, *poro* | *tor*, *nor*, *err* |
| /i/     | -- | *simi*, *fasi*, *alati* | -- |
| /e/     | *eno*, *eso*, *en* | *take*, *kela*, *mesa* | -- |
| /a/     | *ano*, *alati*, *alo* | *runa*, *kela*, *toka* | -- |
| /o/     | *ok* | *toka*, *foma*, *voku* | -- |
| /u/     | *un* | *runa*, *luke*, *mute* | -- |

**Note:** /z/, /f/, /h/ show limited distribution (primarily word-initial). This is consistent with the spec's vocabulary being an initial v0.1 set; the phonotactic rules permit these phonemes in all positions.

---

### Phoneme Robustness Ranking

The following ranks Voku's phonemic contrasts from most to least perceptually robust, based on acoustic distinctiveness and cross-linguistic confusion data.

| Rank | Contrast | Type | Robustness | Notes |
|------|----------|------|------------|-------|
| 1 | p/t, t/k, p/k | Place (plosives) | Very robust | Different places of articulation with distinct burst spectra; confusion rate <5% |
| 2 | f/v | Voicing (labiodental) | Robust | /f/ has high-energy frication providing additional cue beyond voicing |
| 3 | l/r | Manner (liquids) | Robust for most L1s | Lateral vs trill/tap -- robust for most speakers; risk of merger for East Asian L1 backgrounds (29 minimal pairs; high functional load) |
| 4 | m/n | Place (nasals) | Fragile in noise | Place-only distinction between nasals; ~15-20% confusion rate in degraded channels; 4 minimal pairs |
| 5 | s/z | Voicing (alveolar fricatives) | Fragile | Voicing-only distinction; /z/ devoices in final position and whispered speech; ~12-18% confusion rate; low functional load (~5.8% of vocabulary) |

#### Implications for Language Use

- **High-robustness contrasts** (ranks 1-2): Reliable in all conditions including noise, compression, and whispered speech.
- **Medium-robustness contrasts** (rank 3): Reliable for most speakers; targeted pedagogy needed for L1 backgrounds that merge /l/ and /r/.
- **Low-robustness contrasts** (ranks 4-5): Require extra articulatory care in noisy conditions. See orthography/conventions.md for disambiguation recommendations.

---

## Phonotactics

### Syllable Template

**(C)V(C)**

Every syllable in Voku has exactly one vowel as its nucleus. The onset (initial consonant) and coda (final consonant) are each optional, but limited to a single consonant.

```
Onset:   0-1 consonant (any of the 12 consonants)
Nucleus: 1 vowel (required)
Coda:    0-1 consonant (restricted set; see below)
```

#### Possible Syllable Shapes

| Shape | Structure | Example        | Source Word    |
|-------|-----------|----------------|----------------|
| V     | vowel only | /a/           | *a-* (in *ano*) |
| CV    | consonant + vowel | /ka/    | *ka* (declarative) |
| VC    | vowel + consonant | /en/    | *en* (and)     |
| CVC   | consonant + vowel + consonant | /sol/ | *sol* (I) |

**The dominant pattern is CV** (open syllables). The spec states that Voku has "predominantly open syllables," giving it a rhythm similar to Japanese or Spanish.

---

### Onset Constraints

#### Permitted Onsets

All 12 consonants may appear as syllable onsets:

| Consonant | Example Onset |
|-----------|---------------|
| /p/       | *pe.ra* |
| /t/       | *to.ka* |
| /k/       | *ke.la* |
| /m/       | *me.sa* |
| /n/       | *no.vi* |
| /s/       | *se.ne* |
| /z/       | *ze.l* |
| /f/       | *fo.ma* |
| /v/       | *vo.ku* |
| /h/       | *ha-* |
| /l/       | *lo.ka* |
| /r/       | *ru.na* |

#### Onset Clusters

**Not permitted.** No consonant clusters of any kind are allowed in onset position. The maximum onset is one consonant. Sequences like */pr/, */tr/, */kl/, */sl/ are impossible in Voku.

---

### Coda Constraints

#### Permitted Codas

Not all consonants are equally attested in coda position. Based on the v0.1 vocabulary, the following consonants appear as codas:

| Coda | Example Words | Notes |
|------|---------------|-------|
| /l/  | *sol*, *vel*, *zel*, *nul* | Very common; pronouns and particles |
| /n/  | *ran*, *pen*, *kon*, *tan*, *ken*, *min*, *ren*, *un* | Very common; connectives and particles |
| /r/  | *tor*, *par*, *nor*, *err* | Common; quantifiers and pronouns |
| /s/  | *mas*, *kes*, *pos*, *vas* | Common; causal and quantifier particles |
| /k/  | *ink*, *ok*, *vok* (in compounds) | Moderate |

#### Potential Codas (phonotactically permitted but not yet attested)

The following consonants are structurally eligible for coda position but have no attested examples in the v0.1 vocabulary:

| Coda | Status |
|------|--------|
| /p/  | Permitted -- no examples yet in spec |
| /t/  | Attested: *vet* (prohibition) |
| /m/  | Permitted -- no examples yet in spec |
| /f/  | Permitted -- no examples yet in spec |
| /z/  | Permitted -- no examples yet in spec |
| /v/  | Permitted -- no examples yet in spec |
| /h/  | Unlikely in coda -- /h/ is typically onset-only cross-linguistically |

**Design note:** Given Voku's preference for open syllables and the classificatory role of final vowels, codas appear primarily in:
1. **Monosyllabic function words** (pronouns, particles, connectives): *sol*, *nor*, *vel*, *zel*, *tor*, *par*, *mas*, *min*, *ran*, *pen*, *kon*, *tan*, *ken*, *kes*, *pos*, *ink*, *err*, *vet*, *nul*, *un*, *en*
2. **Number words**: *ok* (eight), *un* (one)
3. **The first syllable of polysyllabic content roots**: *sol.ri*, *vel.ri*

Content roots (nouns, verbs, adjectives, relations, abstractions) always end in a vowel due to the final-vowel classification system. Therefore, codas in content words only occur word-internally.

---

### Consonant Cluster Prohibition

**Voku permits no consonant clusters anywhere.** This is the single most important phonotactic constraint.

- No CC sequences within a syllable (no complex onsets, no complex codas)
- No CC sequences across syllable boundaries within a morpheme

Every consonant must be separated from any adjacent consonant by a vowel. This guarantees the maximal syllable complexity is CVC, and adjacent syllables follow patterns like:

```
CV.CV     ka.la
CVC.CV    sol.ri
CV.CVC    no.ren
CVC.CVC   (rare, only in monosyllabic sequences)
```

#### Consequences for Morphology

When affixes or compounds would create a consonant cluster, the syllable boundary falls between the consonants:

- *sol.ri* (we) -- /l/ is coda of first syllable, /r/ is onset of second
- *vel.ri* (they) -- /l/ is coda, /r/ is onset
- *nor.ri* (you all) -- /r/ is coda, /r/ is onset (geminate sequence across boundary)

Note that /nor.ri/ contains a geminate /rr/ across a syllable boundary. This is the only type of "double consonant" possible -- two identical consonants separated by a syllable boundary, each belonging to a different syllable.

---

### Compound Word Phonotactics

Compound words in Voku are formed by joining two roots with a hyphen: *modifier-nucleus*.

#### Hyphenated Compounds

| Compound | Syllabification | Structure |
|----------|----------------|-----------|
| *kela-teru* | ke.la.te.ru | CV.CV.CV.CV |
| *runa-meke* | ru.na.me.ke | CV.CV.CV.CV |
| *mesa-reku* | me.sa.re.ku | CV.CV.CV.CV |
| *kela-novi* | ke.la.no.vi | CV.CV.CV.CV |
| *pera-tore* | pe.ra.to.re | CV.CV.CV.CV |
| *runa-alati* | ru.na.a.la.ti | CV.CV.V.CV.CV |
| *kela-foma* | ke.la.fo.ma | CV.CV.CV.CV |

The hyphen in writing represents a morpheme boundary but not a phonological break. In speech, compounds are pronounced as a single phonological word with continuous syllabification.

**No cluster creation:** Because every content root ends in a vowel (final-vowel classification), and every root begins with either a vowel or a single consonant, compound formation never creates consonant clusters. The vowel ending of the first root always provides a buffer:

```
kela + teru  →  ke.la.te.ru   (V-C boundary, no cluster)
runa + alati  →  ru.na.a.la.ti   (V-V boundary, hiatus)
```

#### Hiatus in Compounds

When the first element ends in a vowel and the second element begins with a vowel, a hiatus (V.V) occurs:

- *runa-alati* → [ru.na.a.la.ti] -- the /a.a/ is resolved by syllable boundary
- *kela-eno* → [ke.la.e.no] -- /a.e/ hiatus

Hiatus is tolerated in Voku. There is no epenthetic consonant, no glide insertion, and no vowel deletion. Each vowel retains its full quality.

---

### Minimal Pairs

The following minimal pairs demonstrate that each consonant phoneme is contrastive (i.e., changing one consonant changes the meaning).

#### Consonant Contrasts

| Pair | Contrast | Phonemes Distinguished |
|------|----------|----------------------|
| *toka* (task) ~ *loka* (place) | /t/ ~ /l/ | Plosive vs. lateral |
| *take* (do) ~ *make* (create) | /t/ ~ /m/ | Plosive vs. nasal |
| *sene* (perceive) ~ *sena* (source) | /e/ ~ /a/ final | (Vowel, but also shows /sen-/ stem) |
| *kela* (information) ~ *pela* | /k/ ~ /p/ | Velar vs. bilabial plosive |
| *sol* (I) ~ *vol* | /s/ ~ /v/ | Fricative contrast |
| *mesa* (message) ~ *resa* | /m/ ~ /r/ | Nasal vs. rhotic |
| *fasi* (false) ~ *vasi* | /f/ ~ /v/ | Voiceless vs. voiced labiodental |
| *sene* (perceive) ~ *zene* | /s/ ~ /z/ | Voiceless vs. voiced alveolar fricative |
| *nor* (you) ~ *hor* | /n/ ~ /h/ | Nasal vs. glottal |
| *luke* (evaluate) ~ *ruke* | /l/ ~ /r/ | Lateral vs. rhotic |

**Note:** Some pairs above use hypothetical words (e.g., *pela*, *vasi*) to illustrate contrasts. As the lexicon expands, naturally occurring minimal pairs will replace these.

#### Vowel Contrasts

The final-vowel classification system provides systematic minimal pairs:

| Set | -a (entity) | -e (action) | -i (quality) | -o (relation) | -u (abstraction) |
|-----|-------------|-------------|---------------|----------------|-------------------|
| *mek-* | *meka* | *meke* (create) | *meki* | *meko* | *meku* (define) |
| *kel-* | *kela* (info) | *kele* (know) | *keli* | *kelo* | *kelu* |
| *vok-* | *voka* | *voke* (speak) | *voki* | *voko* | *voku* (language) |
| *mut-* | *muta* | *mute* (change) | *muti* | *muto* | *mutu* |

Each column shift changes the semantic category while preserving the root consonant skeleton.

---

### Phonotactic Constraints on Word Formation

#### Content Words (roots with classificatory vowels)

1. **Must end in a vowel** (-a, -e, -i, -o, or -u)
2. **Minimum shape:** CV (two segments) -- e.g., *ka*, *ve*, *to*, *si*, *na*, *de*, *vo*, *ko*, *re*, *su*
3. **Typical shape:** CVCV (two open syllables) -- e.g., *runa*, *take*, *novi*, *motu*
4. **Maximum attested root shape:** VCVCV (e.g., *alati*) or CVCV (e.g., *foma*, *pati*)
5. **No root begins with a consonant cluster**
6. **No root contains a consonant cluster**

#### Function Words (particles, pronouns, connectives)

1. **May end in a consonant** -- e.g., *sol*, *nor*, *vel*, *tor*, *par*, *en*, *tan*
2. **May be monosyllabic** -- e.g., *ka*, *ve*, *to*, *en*, *o*, *un*
3. **Shape range:** V, CV, VC, CVC
4. **No consonant clusters**

#### Affixes

1. **Prefixes** are typically CV- or CVC-: *te-* (past), *fu-* (future), *nu-* (present), *ko-* (atemporal), *du-* (durative), *fi-* (completive), *re-* (iterative), *ha-* (habitual), *in-* (inceptive), *ze-* (cessative), *zo-* (direct evidence), *li-* (deductive), *pe-* (reported), *mi-* (computed), *he-* (inherited), *as-* (assumed)
2. **Suffixes** are typically -CV or -CVC: *-pu* (passive), *-se* (reflexive), *-me* (reciprocal), *-fe* (causative), *-pro* (benefactive), *-en* (probable), *-ul* (uncertain), *-os* (speculative), *-ri* (plural)
3. **No affix creates a consonant cluster** when attached to a root

---

### Syllabification Algorithm

Given a Voku string, syllabification follows these rules in order:

1. **Every vowel is a syllable nucleus.**
2. **A single consonant between two vowels belongs to the onset of the following syllable:** V.CV (e.g., *ru.na*, *ke.la*)
3. **Two consonants between vowels split:** VC.CV (e.g., *sol.ri*, *vel.ri*)
4. **Word-initial consonant is an onset:** CV (e.g., *ka*, *sol*)
5. **Word-final consonant is a coda:** VC (e.g., *sol*, *nor*)

Since consonant clusters are prohibited, rule 3 never encounters three or more consonants between vowels.

#### Examples

| Word | Syllabification | Pattern |
|------|----------------|---------|
| *voku* | vo.ku | CV.CV |
| *runa* | ru.na | CV.CV |
| *kela* | ke.la | CV.CV |
| *foma* | fo.ma | CV.CV |
| *alati* | a.la.ti | V.CV.CV |
| *sol* | sol | CVC |
| *nor* | nor | CVC |
| *eno* | e.no | V.CV |
| *ano* | a.no | V.CV |
| *un* | un | VC |
| *solri* | sol.ri | CVC.CV |
| *kela-teru* | ke.la.te.ru | CV.CV.CV.CV |
| *runa-alati* | ru.na.a.la.ti | CV.CV.V.CV.CV |

---

## Prosody

### Stress

#### Primary Stress Rule

**Stress falls on the first syllable of the root.** This rule is exceptionless.

| Word | Stress Pattern | IPA |
|------|---------------|-----|
| *runa* | **RU**.na | /ˈru.na/ |
| *kela* | **KE**.la | /ˈke.la/ |
| *foma* | **FO**.ma | /ˈfo.ma/ |
| *toka* | **TO**.ka | /ˈto.ka/ |
| *voku* | **VO**.ku | /ˈvo.ku/ |
| *novi* | **NO**.vi | /ˈno.vi/ |
| *alati* | **A**.la.ti | /ˈa.la.ti/ |

**Predictability:** Because stress is always initial and fixed, it is fully predictable from the phonological form. Stress is never marked in the romanization -- the reader always knows where it falls.

#### Monosyllabic Words

Function words of one syllable (*ka*, *ve*, *to*, *sol*, *nor*, *vel*, *en*, *o*, *un*, *mu*, etc.) bear stress by default since they have only one syllable. In connected speech, they may be unstressed when they occur in rapid sequence with content words.

#### Prefixed Forms

Grammatical prefixes (tense, aspect, evidentiality, execution state) do **not** shift the stress. Stress remains on the first syllable of the **root**, not the first syllable of the word:

| Prefixed Form | Stress | IPA | Analysis |
|--------------|--------|-----|----------|
| *te-take* | te-**TA**.ke | /te.ˈta.ke/ | Past + do |
| *fu-meke* | fu-**ME**.ke | /fu.ˈme.ke/ | Future + create |
| *nu-re-take* | nu-re-**TA**.ke | /nu.re.ˈta.ke/ | Present + iterative + do |
| *te-du-take* | te-du-**TA**.ke | /te.du.ˈta.ke/ | Past + durative + do |
| *zo-sene* | zo-**SE**.ne | /zo.ˈse.ne/ | Direct-evidence + perceive |
| *li-kele* | li-**KE**.le | /li.ˈke.le/ | Deductive + know |
| *ru-take* | ru-**TA**.ke | /ru.ˈta.ke/ | Running + do |

#### Suffixed Forms

Suffixes (voice, certainty) do not shift stress either:

| Suffixed Form | Stress | IPA | Analysis |
|--------------|--------|-----|----------|
| *take-pu* | **TA**.ke.pu | /ˈta.ke.pu/ | Do + passive |
| *mute-se* | **MU**.te.se | /ˈmu.te.se/ | Change + reflexive |
| *voke-me* | **VO**.ke.me | /ˈvo.ke.me/ | Communicate + reciprocal |
| *kele-en* | **KE**.le.en | /ˈke.le.en/ | Know + probable |
| *take-ul* | **TA**.ke.ul | /ˈta.ke.ul/ | Do + uncertain |

#### Stress in Compounds

Compound words receive **two stress marks**:
- **Primary stress** on the first syllable of the first element (modifier)
- **Secondary stress** on the first syllable of the second element (nucleus)

| Compound | Stress Pattern | IPA |
|----------|---------------|-----|
| *kela-teru* | **KE**.la.**TE**.ru | /ˈke.la.ˌte.ru/ |
| *runa-meke* | **RU**.na.**ME**.ke | /ˈru.na.ˌme.ke/ |
| *mesa-reku* | **ME**.sa.**RE**.ku | /ˈme.sa.ˌre.ku/ |
| *pera-tore* | **PE**.ra.**TO**.re | /ˈpe.ra.ˌto.re/ |
| *runa-alati* | **RU**.na.**A**.la.ti | /ˈru.na.ˌa.la.ti/ |

---

### Tone

**Voku has no lexical tone.** Pitch is not used to distinguish word meanings. Two words that differ only in pitch are the same word.

This is consistent with the design goal of maximum simplicity and cross-linguistic accessibility. Tone systems (found in ~40-50% of natural languages) add complexity that Voku explicitly avoids.

---

### Intonation

While Voku has no lexical tone, it uses **sentence-level intonation contours** that correlate with the mode particles. These are prosodic defaults, not grammatical requirements -- the mode particle already disambiguates sentence type unambiguously.

#### Declarative Intonation (ka)

**Falling contour.** Pitch starts at a mid level and falls toward the end of the sentence.

```
Pitch:  ——————\
               \
                \___
        ka sol zo-sene pera eno teru
```

Pattern: mid-level through the body, falling on the final content word.

#### Interrogative Intonation (ve)

**Rising contour.** Pitch rises toward the end of the sentence.

```
Pitch:           /——
               /
        ——————/
        ve nor kele kela?
```

Pattern: mid-level through the body, rising on the final content word.

#### Imperative Intonation (to)

**Level-then-falling contour.** Pitch maintains a slightly elevated level, then drops sharply at the end.

```
Pitch:  ————————\
                  \
                   \___
        to nor take toka
```

Pattern: elevated flat pitch, sharp fall on the final word.

#### Conditional Intonation (si...ta)

**Rise-fall contour.** Pitch rises through the protasis (if-clause) and falls through the apodosis (then-clause).

```
Pitch:       /——\
            /    \
        ——/       \___
        si kela veri, sol fu-meke mesa
```

#### Other Modes

The remaining mode particles (*na*, *de*, *vo*, *ko*, *re*, *su*) generally follow the declarative falling pattern, since the particle itself already marks the illocutionary force.

---

### Rhythm

#### Mora-Timed Tendency

Voku tends toward **mora-timed rhythm** (similar to Japanese), where each mora (roughly: each V or CV unit) takes approximately equal time.

- A light syllable (CV) = 1 mora
- A heavy syllable (CVC) = 2 morae
- A vowel-only syllable (V) = 1 mora

Because Voku overwhelmingly favors open syllables (CV), most syllables are light (1 mora), creating an even, staccato-like rhythm.

#### Example Timing

```
ka   sol  zo-  se-  ne   pe-  ra   e-   no   te-  ru
CV   CVC  CV   CV   CV   CV   CV   V    CV   CV   CV
1    2    1    1    1    1    1    1    1    1    1

"Ka sol zo-sene pera eno teru"
```

The CVC syllable *sol* takes approximately twice as long as each CV syllable, giving a slight lengthening effect on closed syllables.

#### Comparison to Natural Languages

| Rhythm Type | Languages | Character |
|-------------|-----------|-----------|
| **Mora-timed** | Japanese, Finnish | Even, syllable-by-syllable pacing |
| Stress-timed | English, German, Russian | Stressed syllables at regular intervals, unstressed compressed |
| Syllable-timed | Spanish, French, Italian | Each syllable takes roughly equal time |

Voku's rhythm falls between mora-timed and syllable-timed. The predominance of CV syllables makes the distinction moot in practice -- most syllables are one mora and roughly equal in duration.

---

### Tempo and Pause

#### Conversational Turn Markers

Voku's discourse particles create natural prosodic boundaries and pauses:

| Particle | Function | Prosodic Effect |
|----------|----------|-----------------|
| *alo* | Conversation start | Followed by a pause |
| *finu* | End of turn | Preceded by a falling pitch; followed by silence |
| *tenu* | Holding the turn | Brief pause, then continuation at same pitch |
| *klosu* | End of conversation | Strong falling pitch, final silence |
| *reku* | Requesting a turn | Rising pitch on the particle |

#### Pause Placement

Natural pause points in Voku speech:

1. **After the mode particle:** *ka* [pause] *sol zo-sene pera eno teru*
2. **Before subordinate clause openers:** ... [pause] *ta* ...
3. **After subordinate clause closers:** ... *ti* [pause] ...
4. **At morpheme compound boundaries:** *kela* [micro-pause] *teru*
5. **Before and after turn markers:** [pause] *finu* [pause]
6. **Between coordinated clauses:** ... *en* [pause] ...

#### Speech Rate

No grammatical constraints on speech rate. However, the design principle of "zero ambiguity" means that fast speech does not introduce neutralizations or reductions -- every segment retains its full phonetic value regardless of tempo.

---

### Prosodic Summary

| Feature | Value | Notes |
|---------|-------|-------|
| Stress type | Fixed, initial | On first syllable of root; predictable |
| Stress in compounds | Primary + secondary | First syllable of each element |
| Lexical tone | None | Pitch does not distinguish words |
| Intonation | Contour-based | Falls for declaratives, rises for questions |
| Rhythm | Mora-timed tendency | Even pacing, predominantly open syllables |
| Vowel reduction | None | All vowels maintain full quality |
| Consonant lenition | None | No weakening in any position |
| Resyllabification | Minimal | Follows standard (C)V(C) parsing |
