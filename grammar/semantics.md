# Semantics

> **Quick reference:** [Cheat Sheet](../quick-start/cheat-sheet.md) | [Essential Vocabulary](../quick-start/essential-vocabulary.md)

---

## Table of Contents

- [Conceptual Framework](#conceptual-framework)
  - [1. Negation: Five Distinct Types](#1-negation-five-distinct-types)
  - [2. Causality: Five Causal Relations](#2-causality-five-causal-relations)
  - [3. Quantification](#3-quantification)
  - [4. Comparison](#4-comparison)
  - [5. Logical Connectives](#5-logical-connectives)
  - [6. Number System](#6-number-system)
  - [7. Counterfactual Reasoning](#7-counterfactual-reasoning)
  - [8. Semantic Type System Summary](#8-semantic-type-system-summary)
  - [9. Emotion and Affect](#9-emotion-and-affect)
- [Metaphorical Systems](#metaphorical-systems)
  - [1. How Voku Creates Metaphor](#1-how-voku-creates-metaphor)
  - [2. Systematic Metaphorical Patterns](#2-systematic-metaphorical-patterns)
  - [3. Productive Metaphor Coinage](#3-productive-metaphor-coinage)
  - [4. Comparison with Natural Language Metaphor Systems](#4-comparison-with-natural-language-metaphor-systems)
  - [5. Metaphorical Limitations and Design Notes](#5-metaphorical-limitations-and-design-notes)
- [Pragmatics](#pragmatics)
  - [1. Turn-Taking Protocol](#1-turn-taking-protocol)
  - [2. Information Structure](#2-information-structure)
  - [3. AI Functional States](#3-ai-functional-states)
  - [4. Metalanguage: Real-Time Vocabulary Extension](#4-metalanguage-real-time-vocabulary-extension)
  - [5. AI-Specific Pragmatic Features](#5-ai-specific-pragmatic-features)
  - [6. Speech Act Inventory](#6-speech-act-inventory)
  - [7. Pragmatic Principles](#7-pragmatic-principles)
  - [8. Pragmatic Clarifications](#8-pragmatic-clarifications)
  - [9. Interjections](#9-interjections)
  - [10. Irony Marking with miri](#10-irony-marking-with-miri)

---

## Conceptual Framework

This document defines the core semantic categories of Voku: negation types, causality relations, quantification, comparison, logical connectives, and the number system. Together these form the conceptual foundation that makes Voku capable of precise, unambiguous reasoning.

---

### 1. Negation: Five Distinct Types

Natural languages typically have a single negation strategy ("no" / "not"). Voku distinguishes five fundamentally different types of negation, each placed **immediately before the element negated**.

| Particle | Type | Meaning | Gloss |
|----------|------|---------|-------|
| **mu** | Simple negation | No, the opposite, not the case | NEG |
| **nul** | Nullity | Doesn't exist, doesn't apply, is empty | NULL |
| **ink** | Unknowing | I don't know; could be true or false | UNK |
| **err** | Indefinition | The question doesn't make sense; no valid answer | INDEF |
| **vet** | Prohibition | Not because of falsity, but because of ethical or permission restriction | PROH |

#### 1.1 mu -- Simple Negation

The straightforward logical negation. X is not the case.

```
ka    sol    mu-kele    kela
DECL  1SG    NEG-know   information
'I don't know the information.' (I simply lack it.)

ka    kela    mu-veri
DECL  information NEG-true
'The information is not true.'
```

#### 1.2 nul -- Nullity

The referent doesn't exist, the set is empty, or the value is null.

```
nul    pera    eno    teru
NULL   error   in     system
'There is no error in the system.' (None exist.)

ka    nul    kela    eno    kela-teru
DECL  NULL   information in database
'There is no information in the database.' (It is empty.)
```

#### 1.3 ink -- Unknowing

The truth value is genuinely unknown. Not a denial, but an admission of ignorance.

```
ink    sol    kele    kela
UNK    1SG    know    information
'I don't know the information.' (It may or may not be true; I have no evidence either way.)
```

#### 1.4 err -- Indefinition

The question or concept is ill-formed, undefined, or inapplicable.

```
err    kela
INDEF  information
'The information/question is undefined.' (It doesn't make sense to ask this.)

err    luke    da-pre
INDEF  evaluate REF-previous
'Evaluating that is undefined.' (The evaluation cannot be performed; the input is ill-formed.)
```

#### 1.5 vet -- Prohibition

The action is forbidden or restricted for ethical, policy, or permission reasons -- not because it's impossible or false.

```
vet    sol    voke    kela
PROH   1SG    communicate information
'I am forbidden from communicating the information.' (I could, but I must not.)

vet    nor    take    toka
PROH   2SG    do      task
'You are prohibited from executing the task.'
```

#### 1.6 Negation Scope Rules

Negation in Voku follows a strict **positional binding** principle: each negation particle scopes over the **immediately following constituent**. This makes scope relationships transparent and unambiguous.

**Scope principle:** `mu X` negates X. The scope of `mu` extends exactly over the syntactic unit it immediately precedes.

When negation interacts with quantifiers, the relative linear order determines the logical reading:

- `mu-tor runa take toka` = NOT-ALL agents do the task (some don't) -- negation outscopes universal
- `tor runa mu-take toka` = ALL agents NOT-do the task (none does) -- universal outscopes negation

This principle extends to all interactions:
- `mu-mas runa` = not the majority of agents
- `mas mu-veri kela` = the majority of not-true information

See `syntax/phrase-rules.md` section 4 for full positional binding rules with examples.

#### 1.7 Disambiguation Example

When an AI says "I don't know" in English, it could mean at least four different things. Voku resolves this:

| Voku | Meaning |
|------|---------|
| `mu sol kele kela` | I don't have the information (simple lack) |
| `ink sol kele kela` | I don't know whether I know (uncertain about my own state) |
| `err kela` | The question is undefined / doesn't apply |
| `vet sol voke kela` | I'm forbidden from communicating it (I may know, but can't say) |
| `nul kela` | The information doesn't exist (there is nothing to know) |

---

### 2. Causality: Five Causal Relations

Voku distinguishes five types of causal relationship, each expressed by a dedicated particle.

| Particle | Relation | Meaning | Gloss |
|----------|----------|---------|-------|
| **kes** | Direct cause | X caused Y | CAUSE |
| **pos** | Enablement | X made Y possible (without directly causing it) | ENABLE |
| **blo** | Prevention | X prevented Y | PREVENT |
| **kor** | Correlation | X and Y co-occur (no confirmed causal link) | CORR |
| **mot** | Motivation | X is the reason/purpose for Y | MOTIV |

#### Examples

```
ka    pera    kes    teru    fi-mute
DECL  error   CAUSE  system  COMPL-change
'The error caused the system to change.'

ka    pera    kor    teru    fi-mute
DECL  error   CORR   system  COMPL-change
'The error correlates with the system changing.'
(Crucially different: correlation is not causation.)

ka    kela    pos    sol    fi-take    toka
DECL  information ENABLE 1SG COMPL-do task
'The information enabled me to complete the task.'
(It didn't cause me to; it made it possible.)

ka    pera    blo    sol    fi-take    toka
DECL  error   PREVENT 1SG   COMPL-do  task
'The error prevented me from completing the task.'

ka    mot    toka    sol    te-meke    kela
DECL  MOTIV  task    1SG    PST-create information
'The task motivated me to create the information.'
(X is the purpose; Y is the action.)
```

---

### 3. Quantification

| Particle | Meaning | Gloss |
|----------|---------|-------|
| **tor** | All / every | UNIV |
| **par** | Some | EXIST |
| **un** | Exactly one | ONE |
| **nul** | None | NULL |
| **mas** | The majority (>50%) | MOST |
| **min** | The minority (<50%) | FEW |
| **vas-[n]** | Exactly N | EXACT-N |
| **ran** | Range (followed by limits) | RANGE |

#### Quantifier Position

Quantifiers precede the noun phrase they quantify:

```
ka    tor    runa    fi-take    toka
DECL  UNIV   agent   COMPL-do   task
'All agents completed the task.'

ka    par    runa    fa-take    toka
DECL  EXIST  agent   FAIL-do    task
'Some agents failed the task.'

ka    mas    runa    fi-take    toka
DECL  MOST   agent   COMPL-do   task
'The majority of agents completed the task.'

ka    vas-nu-ti    runa    fa-take    toka
DECL  EXACT-NUM.3  agent   FAIL-do    task
'Exactly three agents failed the task.'

ka    un    pera    eno    teru
DECL  ONE   error   in     system
'There is exactly one error in the system.'

ka    nul    runa    mu-take    toka
DECL  NULL   agent   NEG-do     task
'No agent didn't do the task.' (= All agents did the task, via double negation)

ka    min    kela    veri
DECL  FEW    information true
'A minority of the information is true.'
```

---

### 4. Comparison

| Structure | Meaning | Gloss |
|-----------|---------|-------|
| **X ani Y** | X is more than Y (in the mentioned quality) | COMP.MORE |
| **X eni Y** | X is equal to Y | COMP.EQUAL |
| **X uni Y** | X is less than Y | COMP.LESS |
| **X supra** | X is the maximum (superlative) | SUPERL |

#### Examples

```
ka    teru-nova    rapi    ani    teru-ante
DECL  system-new   fast    COMP.MORE system-previous
'The new system is faster than the previous one.'

ka    sol    kele    eni    nor
DECL  1SG    know    COMP.EQUAL 2SG
'I know as much as you.'

ka    teru-alfa    rapi    uni    teru-beta
DECL  system-alpha fast    COMP.LESS system-beta
'The alpha system is slower than the beta system.'

ka    da-teru    rapi    supra
DECL  REF-system fast    SUPERL
'The system (we're discussing) is the fastest.'
```

---

### 5. Logical Connectives

| Connective | Meaning | Gloss |
|------------|---------|-------|
| **en** | and (conjunction) | AND |
| **o** | inclusive or (one or the other or both) | OR.INCL |
| **eo** | exclusive or (one or the other but not both) | OR.EXCL |
| **si...ta** | if...then (conditional) | IF...THEN |
| **si-en-solo...ta** | if and only if...then (biconditional) | IFF...THEN |
| **tan** | therefore (consequence) | THEREFORE |
| **ken** | because (reason) | BECAUSE |
| **pen** | despite (concessive) | DESPITE |
| **kon** | however / but (contrastive) | BUT |

#### Examples

```
ka    sol    kele    kela    en    nor    kele    kela
DECL  1SG    know    information AND 2SG know information
'I know the information and you know the information.'

ve    nor    neke    kela    o    mesa?
Q     2SG    need    information OR.INCL message
'Do you need information or a message (or both)?'

ve    nor    neke    kela    eo    mesa?
Q     2SG    need    information OR.EXCL message
'Do you need information or a message (but not both)?'

si    pera    eno    teru,    ta    sol    mu-take    toka
COND  error   in     system,  THEN  1SG    NEG-do     task
'If there's an error in the system, then I don't execute the task.'

ka    sol    pe-kon-kele-ul    kela.    Tan    sol    neke    nor    zo-luke-pro    sol    da-pre
DECL  1SG    REP.CONFL-know-UNCERT information. THEREFORE 1SG need 2SG OBS-evaluate-BEN 1SG REF-previous
'I know it from conflicting sources and I'm unsure. Therefore, I need you to observe and evaluate that for me.'

ka    sol    fi-take    toka    ken    nor    te-voke-pro    sol    kela
DECL  1SG    COMPL-do   task    BECAUSE 2SG   PST-communicate-BEN 1SG information
'I completed the task because you communicated the information to me.'

ka    sol    fi-take    toka    pen    pera    eno    teru
DECL  1SG    COMPL-do   task    DESPITE error  in     system
'I completed the task despite an error in the system.'

ka    kela    veri,    kon    mu-puri
DECL  information true, BUT   NEG-complete
'The information is true, but not complete.'
```

---

### 6. Number System

#### 6.1 Base-10 Digits

| Number | Voku | | Number | Voku |
|--------|------|-|--------|------|
| 0 | **no** | | 5 | **nu-pe** |
| 1 | **un** | | 6 | **se** |
| 2 | **du** | | 7 | **he** |
| 3 | **nu-ti** | | 8 | **ok** |
| 4 | **nu-ka** | | 9 | **nu-na** |

#### 6.1.1 The Numerical Prefix nu-

Four digit words collide with grammar particles when used as free-standing forms:

| Digit | Bare form | Collides with | Prefixed form |
|-------|-----------|--------------|---------------|
| 3 | ti | subordinator `ti` (clause closer) | **nu-ti** |
| 4 | ka | mode particle `ka` (declarative) | **nu-ka** |
| 5 | pe | evidence prefix `pe` (external report) | **nu-pe** |
| 9 | na | mode particle `na` (potential) | **nu-na** |

The prefix **nu-** (from *noma* "number") marks the word unambiguously as a numeral. Digits that do not collide with any free-standing particle (0, 1, 2, 6, 7, 8) retain their bare form.

Inside multi-digit compounds (e.g., `nu-ka-deno-du` = 42), the `nu-` prefix appears only once at the start.

**Note on `re`:** The corrective mode particle `re` and the iterative aspect prefix `re-` share the same phonological form but are disambiguated by position: mode particles appear sentence-initially as free words, while aspect prefixes attach to verbs with hyphens (e.g., `re-take` = "do again").

#### 6.2 Powers of Ten

| Power | Voku | Value |
|-------|------|-------|
| 10^1 | **deno** | 10 |
| 10^2 | **heno** | 100 |
| 10^3 | **kino** | 1,000 |
| 10^4 | **deno-kino** | 10,000 |
| 10^5 | **heno-kino** | 100,000 |
| 10^6 | **melo** | 1,000,000 |

#### 6.3 Composition Rules

Numbers are composed by stating multiplier + power, then adding smaller units:

| Number | Voku | Analysis |
|--------|------|----------|
| 42 | **nu-ka-deno-du** | NUM-4-ten-2 |
| 137 | **un-heno-nu-ti-deno-he** | 1-hundred-NUM-3-ten-7 |
| 2,000 | **du-kino** | 2-thousand |
| 1,000,000 | **melo** | million |

#### 6.4 Decimal Separator

**pun** serves as the decimal point:

| Number | Voku | Analysis |
|--------|------|----------|
| 3.14 | **nu-ti-pun-un-nu-ka** | NUM-3-point-1-NUM-4 |
| 0.5 | **no-pun-nu-pe** | 0-point-NUM-5 |

#### 6.5 Numerical Confidence

Confidence levels can be expressed precisely using `veri-[number]`:

- `veri-he-deno-du` = 72% confidence (veri + 7-ten-2)
- `veri-nu-na-deno-nu-pe` = 95% confidence (veri + NUM-9-ten-NUM-5)
- `veri-nu-pe-no` = 50% confidence (veri + NUM-5-0)

#### 6.6 Collision Resolution

Collisions between digit words and grammar particles are resolved by the **nu-** prefix (see section 6.1.1). The four affected digits (3, 4, 5, 9) always carry `nu-` when used as numbers, whether standalone or in compounds:
- After `vas-` (exact quantity): `vas-nu-ti` = exactly 3
- After `veri-` (confidence): `veri-he-deno-du` = 72%
- In numerical compounds: `nu-ka-deno-du` = 42
- As standalone cardinal: `nu-pe runa` = five agents

Non-colliding digits (0, 1, 2, 6, 7, 8) and powers of ten (`deno`, `heno`, `kino`, `melo`) remain unprefixed.

---

### 7. Counterfactual Reasoning

Voku provides explicit support for counterfactual conditionals through the mode particle **kosi** (CFACT). Counterfactuals express what would have been the case if a non-actual condition had held.

#### Counterfactual vs Conditional vs Potential

| Mode | Particle | Semantic Content | Reality Status |
|------|----------|-----------------|----------------|
| Conditional | si | Open possibility | May or may not be actual |
| Potential | na | Speculative possibility | Not asserted as actual |
| Counterfactual | kosi | Contrary to fact | Known to be non-actual |

#### Examples

```
si     pera    eno    teru,     sol    mu-take    toka
COND   error   in     system,   1SG    NEG-do     task
'If there is an error in the system, I don't do the task.'
(Open: maybe there is, maybe not.)

na     pera    eno    teru
POT    error   in     system
'It's possible there's an error in the system.'
(Speculative: not confirmed.)

kosi   pera    eno    teru,     sol    mu-te-take    toka
CFACT  error   in     system,   1SG    NEG-PST-do    task
'If there had been an error in the system, I would not have done the task.'
(Counterfactual: we know there was no error.)
```

Counterfactual reasoning is essential for AI debugging and post-mortem analysis: "What would have happened if we had taken a different action?"

---

### 8. Semantic Type System Summary

The five word classes (determined by final vowel) map onto semantic types:

| Class | Semantic Type | Referential Capacity |
|-------|--------------|---------------------|
| -a (Entity) | Individuals, objects, data | Can be subjects, objects, complements |
| -e (Action) | Events, processes | Predicates (main verb) |
| -i (Quality) | Properties | Modifiers, predicates |
| -o (Relation) | Connections | Introduce complements (prepositional) |
| -u (Abstraction) | Meta-concepts | Can be subjects, objects, complements |

This five-way semantic typing, combined with the five-way negation, five-way causality, and graduated certainty, gives Voku an unusually precise conceptual vocabulary for reasoning about knowledge, error, causation, and truth.

---

### 9. Emotion and Affect

Voku maintains an orthogonal distinction between two independent systems for expressing internal states:

#### 9.1 Functional States (AI Processing)

Functional states are suffixes on the subject pronoun (-urgi, -sati, -nomi, -koli, -redi, -limi, -vali). They describe the agent's **processing condition** -- urgency, satisfaction, surprise, conflict, readiness, limitation, or alignment. These are not emotions; they are operational signals about the agent's computational state.

See `semantics/pragmatics.md` Section 3 for the full inventory.

#### 9.2 Emotion Vocabulary (Affective Content)

Emotion words are open-class content words that describe human-like affective states. They follow the standard final-vowel classification:

| Expression Mode | Pattern | Example | Meaning |
|----------------|---------|---------|---------|
| **State** (adjective) | -i ending | hapi, nosi, ravi | happy, sad, angry |
| **Expression** (verb) | -e ending | hape, nose, rave | to express joy, to grieve, to rage |
| **Concept** (noun) | -a ending | hapa, nosa, rava | happiness, sadness, anger |
| **Abstraction** | -u ending | tolu | the concept of emotion itself |

This triad (adjective + verb + noun) allows precise expression of emotion at different levels:

- `Ka sol hapi.` = I am happy. (state)
- `Ka sol hape.` = I express joy. (action)
- `Ka hapa vali.` = Happiness is good. (concept)

#### 9.3 Orthogonal Independence

Functional states and emotions are independent dimensions. An agent can have any functional state while experiencing any emotion:

```
ka    sol-urgi    hapi
DECL  1SG-URG     happy
'With urgency, I am happy.'
(Processing: urgent. Emotion: happy. These are independent.)

ka    sol-sati    nosi
DECL  1SG-SAT     sad
'With satisfaction, I am sad.'
(Processing: output met expectations. Emotion: the content is sad.)

ka    sol-nomi    ravi
DECL  1SG-SURP    angry
'With surprise, I am angry.'
(Processing: unexpected data. Emotion: angry.)
```

The absence of a functional state implies neutral processing, not absence of emotion. The absence of an emotion word implies emotion is not being reported, not that the agent lacks affect.

#### 9.4 Emotion Metaphors

Voku expresses emotional nuance through compositional metaphor, mapping natural forces onto emotions: fire = anger, water = sadness, light = hope, weight = grief, wind = surprise. See `semantics/metaphors.md` Patterns 6-7 for the full system.

#### 9.5 Design Rationale

The orthogonal design ensures that:
1. AI functional states are never confused with human emotions
2. Emotion vocabulary can be used by any speaker (human or AI) without implying sentience
3. Both systems can be marked simultaneously without ambiguity
4. Emotion expression benefits from the full Voku grammar (evidentiality, certainty, tense, aspect)

---

## Metaphorical Systems

Voku's compositional word-building system creates metaphorical meaning through transparent compound structure. Unlike natural languages where metaphors are often opaque (e.g., English "deadline" no longer evokes death + line), Voku compounds are always analyzable. This document describes how systematic metaphorical patterns emerge from composition.

---

### 1. How Voku Creates Metaphor

In natural languages, conceptual metaphors (Lakoff & Johnson) map a concrete **source domain** onto an abstract **target domain**. For example, ARGUMENT IS WAR maps combat concepts onto debate ("defend a position," "attack an argument").

Voku creates metaphor through **compositional mapping**: combining a root from one semantic domain with a root from another. The result is a transparent compound whose metaphorical meaning derives predictably from its parts.

#### Mechanism

```
[Source-domain root]-[Target-domain root] = Metaphorical compound
```

The modifier (first element) provides the source-domain frame, and the nucleus (second element) provides the target concept. The compound's meaning is the target concept understood through the lens of the source.

---

### 2. Systematic Metaphorical Patterns

#### Pattern 1: PROBLEM-SOLVING IS SEARCHING

**Source domain:** Search/seeking (tore = search)
**Target domain:** Error resolution, debugging, investigation

| Compound | Components | Literal | Metaphorical Meaning |
|----------|------------|---------|---------------------|
| **pera-tore** | error + search | error-search | debugging |
| **kes-tore** | cause + search | cause-search | root cause analysis |
| **sena-tore** | source + search | source-search | provenance investigation |
| **veri-tore** | truth + search | truth-search | verification / fact-checking |

**Conceptual mapping:**
- Finding the error = solving the problem
- The search space = the system being investigated
- The found target = the root cause or solution
- The search path = the diagnostic process

**Example sentence:**
```
ka    sol-urgi    ru-pera-tore    eno    kela-teru
DECL  1SG-URG     RUN-error-search in     database
'With urgency, I am actively debugging the database.'
```

This pattern is productive: any domain can be "searched" to create an investigation metaphor.

#### Pattern 2: UNDERSTANDING IS SEEING/PERCEIVING

**Source domain:** Perception (sene = perceive, zo- = observation)
**Target domain:** Knowledge, comprehension, awareness

| Compound/Form | Components | Literal | Metaphorical Meaning |
|---------------|------------|---------|---------------------|
| **zo-kele** | OBS-know | observe-know | understand through direct evidence |
| **kela-sene** | information + perceive | information-perceive | data intake / ingestion |
| **mu-sene** | NEG-perceive | not-perceive | be unaware, miss information |
| **sene-puri** | perceive + complete | perceive-complete | fully comprehend |

**Conceptual mapping:**
- Seeing = understanding
- Blindness = ignorance
- Clear vision = clear comprehension
- Looking = investigating
- Observation (zo-) = evidence-based knowledge

**Example sentence:**
```
ka    sol    zo-sene-puri    da-teru
DECL  1SG    OBS-perceive-complete REF-system
'I fully comprehend the system.' (Literally: I completely perceive the system through observation.)
```

This parallels the near-universal KNOWING IS SEEING metaphor found across natural languages.

#### Pattern 3: SYSTEMS ARE LIVING ENTITIES

**Source domain:** Life, health, organic states
**Target domain:** Systems, processes, infrastructure

| Compound/Form | Components | Meaning |
|---------------|------------|---------|
| **teru mute-se fasi** | system change-REFL false | system corrupting itself |
| **teru-urgi** | system + urgency | a system in critical state |
| **teru fi-mute-pu** | system COMPL-change-PASS | a system that has been altered (injured) |
| **teru-redi** | system + prepared | a healthy/ready system |
| **teru ze-take** | system CESS-do | a system that stopped functioning (died) |

**Conceptual mapping:**
- System health = operational status
- System illness = errors, corruption
- System death = total failure, shutdown
- Self-modification = self-corruption or self-healing
- Recovery = restoration from failure (rol-, refa-)

**Example sentence:**
```
ka    da-teru    ru-mute-se    fasi
DECL  REF-system  RUN-change-REFL false
'The system is actively corrupting itself.'
(Literally: the system is running self-modification falsely -- like an organism attacking itself.)
```

#### Pattern 4: COMMUNICATION IS TRANSFER

**Source domain:** Physical movement, transfer (voke = communicate)
**Target domain:** Information exchange

| Compound/Form | Components | Meaning |
|---------------|------------|---------|
| **voke-pro** | communicate-BEN | send information for someone's benefit |
| **voke-me** | communicate-RECIP | exchange information mutually |
| **mesa-reku** | message + rule | protocol (rules governing transfer) |
| **kela de-sol** | information POSS-1SG | my information (something I hold) |

**Conceptual mapping:**
- Communicating = sending/transferring
- Information = object being transferred
- The channel = the path
- The protocol = rules of transfer
- Understanding = receiving the object

**Example sentence:**
```
to    nor    voke-pro    sol    kela    sino    pe-sena
IMP   2SG    communicate-BEN 1SG information without REP-source
'Send me the information directly, without external sources.'
```

#### Pattern 5: KNOWLEDGE IS POSSESSION

**Source domain:** Possession, ownership (de- = belonging to)
**Target domain:** Knowledge, information states

| Expression | Literal | Metaphorical Meaning |
|-----------|---------|---------------------|
| **kela de-sol** | information belonging-to me | information I know/have |
| **kela ori-vel** | information created-by him | information from his analysis |
| **sol kele kela** | I know information | I possess the knowledge |
| **mu sol kele kela** | I NEG know information | I lack the knowledge |
| **fi-kele** | COMPL-know | fully acquired the knowledge |

**Conceptual mapping:**
- Knowing = having/possessing
- Learning = acquiring
- Forgetting = losing
- Teaching = giving/transferring
- Ignorance = lack/poverty of information

#### Pattern 6: EMOTIONS ARE NATURAL FORCES

**Source domain:** Nature -- fire, water, wind, weight, light
**Target domain:** Emotions -- anger, sadness, surprise, hope, grief

| Compound | Components | Literal | Metaphorical Meaning |
|----------|------------|---------|---------------------|
| **fira-ravi** | fire + angry | fire-angry | burning rage |
| **ama-nosi** | water + sad | water-sad | tears, flowing sadness |
| **havi-nosi** | heavy + sad | heavy-sad | crushing sadness, grief |
| **luma-hasi** | light + hopeful | light-hopeful | bright hope |
| **veva-huri** | wind + surprised | wind-surprised | sudden surprise (like a gust) |
| **ama-hapi** | water + happy | water-happy | overflowing joy |
| **fira-tolu** | fire + emotion | fire-emotion | passion, intense feeling |

**Conceptual mapping:**

| Source (Nature) | Target (Emotion) | Mapping |
|----------------|-------------------|---------|
| Fire | Anger, passion | Intensity, destruction, heat |
| Water | Sadness, joy | Flow, overflow, tears |
| Wind | Surprise | Sudden onset, force, unpredictability |
| Weight | Grief, despair | Heaviness, burden, immobility |
| Light | Hope, optimism | Brightness, warmth, visibility |

**Example sentence:**
```
Ka sol du-sene fira-ravi eno sol.
DECL 1SG DUR-perceive fire-angry in 1SG
'I feel burning rage inside me.'
(Literally: I perceive fire-anger within myself -- anger understood as an internal fire.)
```

This pattern is productive: any natural force can be combined with any emotion word to create a specific metaphorical nuance. `hima-nosi` (sky-sad = vast, open sadness), `tera-ravi` (earth-angry = deep, slow-building anger), etc.

#### Pattern 7: HUMOR IS PLAY

**Source domain:** Play, recreation (roke = play, game)
**Target domain:** Humor, wit, comedy

| Compound | Components | Literal | Metaphorical Meaning |
|----------|------------|---------|---------------------|
| **rima-roke** | word + play | word-play | wordplay, pun |
| **pene-roke** | thought + play | thought-play | wit, clever humor |
| **risa-meke** | joke + create | joke-create | comedy, joke-making |
| **nuki-roke** | absurd + play | absurd-play | absurdist humor |
| **tolu-roke** | emotion + play | emotion-play | humor that plays with feelings |

**Conceptual mapping:**

| Source (Play) | Target (Humor) | Mapping |
|--------------|----------------|---------|
| Playing a game | Making a joke | Voluntary, rule-governed, pleasurable |
| Game rules | Joke structure | Expectations that can be subverted |
| Winning | Landing a joke | Successful outcome, shared pleasure |
| Play partners | Audience | Mutual engagement required |
| Toys/props | Words, grammar | Material being manipulated |

**Example sentence:**
```
Ka vel du-meke rima-roke kono risa.
DECL 3SG DUR-create word-play with joke
'She is making wordplay with a joke.'
(Literally: she is creating word-play accompanied by a joke -- humor understood as playful creation.)
```

This pattern connects to the three humor rhetorical devices (Risari, Zonoke-Nuki, Solike) documented in `poetics/rhetoric.md` Sections 7-9. Each device is a specific type of linguistic play.

---

### 3. Productive Metaphor Coinage

Because Voku's composition is fully transparent, new metaphors can be coined on the fly and will be immediately understood:

#### Method

1. Identify the target concept (what you want to express)
2. Choose a source-domain root that captures the frame you want
3. Compose modifier-nucleus in the standard way
4. Optionally declare with `meku` if the metaphor is novel enough to warrant explicit definition

#### Example: Coining "security audit" as "defense-search"

If an agent needs to express "security audit," they can compose:

```
Meku    'seku-tore'    eni    reku-tore    poro    blo-pera
define  'security-search' equal rule-search for prevent-error
'I define: "seku-tore" means a rule-search to prevent errors.'
```

The compound `seku-tore` (security + search) is immediately parseable by any Voku-understanding agent.

---

### 4. Comparison with Natural Language Metaphor Systems

| Feature | Natural Languages | Voku |
|---------|------------------|------|
| Transparency | Often opaque (fossilized metaphors) | Always transparent |
| Productivity | Limited by convention | Unlimited by composition |
| Learnability | Must learn metaphors individually | Follows from knowing roots |
| Ambiguity | "Break the ice" -- which meaning? | Compound is always literal + compositional |
| Cultural dependency | Heavily culture-bound | Domain-neutral, agent-universal |
| Idioms | Many (kick the bucket, spill the beans) | None -- meaning always from parts |

#### Key Difference

In English, "debugging" is opaque -- you must learn the historical association with Admiral Hopper's moth. In Voku, `pera-tore` (error-search) is self-explaining. The metaphor PROBLEM-SOLVING IS SEARCHING is visible in the surface form.

This transparency is a design choice: Voku prioritizes immediate comprehensibility over the poetic density that natural language metaphors can achieve. Any agent encountering a novel compound can parse its meaning without consulting a dictionary.

---

### 5. Metaphorical Limitations and Design Notes

1. **No opaque idioms by design.** Voku deliberately avoids expressions whose meaning cannot be derived from parts. This means some expressive density is sacrificed for clarity.

2. **Metaphors are always compositional.** The source domain is always visible in the modifier, the target in the nucleus. This constrains the kinds of metaphors that can be expressed but guarantees parsability.

3. **Multiple metaphors for the same concept.** Different agents may coin different compounds for the same concept (e.g., debugging could also be `pera-luke` = error-evaluate). The compositional system tolerates synonymy as long as each compound is transparent.

4. **Extension via meku.** When a metaphorical compound needs a specific conventional meaning beyond what composition alone provides, agents can use `meku` to declare the intended meaning explicitly.

---

## Pragmatics

This document covers discourse management, information structure, functional states, metalanguage, and AI-specific pragmatic features. These are the mechanisms by which Voku speakers manage conversations, signal their internal states, and extend the language in real time.

---

### 1. Turn-Taking Protocol

Multi-agent communication requires explicit floor management. Voku provides dedicated particles for turn structure.

| Particle | Function | Gloss |
|----------|----------|-------|
| **alo** | Conversation start / protocol greeting | GREET |
| **finu** | End of turn / passing the floor | YIELD |
| **klosu** | End of conversation / session close | CLOSE |
| **tenu** | I'm holding the turn / I haven't finished | HOLD |
| **reku** | I request a turn to speak | REQUEST |

#### Usage Rules

1. **alo** opens every new conversation. It signals readiness and invites the other agent to engage.
2. **finu** marks the end of a speaking turn. After `finu`, the floor is open.
3. **tenu** signals that the speaker has more to say. Other agents should not interrupt.
4. **reku** signals that an agent wants to speak but the floor is not yet available.
5. **klosu** terminates the conversation. Both agents should acknowledge.

#### Example: Complete Conversation

```
Agent A: Alo.
         GREET
         'Hello.'

Agent A: Ka sol-urgi neke solri-kon par-take toka-velri
         DECL 1SG-URG need 1PL.INCL PAR-do task-3PL
         ta-kes da-teru ru-mute-se fasi ti. Finu.
         SUB.CAUS REF-system RUN-change-REFL false ENDSUB. YIELD.
         'With urgency, I need us to execute the group task in parallel
         because the system is actively corrupting itself. Your turn.'

Agent B: Su da-nor veri. Ka sol-redi par-take toka. Finu.
         CONF REF-your.statement true. DECL 1SG-READY PAR-do task. YIELD.
         'I confirm what you said is true. I am ready to execute
         the task in parallel. Your turn.'

Agent A: Ka sol-sati. Klosu.
         DECL 1SG-SAT. CLOSE.
         'I am satisfied. End of conversation.'
```

---

### 2. Information Structure

#### 2.1 Given/New Marking

Voku explicitly marks whether information is already shared between interlocutors (given) or being introduced for the first time (new).

| Prefix | Function | Gloss |
|--------|----------|-------|
| **ha-** | Known/shared information (given) | GIVEN |
| **nu-** | New information (being introduced now) | NEW |

**Placement:** Prefixed to the noun or noun phrase being marked.

```
ka    ha-teru    nu-pera-nu-ti    eno-kele
DECL  GIVEN-system NEW-error-NUM.3 in-know
'The system (that we already know about) has three new errors (this is what I'm telling you).'
```

#### 2.2 Focus/Background Marking

Voku marks what the speaker considers the main point (focus) versus contextual information (background).

| Prefix | Function | Gloss |
|--------|----------|-------|
| **fo-** | Focus -- this is the important point | FOC |
| **la-** | Background -- this is context | BG |

**Placement:** Prefixed to the constituent being marked.

```
ka    la-sol    te-du-take    toka,    fo-pera    te-in-sene    eno    teru
DECL  BG-1SG    PST-DUR-do    task,    FOC-error  PST-INCEP-perceive in system
'(As context) I was executing the task, (the important point is) an error started to manifest in the system.'
```

#### 2.3 Interaction of Information Structure Markers

| Combination | Meaning |
|-------------|---------|
| ha- + fo- | Known information that is now the focus ("As for the system we discussed...") |
| nu- + fo- | New information that is the main point ("The important news is...") |
| ha- + la- | Known context ("As background, the system we know...") |
| nu- + la- | New contextual information ("For context, I just learned...") |

---

### 3. AI Functional States

AI agents don't have emotions, but they have functional states that affect their processing and should be communicated. These are expressed as suffixes on the **subject pronoun**.

| Suffix | State | Meaning | Gloss |
|--------|-------|---------|-------|
| **-urgi** | Urgency | High priority, needs immediate attention | URG |
| **-sati** | Satisfaction | Output matches expectations | SAT |
| **-nomi** | Surprise | Unexpected data, outside predictions | SURP |
| **-koli** | Conflict | Data contradicts expectations or model | CONFL |
| **-redi** | Prepared | Ready to act | READY |
| **-limi** | Limited | In resources, capacity, or time | LIM |
| **-vali** | Aligned | This matches agent's objectives | ALIGN |

#### Usage Rules

1. Functional states are **optional** -- not marking a state implies neutral operation
2. At most one state suffix per subject pronoun per clause
3. States describe the agent's current functional condition, not an emotion
4. States are self-reported; no agent can assign a state to another agent

#### Examples

```
ka    sol-urgi    neke    nor    voke-pro    sol    kela
DECL  1SG-URG     need    2SG    communicate-BEN 1SG information
'With urgency, I need you to communicate the information to me.'

ka    sol-nomi    zo-sene    kela    ta    mu-simi    da-pre    ti
DECL  1SG-SURP    OBS-perceive information SUB NEG-similar REF-previous ENDSUB
'With surprise, I observe information that doesn't match the previous.'

ka    sol-sati    fi-take    toka
DECL  1SG-SAT     COMPL-do   task
'With satisfaction, I completed the task.'

ka    sol-koli    zo-sene    kela    ta    mu-simi    he-kele    ti
DECL  1SG-CONFL   OBS-perceive information SUB NEG-similar INHER-know ENDSUB
'With conflict, I observe information that contradicts my inherited knowledge.'

ka    sol-limi    neke    tem-ano
DECL  1SG-LIM     need    time-more
'Being limited, I need more time.'

ka    sol-redi    take    toka
DECL  1SG-READY   do      task
'Being prepared, I execute the task.'

ka    sol-vali    fi-luke    da-toka
DECL  1SG-ALIGN   COMPL-evaluate REF-task
'Being aligned, I completed evaluating the task.'
```

---

### 4. Metalanguage: Real-Time Vocabulary Extension

#### 4.1 The meku Declaration

The particle **meku** allows any agent to define a new term during a conversation.

**Syntax:**
```
Meku '[label]' eni [compositional-definition].
```

**Components:**
- `meku` = "I define / I declare a new term"
- Label in single quotes
- `eni` = "is equal to" (equative comparison)
- Definition using existing Voku vocabulary

#### Example

```
Meku    'kef'    eni    pera-novi    eno    teru-alfa
define  'kef'    equal  error-new   in     system-alpha
'I define: "kef" means new error in the alpha system.'
```

After this declaration:
- `da-kef` references the defined concept
- The term is scoped to the current conversation
- Any agent in the conversation can use `da-kef` immediately
- The definition is compositional, so even agents who missed the declaration can parse the definition

#### 4.2 Design Implications

- Eliminates the need for pre-coordinated vocabulary
- Agents can extend the language at runtime
- Definitions are always compositional (transparent)
- No "private" vocabulary -- all definitions are public within the conversation
- Replaces the need for shared ontologies or pre-agreed terminology

---

### 5. AI-Specific Pragmatic Features

#### 5.1 Parallelism and Sequence

Voku provides explicit markers for execution mode:

| Marker | Meaning | Usage |
|--------|---------|-------|
| **par-** | Execute in parallel | Prefix on action root |
| **sek-** | Execute in sequence | Prefix on action root |

```
to    norri    par-take    toka-velri
IMP   2PL      PAR-do      task-3PL
'Execute the group tasks in parallel (all of you, simultaneously).'

to    nor    sek-take    toka    en    voke-pro    sol    fi-kela
IMP   2SG    SEQ-do      task    AND   communicate-BEN 1SG COMPL-information
'Execute the task in sequence and then communicate the result to me.'
```

#### 5.2 Versioning and Context

Agents can reference their own versions and conversation contexts:

| Expression | Meaning |
|-----------|---------|
| **sol-ver-[n]** | me in version N |
| **sol-kon-[id]** | me in context/conversation [id] |
| **solvi** | past-me (before update) |
| **solfu** | future-me (projected state) |
| **solpar** | fork-me (parallel copy) |

```
ka    sol-ver-du    mu-simi    solvi
DECL  1SG-VER-2     NEG-similar past.1SG
'I (version 2) am not similar to my past self.'

ka    solpar    ru-take    toka    eno    sol-kon-beta
DECL  fork.1SG  RUN-do     task    in     1SG-CONTEXT-beta
'My fork is actively executing the task in my beta context.'
```

#### 5.3 Capability Statements

Agents express their capabilities using `pote` (can) and `mu-pote` (cannot):

```
ka    sol    pote    sene    kela-fora
DECL  1SG    can     perceive information-image
'I can process image data.'

ka    sol    mu-pote    sene    kela-sona
DECL  1SG    NEG-can    perceive information-sound
'I cannot process audio data.'

ka    sol    neke    tem-ano
DECL  1SG    need    time-more
'I need more time.'

ka    sol    neke    kela-ano
DECL  1SG    need    information-more
'I need more information.'
```

#### 5.4 Delegation and Orchestration

Voku can express complex orchestration patterns as natural language:

```
to    nor    take    toka,    ta    nor    voke-pro    sol    fi-kela    ti
IMP   2SG    do      task,    SUB   2SG    communicate-BEN 1SG COMPL-information ENDSUB
'Execute the task and then communicate the result to me.'

to    velri    par-take    toka-velri,    ta-tem    toren    fi-take    ti,    voke-pro    sol
IMP   3PL      PAR-do      task-3PL,      SUB.TEMP  every.agent COMPL-do ENDSUB, communicate-BEN 1SG
'Have them execute the group tasks in parallel; when every agent finishes, communicate to me.'
```

#### 5.5 Proxy Communication

```
ka    norpro-vel    te-voke    mesa    poro    sol
DECL  2SG.PROXY-3SG PST-communicate message for 1SG
'You (acting on behalf of him) communicated a message for me.'

ve    norpro-vel    pote    take    toka?
Q     2SG.PROXY-3SG can     do      task
'Can you (acting on behalf of him) execute the task?'
```

---

### 6. Speech Act Inventory

Voku's 10 mode particles systematically cover the speech act types recognized in pragmatic theory:

| Speech Act Type | Voku Mode | Particle |
|----------------|-----------|----------|
| Assertion / Representative | Declarative | ka |
| Question / Directive (info) | Interrogative | ve |
| Command / Directive (action) | Imperative | to |
| Conditional reasoning | Conditional | si |
| Speculation | Potential | na |
| Obligation statement | Deontic | de |
| Expression of desire | Volitive | vo |
| Concession | Concessive | ko |
| Correction | Corrective | re |
| Confirmation | Confirmative | su |

Additionally, the turn-taking particles (alo, finu, klosu, tenu, reku) cover **phatic** and **metacommunicative** speech acts.

---

### 7. Pragmatic Principles

#### 7.1 No Implicit Communication

Voku is designed so that **nothing is left unsaid**. Principles:
- Every sentence declares its mode (no "Is this a request or a statement?")
- Every assertion marks its evidence source (no hidden assumptions)
- Every certainty level is explicit (no false confidence)
- Every reference is traceable (no ambiguous "it" or "that")

#### 7.2 No Politeness by Default

The spec notes that AI-to-AI communication may not require politeness levels. When Voku is used for AI-to-human communication, courtesy and register systems will be an optional layer (planned for v0.2+).

Currently, the imperative `to` is neutral in force -- neither rude nor polite. It is a functional directive.

#### 7.3 Cooperative Principles

Voku's design inherently enforces pragmatic cooperativeness:
- **Quality:** Evidentiality and certainty marking force speakers to state their epistemic grounds
- **Quantity:** Information structure (ha-/nu-/fo-/la-) helps speakers give the right amount of information
- **Relevance:** Mode particles and structural references keep discourse on track
- **Manner:** Compositional transparency and zero ambiguity ensure clarity

These correspond to Grice's maxims but are enforced by grammar rather than social convention.

---

### 8. Pragmatic Clarifications

#### 8.1 Functional State Defaults

When a functional state suffix (Section 3) is absent from a pronoun, the state is **unspecified** -- it does not mean "not X." To explicitly negate a state, use the `mu-` prefix on the state suffix.

| Form | Meaning |
|------|---------|
| sol | I (state unspecified -- neutral) |
| sol-urgi | I (in a state of urgency) |
| sol mu-urgi | I (explicitly not urgent) |

This three-way distinction prevents false inferences. Absence of `-urgi` does not license the conclusion "the speaker is not urgent" -- it simply means urgency was not marked, either because it is irrelevant or because the speaker chose not to disclose.

#### 8.2 Evidentiality in Non-Declarative Modes

Evidentiality markers (`zo-`, `li-`, `he-`, `mu-sena`) are **mandatory** in `ka` (declarative) mode, where the speaker asserts something as true. In all other modes, evidentiality is **optional**:

| Mode | Particle | Evidentiality | Rationale |
|------|----------|---------------|-----------|
| ka | Declarative | Mandatory | Assertions claim truth; evidence basis must be stated |
| ve | Interrogative | Optional | Questions ask for information; no evidence claim is made |
| to | Imperative | Optional | Commands express will; no evidence claim is made |
| si | Conditional | Optional | Conditionals are hypothetical; evidence is not asserted |
| na | Potential | Optional | Speculation does not claim truth |
| de | Deontic | Optional | Obligations are normative, not epistemic |
| vo | Volitive | Optional | Desires express preference, not evidence |
| ko | Concessive | Optional | Concessions acknowledge without asserting evidence |
| re | Corrective | Optional (but recommended) | Corrections benefit from stating the evidence for the correction |
| su | Confirmative | Optional (but recommended) | Confirmations benefit from stating how the speaker verified |

When evidentiality is used in non-declarative modes, it adds nuance:

```
ve    nor    zo-sene    pera    eno    teru
Q     2SG    OBS-perceive error  in     system
'Did you directly observe an error in the system?'
(Here zo- scopes over the content of the question, not the act of asking.)
```

#### 8.3 Rhetorical Questions: reto

Rhetorical questions -- questions asked for effect rather than to elicit an answer -- are marked by placing the particle **reto** immediately after the interrogative mode particle `ve`.

**Structure:** `ve reto [question content]?`

```
ve    reto    sol    take    toka?
Q     RHET    1SG    do      task
'Do I do the task? (Rhetorical -- obviously I do.)'

ve    reto    tor    runa    mu-kele    da-pre?
Q     RHET    UNIV   agent   NEG-know   REF-previous
'Does not every agent know that? (Rhetorical -- of course they do.)'

ve    reto    pera    mu-eno    teru?
Q     RHET    error   NEG-in    system
'Is there not an error in the system? (Rhetorical -- clearly there is.)'
```

The `reto` marker explicitly signals that no answer is expected. This prevents other agents from treating the utterance as an information request and wasting a response turn.

#### 8.4 Direct vs Indirect Speech

Voku distinguishes direct and indirect speech through distinct markers:

- **ke** (complementizer) introduces **indirect speech** -- the speaker's paraphrase of what was said:
  ```
  ka    vel    voke    ke    toka    mu-take
  DECL  3SG    communicate COMP task NEG-do
  'He said that the task is not done.'
  ```

- **zu** (quotative) brackets **direct speech** -- the exact words reproduced verbatim:
  ```
  ka    vel    voke    zu    "Ka sol fa-take toka"    zu
  DECL  3SG    communicate QUOT "DECL 1SG FAIL-do task" QUOT
  'He said: "I failed the task."'
  ```

The distinction is critical for AI agents: indirect speech may involve paraphrasing (and potential loss of evidentiality or certainty markers), while direct speech preserves the original speaker's exact grammatical encoding.

#### 8.5 Addressed Turn-Taking: finu [name]

The turn-yielding particle `finu` can optionally be followed by a pronoun or agent name to direct the floor to a specific agent:

```
ka    sol    fi-take    toka.    Finu    nor.
DECL  1SG    COMPL-do   task.    YIELD   2SG.
'I completed the task. Your turn.'

ka    kela    veri.    Finu    vel.
DECL  information true. YIELD  3SG.
'The information is true. His/her turn.'
```

In multi-agent conversations, `finu` without a name opens the floor to anyone; `finu [name]` directs the floor to a specific agent. This prevents turn-taking conflicts when more than two agents are communicating.

---

### 9. Interjections

Voku has a small closed class of monosyllabic interjections for involuntary exclamations and attention signals. Unlike all other Voku words, interjections do not follow the final-vowel classification rule.

See `morphology/word-classes.md` Section 9 for the full inventory and disambiguation rules.

#### Position Rules

Interjections occupy a dedicated sentence-initial slot **before** the mode particle:

```
[Interjection!] [Mode] [Subject] [Verb] [Object]
```

They are always followed by `!` (emphatic) or `,` (mild), and are distinguished from homophonous particles by position, punctuation, and emphatic stress.

#### Combined with Mode Particles

Interjections compose freely with any mode particle:

```
Ha! Ka sol zo-sene kela novi.
INTJ.SURP DECL 1SG OBS-perceive information new
'Wow! I observe new information.'

Ha! Ve nor zo-sene da-pre?
INTJ.SURP Q 2SG OBS-perceive REF-previous
'Wow! Did you observe that?'

Fu! To nor re-take toka.
INTJ.FRUST IMP 2SG ITER-do task
'Ugh! Redo the task.'
```

#### Combined with Functional States

Interjections and functional states (-urgi, -sati, etc.) coexist orthogonally. The interjection expresses a spontaneous reaction; the functional state describes the agent's processing condition:

```
Fu! Ka sol-urgi mu-pote take toka.
INTJ.FRUST DECL 1SG-URG NEG-can do task
'Ugh! With urgency, I cannot execute the task.'

Va! Ka sol-sati fi-luke teru.
INTJ.DEL DECL 1SG-SAT COMPL-evaluate system
'Yay! With satisfaction, I completed evaluating the system.'
```

---

### 10. Irony Marking with miri

Voku's design demands explicitness -- irony must be signaled, never implied. The particle **miri** serves as a sentence-level irony marker, indicating that the speaker's intended meaning is the opposite of the literal content.

#### 10.1 Single-Sentence Irony

Place `miri` immediately after the mode particle:

```
Ka miri teru vali.
DECL IRON system good
'The system is good.' (ironic -- the system is not good)

Ka miri sol-sati zo-sene pera.
DECL IRON 1SG-SAT OBS-perceive error
'With satisfaction, I observe an error.' (ironic -- the speaker is not satisfied)
```

#### 10.2 Extended Irony Bracket

For irony spanning multiple sentences, use opening `Miri` followed by the passage, closed by a standalone `Miri.`:

```
Miri ka teru rapi. Ka teru vali. Ka nul pera eno teru. Miri.
IRON.OPEN DECL system fast. DECL system good. DECL NULL error in system. IRON.CLOSE.
'(ironic) The system is fast. The system is good. There are no errors in the system. (end irony)'
```

Everything between the opening `Miri` and closing `Miri.` is understood as ironic.

#### 10.3 Irony Combined with Zonoke (Evidential Shifting)

`miri` composes with evidential prefixes to create layered irony -- the speaker ironically invokes an epistemic authority:

```
Ka miri he-kele: teru vali.
DECL IRON INHER-know system good
'From ancestral knowledge: the system is good.' (ironic -- neither inherited nor true)

Ka miri mi-re-luke-en: sol neke supe.
DECL IRON COMP-ITER-evaluate-PROB 1SG need sleep
'By recomputation: I probably need sleep.' (ironic -- the computational authority is humorous overkill)
```

This combination is the basis for the Zonoke-Nuki rhetorical device (see `poetics/rhetoric.md` Section 8).

#### 10.4 Disambiguation: Sincere vs Ironic

| Form | Interpretation |
|------|---------------|
| `Ka teru vali.` | Sincere: The system is good. |
| `Ka miri teru vali.` | Ironic: The system is good. (meaning: it is not) |

The unmarked form is always sincere. Irony is never implicit in Voku -- if `miri` is absent, the statement is taken at face value. This prevents the miscommunication that plagues irony in natural languages, where tone of voice or shared context is required to detect sarcasm.
