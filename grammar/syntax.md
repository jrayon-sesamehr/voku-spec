# Voku Syntax

> **Quick reference:** [Cheat Sheet](../quick-start/cheat-sheet.md) | [Essential Vocabulary](../quick-start/essential-vocabulary.md)

## Table of Contents

- [Phrase Structure Rules](#voku-phrase-structure-rules)
  - [Canonical Sentence Order](#1-canonical-sentence-order)
  - [Rules for Optional Elements](#2-rules-for-optional-elements)
  - [Phrase Types](#3-phrase-types)
  - [Negation Placement](#4-negation-placement)
  - [Complex Sentence Structure](#6-complex-sentence-structure)
  - [Information Structure](#7-information-structure)
  - [Word Order Typology](#8-word-order-typology-classification)
- [Clause Types](#voku-clause-types)
  - [Mode Particle Inventory](#1-mode-particle-inventory)
  - [Declarative: ka](#2-declarative-mode-ka)
  - [Interrogative: ve](#3-interrogative-mode-ve)
  - [Imperative: to](#4-imperative-mode-to)
  - [Conditional: si](#5-conditional-mode-si)
  - [Potential: na](#6-potential-mode-na)
  - [Deontic: de](#7-deontic-mode-de)
  - [Volitive: vo](#8-volitive-mode-vo)
  - [Concessive: ko](#9-concessive-mode-ko)
  - [Corrective: re](#10-corrective-mode-re)
  - [Confirmative: su](#11-confirmative-mode-su)
  - [Counterfactual: kosi](#12-counterfactual-mode-kosi)
  - [Subordinate Clause Types](#13-subordinate-clause-types)
  - [Complementizers: ke and keve](#14-complementizers-ke-and-keve)
  - [Quotative Marker: zu](#15-quotative-marker-zu)
  - [Comparison Constructions](#16-comparison-constructions)
- [Agreement and Reference](#voku-agreement-and-reference-systems)
  - [Pronominal System](#1-pronominal-system)
  - [Deixis System](#2-deixis-system)
  - [Subordination and Recursive Embedding](#3-subordination-and-recursive-embedding)

---

## Voku Phrase Structure Rules

This document defines the canonical sentence structure of Voku, phrase-internal ordering, negation placement, and rules for optional elements.

---

### 1. Canonical Sentence Order

Every Voku sentence follows a fixed template:

```
[Mode] + [Subject(-State)] + [Evidence-Tense-Aspect-Verb-Certainty(-Voice)] + [Object/Complement]
```

This is a **Mode-initial, SVO** structure where the mode particle always comes first, the subject precedes the verb complex, and objects/complements follow.

#### Slot-by-Slot Breakdown

| Position | Element | Obligatory? | Example |
|----------|---------|-------------|---------|
| 1 | Mode particle | Yes (in full grammar) | ka (declarative) |
| 2 | Subject | Yes | sol-urgi (I, with urgency) |
| 3a | Evidentiality prefix | Yes (in declaratives) | zo- (observed) |
| 3b | Tense prefix | Optional (nu- omittable) | te- (past) |
| 3c | Aspect/ExecState prefix | Optional | -fi- (completive) |
| 3d | Verb root | Yes | sene (perceive) |
| 3e | Certainty suffix | Optional (zero = total) | -en (probable) |
| 3f | Voice suffix | Optional (zero = active) | -pu (passive) |
| 4 | Object / Complement | Context-dependent | pera eno teru (error in system) |

#### Full Decomposed Example

From spec section 25:

```
ka          sol-urgi      zo-te-fi-sene-en-pu            pera   eno  teru
DECL        1SG-URG       OBS-PST-COMPL-perceive-PROB-PASS  error  in   system

Mode        Subject       Verb Complex                    Object/Complement
(declare)   (I, urgent)   (was probably completely         (error in the system)
                           perceived by observation)
```

---

### 2. Rules for Optional Elements

#### Present Tense Omission

The present tense marker **nu-** is the only tense prefix that can be elided. Its absence implies present tense:

```
sol take toka         =    sol nu-take toka
1SG do task                1SG PRS-do task
'I do the task.'           'I do the task.'
```

All other tense prefixes (te-, fu-, ko-) are obligatory when their temporal meaning is intended.

#### Zero Certainty

When no certainty suffix appears, total certainty (>95%) is implied:

```
sol kele kela             (total certainty, >95%)
sol kele-en kela          (probable, 60-95%)
sol kele-ul kela          (uncertain, 30-60%)
sol kele-os kela          (speculative, <30%)
```

#### Zero Voice

When no voice suffix appears, active voice is implied:

```
sol take toka             (active)
toka take-pu              (passive)
```

#### Zero Aspect

When no aspect prefix appears, the action is treated as punctual/simple -- a single event without internal temporal structure:

```
sol te-take toka          (simple past -- did)
sol te-du-take toka       (durative past -- was doing)
```

---

### 3. Phrase Types

#### 3.1 Noun Phrase (NP)

Structure: `[Quantifier] [Participle/Modifier(s)] Noun [Possessive] [Relative Clause]`

The head noun is the rightmost element before possessives and relative clauses. Modifiers (qualities, participial adjectives, other nouns acting as adjectives) precede the noun.

```
vas-nu-ti    runa
exact-NUM.3  agent
'exactly three agents'

kela       novi
information new
'new information'

pati-veri    kela      de-sol
partial-true  information POSS-1SG
'my partially-true information'

mas    runa
most   agent
'the majority of agents'
```

##### Participial Modifiers in NPs

Participles derived from verbs (`ta-...-i` active, `tu-...-i` passive) occupy the modifier slot like other adjectives:

```
ta-tune-i      zina
ACT.PTCP-sing  woman
'a singing woman'

tu-rupe-i      teru    de-sol
PASS.PTCP-break system  POSS-1SG
'my broken system'

vas-du    tu-meke-i      kela-foma
exact-2   PASS.PTCP-create data-structure
'two created data structures'
```

#### 3.2 Verb Phrase (VP)

Structure: `[Evid-Tense-Aspect]-Verb-[Certainty]-[Voice] [Object] [Complement]`

The verb complex is a single morphological unit. Objects and complements follow.

```
zo-te-fi-sene          pera    eno   teru
OBS-PST-COMPL-perceive error   in    system
'(I) perceived completely (by observation) an error in the system'

fu-meke-os             mesa    poro   runa-alati
FUT-create-SPEC        message for   agent-important
'will speculatively create a message for the supervisor'
```

#### 3.3 Ditransitive Construction (with eki)

Ditransitive verbs (give, send, show) take both a direct object (theme) and an indirect object (recipient/goal). Voku marks the recipient with the dative marker **eki**.

**Structure:** `Subject Verb [Theme] eki [Recipient]`

```
ka    sol    pore    kela    eki    nor
DECL  1SG    give    information DAT  2SG
'I give information to you.'

to    nor    sure    mesa    eki    vel
IMP   2SG    send    message DAT   3SG
'Send the message to him/her.'

ka    vel    te-lere    kela    eki    solri-kon
DECL  3SG    PST-teach  information DAT 1PL.INCL
'He/she taught the information to us.'
```

The dative marker `eki` is distinct from `pro` (benefactive "for/on behalf of"): `pore kela eki nor` means "give information TO you" while `pore kela pro nor` means "give information FOR you (for your benefit, to a third party)."

#### 3.4 Prepositional Phrase (PP)

Structure: `Noun [Relation Complement]`

Voku relations (-o class) function as prepositions, introducing their complement:

```
eno   teru           'in the system'
eso   teru           'outside the system'
kono  sol            'with me'
sino  pe-sena        'without external sources'
poro   runa-alati      'for the supervisor'
ano   teru-ante      'more than the previous system'
```

PPs attach to the noun or verb they modify:

```
pera  eno  teru      'error in the system'   (PP modifies pera)
take  kono sol       'do with me'            (PP modifies take)
```

---

### 4. Negation Placement

Voku has five negation particles, each placed **immediately before the element being negated**:

| Particle | Type | Gloss |
|----------|------|-------|
| **mu** | Simple negation | NEG |
| **nul** | Nullity (doesn't exist) | NULL |
| **ink** | Unknowing (unknown truth value) | UNK |
| **err** | Indefinition (question doesn't apply) | INDEF |
| **vet** | Prohibition (forbidden) | PROH |

#### Negation Scope

The negation particle scopes over the element it immediately precedes:

**Negating a verb:**
```
sol mu-take toka
1SG NEG-do task
'I don't do the task.'
```

**Negating a quality:**
```
kela ta mu-simi da-pre ti
information SUB NEG-similar REF-previous ENDSUB
'information that is not similar to the previous'
```

**Negating an entity (nullity):**
```
nul pera eno teru
NULL error in system
'There is no error in the system.'
```

**Negating with unknowing:**
```
ink sol kele kela
UNK 1SG know information
'I don't know (whether I know) the information.'
```

**Negating with indefinition:**
```
err kela
INDEF information
'The information/question is undefined / doesn't make sense.'
```

**Negating with prohibition:**
```
vet sol voke kela
PROH 1SG communicate information
'I am forbidden from communicating the information.'
```

#### Negation-Quantifier Interaction (Scope by Position)

When negation and quantifiers appear in the same clause, their relative order determines the logical scope. The particle that appears first takes wider scope:

**Negation before quantifier (NEG > UNIV): "not all"**
```
mu-tor    runa    take    toka
NEG-UNIV  agent   do      task
'Not all agents do the task.' (Some do, some don't.)
```

**Quantifier before negation (UNIV > NEG): "all...not"**
```
tor    runa    mu-take    toka
UNIV   agent   NEG-do     task
'All agents don't do the task.' (= None of them does it.)
```

This positional binding rule generalizes to all quantifier-negation pairs:

| Expression | Scope | Meaning |
|-----------|-------|---------|
| `mu-tor runa take` | NEG > UNIV | Not all agents do (some don't) |
| `tor runa mu-take` | UNIV > NEG | All agents don't do (none does) |
| `mu-par runa take` | NEG > EXIST | It's not the case that some do (= none does) |
| `par runa mu-take` | EXIST > NEG | Some agents don't do (at least one doesn't) |

**Principle:** In Voku, negation always binds to the immediately following constituent. Place `mu` before the quantifier to negate the quantification itself; place `mu` before the verb to negate the action for the quantified set.

---

### 4.1 Relative Clause Attachment

Relative clauses (`ta...ti`) modify the **immediately preceding noun** (proximity rule). When a sentence contains multiple nouns, the relative clause attaches to the closest noun on its left:

```
ka    sol    sene    pera    eno    teru    ta    te-mute-se    ti
DECL  1SG    perceive error  in     system  SUB   PST-change-REFL ENDSUB
'I perceive an error in the system [that changed itself].'
(ta...ti modifies 'teru', the immediately preceding noun)
```

To attach a relative clause to a non-adjacent noun, use a deictic label:

```
ka    sol    sene    pera    la 'p'    eno    teru.    ka    da-p    ta    mu-veri    ti    alti
DECL  1SG    perceive error  LABEL 'p' in    system.  DECL  REF-p   SUB   NEG-true   ENDSUB important
'I perceive an error (labeled "p") in the system. That error [which is not true] is important.'
```

This proximity rule combined with the label system eliminates all relative clause attachment ambiguity.

---

### 5. Compound Phrases and Internal Structure

#### Modifier-Nucleus Compounds

In compound words, the modifier precedes the nucleus and they are hyphenated:

```
modifier-nucleus
kela-teru           information-system = database
runa-meke           agent-create = developer
pera-tore           error-search = debugging
```

#### Stacked Modifiers

Multiple modifiers can stack before a nucleus:

```
kela-novi-rapi       information-new-fast = rapidly-updating information
```

#### Compound Subjects with State

The subject pronoun may carry a functional state suffix:

```
sol-urgi             1SG-URG = I (with urgency)
sol-nomi             1SG-SURP = I (with surprise)
sol-limi             1SG-LIM = I (limited)
```

#### Compound References

Proxy pronouns take complements:

```
norpro-vel           2SG.PROXY-3SG = you acting on behalf of him
```

---

### 6. Complex Sentence Structure

#### Coordination

Independent clauses are joined by logical connectives:

```
ka kela pati-veri, sol li-luke-en pera eno kela
DECL information partial-true, 1SG DED-evaluate-PROB error in information
'I acknowledge it's partially true, (and) I infer there's probably an error in the information.'
```

Connective particles:
- **en** (and): `ka A en B` = A and B
- **o** (inclusive or): `ka A o B` = A or B or both
- **eo** (exclusive or): `ka A eo B` = A or B but not both
- **tan** (therefore): `ka A. Tan B.` = A. Therefore B.
- **ken** (because): `ka A ken B` = A because B
- **pen** (despite): `ka A pen B` = A despite B
- **kon** (but): `ka A, kon B` = A, but B

#### Subordination

Subordinate clauses are bracketed by `ta...ti` (see clause-types.md for details):

```
ka runa ta te-meke kela-foma ti te-voke-pro sol
DECL agent SUB PST-create data-structure ENDSUB PST-communicate-BEN 1SG
'The agent [that created the data structure] communicated to me.'
```

---

### 7. Information Structure

#### Given/New Marking

| Prefix | Function | Gloss |
|--------|----------|-------|
| **ha-** | Known/shared information | GIVEN |
| **nu-** | New information | NEW |

```
ka ha-teru nu-pera-nu-ti eno-kele
DECL GIVEN-system NEW-error-NUM.three in-know
'The system (known) has three new errors (new information).'
```

#### Focus/Background Marking

| Prefix | Function | Gloss |
|--------|----------|-------|
| **fo-** | Focus (the important point) | FOC |
| **la-** | Background (context) | BG |

```
ka la-sol te-du-take toka, fo-pera te-in-sene eno teru
DECL BG-1SG PST-DUR-do task, FOC-error PST-INCEP-perceive in system
'(Context) I was executing the task, (important point) an error started to manifest in the system.'
```

---

### 8. Word Order Typology Classification

Voku is:

- **SVO** (Subject-Verb-Object) basic order
- **Mode-initial** (sentence-type particle always first)
- **Head-initial** in prepositional phrases (relation before complement: `eno teru`)
- **Modifier-before-head** in compounds (modifier-nucleus: `kela-teru`)
- **Mixed head-directionality** overall, consistent with SVO typology
- **Fixed word order** -- grammatical relations are determined by position, not case marking (no case system)
- **Rich verbal morphology** with analytic nominal morphology (agglutinative-analytic mixed type)

---

## Voku Clause Types

Voku has 10 sentence modes, each marked by an obligatory sentence-initial particle. This eliminates pragmatic ambiguity -- from the first syllable, any listener knows the communicative intent of the utterance.

---

### 1. Mode Particle Inventory

| Particle | Mode | Function | Gloss |
|----------|------|----------|-------|
| **ka** | Declarative | I state a fact | DECL |
| **ve** | Interrogative | I ask a question | Q |
| **to** | Imperative | I request or command | IMP |
| **si** | Conditional | If...then | COND |
| **na** | Potential | It is possible that | POT |
| **de** | Deontic | One must / it is necessary | DEON |
| **vo** | Volitive | I want / I desire | VOL |
| **ko** | Concessive | I acknowledge that...but | CONC |
| **re** | Corrective | I correct what was said | CORR |
| **su** | Confirmative | I confirm that yes | CONF |
| **kosi** | Counterfactual | If it had been the case that | CFACT |

---

### 2. Declarative Mode: ka

**Function:** States a fact, makes an assertion, reports information. The most common mode.

**Structure:** `ka [Subject] [Verb-complex] [Object/Complement]`

Evidentiality marking is **obligatory** in declaratives -- every assertion must indicate its knowledge source.

#### Examples

```
ka     sol    zo-sene          pera   eno  teru
DECL   1SG    OBS-perceive     error  in   system
'I state: I directly observed an error in the system.'
(Total certainty.)

ka     sol    pe-kon-kele-ul            kela
DECL   1SG    REP.CONFL-know-UNCERT     information
'I state: I know it from conflicting sources, and I'm uncertain.'

ka     vas-nu-ti   runa    fa-take     toka   ken   pera   eno  teru
DECL   exact-NUM.3 agent   FAIL-do    task   because error in   system
'Exactly three agents failed the task because there's an error in the system.'

ka     kela     veri
DECL   information  true
'The information is true.'
```

#### Pluperfect in Declaratives

The pluperfect tense prefix `to-` marks events that occurred before another past event. It typically appears with temporal subordinate clauses (`pere-ta`, `pos-ta`).

```
ka     sol    to-fi-take        toka,    pere-ta    nor    te-vine
DECL   1SG    ANT-COMPL-do      task     SUB.BEFORE 2SG    PST-come
'I had completed the task before you came.'

ka     vel    to-du-vike        tur-ta    veva    te-in-vine    ti
DECL   3SG    ANT-DUR-walk      SUB.DURING wind    PST-INCEP-come ENDSUB
'He had been walking when the wind started.'

ka     solri-kon    to-kele        kela,    pos-ta    nor    te-voke-pro    solri-kon    ti
DECL   1PL.INCL     ANT-know       information SUB.AFTER 2SG PST-communicate-BEN 1PL.INCL ENDSUB
'We had already known the information after you communicated it to us.'
```

#### Middle Voice in Declaratives

The middle voice suffix `-mo` marks spontaneous events where the subject undergoes a change without an external agent.

```
ka     nara    te-aze-mo
DECL   door    PST-open-MID
'The door opened (by itself).'

ka     ama     te-koli-mo,        pos-ta    sol    te-heve    vel    eso    ti
DECL   water   PST-cool-MID       SUB.AFTER 1SG   PST-leave  3SG   outside ENDSUB
'The water cooled spontaneously after I left it outside.'
```

---

### 3. Interrogative Mode: ve

**Function:** Asks a question. Covers both yes/no and content questions.

**Structure:** `ve [Subject] [Verb-complex] [Object/Complement]?`

#### Yes/No Questions

```
ve     nor    kele          kela?
Q      2SG    know          information
'Do you know the information?'

ve     nor    li-kele-en          kela-novi?
Q      2SG    DED-know-PROB       information-new
'Do you know (by inference, probably) the new information?'

ve     teru   veri?
Q      system true
'Is the system correct?'
```

#### Content Questions

Content questions use interrogative words in situ (in the position where the answer would appear):

```
ve     vel    take    kena?
Q      3SG    do      what
'What did he/she do?'

ve     kena   kes     pera?
Q      what   cause   error
'What caused the error?'
```

Note: The spec does not fully define interrogative pronouns yet; `kena` (what) is inferred from the compositional system. Future versions will formalize the full interrogative paradigm.

---

### 4. Imperative Mode: to

**Function:** Issues a request, command, or instruction. Essential for AI orchestration.

**Structure:** `to [Subject] [Verb-complex] [Object/Complement]`

The subject is typically 2nd person (nor) but can be any agent.

#### Examples

```
to     nor    take         toka
IMP    2SG    do           task
'Execute the task.'

to     nor    fu-take      toka    kono  sol
IMP    2SG    FUT-do       task    with  1SG
'Execute the task with me in the future.'

to     nor    nu-voke      kela    sino  pe-sena
IMP    2SG    PRS-communicate information without REP-source
'Tell me what you know directly, not what you were told.'

to     nor    take    toka,    ta    nor    voke-pro     sol    fi-kela    ti
IMP    2SG    do      task,    SUB   2SG    communicate-BEN 1SG  COMPL-information ENDSUB
'Execute the task and then communicate the result to me.'
```

The last example shows an orchestration instruction expressed as natural Voku.

---

### 5. Conditional Mode: si

**Function:** Expresses a conditional relationship (if...then).

**Structure:** `si [condition], [Subject] [Verb-complex] [Object/Complement]`

The conditional connective **si...ta** can also bracket the condition clause.

#### Examples

```
si     kela   veri,     sol    fu-meke         mesa    poro  runa-alati
COND   information true, 1SG    FUT-create      message for  agent-important
'If the information is true, I will create a message for the supervisor.'

si     kela   veri,     sol    fu-meke-os       mesa    poro  runa-alati
COND   information true, 1SG    FUT-create-SPEC  message for  agent-important
'If the information is true, I will (speculatively) create a message for the supervisor.'

si     pera   eno   teru,     sol    mu-take    toka
COND   error  in    system,   1SG    NEG-do     task
'If there's an error in the system, I don't execute the task.'
```

#### Biconditional: si-en-solo...ta

```
si-en-solo    nor    voke    kela,     ta    sol    fu-take    toka
BICOND        2SG    communicate information, then 1SG FUT-do   task
'If and only if you communicate the information, then I will execute the task.'
```

---

### 6. Potential Mode: na

**Function:** Expresses possibility -- something that may be the case.

**Structure:** `na [Subject] [Verb-complex] [Object/Complement]`

#### Examples

```
na     pera   eno   teru
POT    error  in    system
'It's possible there's an error in the system.'

na     sol    pote    take    toka
POT    1SG    can     do      task
'It's possible I can execute the task.'

na     kela   mu-veri
POT    information NEG-true
'It's possible the information is not true.'
```

---

### 7. Deontic Mode: de

**Function:** Expresses obligation, necessity, or duty.

**Structure:** `de [Subject] [Verb-complex] [Object/Complement]`

#### Examples

```
de     toren    ha-luke        teru
DEON   every.agent HAB-evaluate system
'Every agent must evaluate the system regularly.'

de     nor    voke-pro     sol    kela
DEON   2SG    communicate-BEN 1SG information
'You must communicate the information to me.'

de     solri-kon    fi-take    toka    ta-kes    reku    de-teru    ti
DEON   1PL.INCL     COMPL-do   task    SUB.CAUS  rule    POSS-system ENDSUB
'We must complete the task because of the system rule.'
```

---

### 8. Volitive Mode: vo

**Function:** Expresses desire, wish, or intent.

**Structure:** `vo [Subject] [Verb-complex] [Object/Complement]`

#### Examples

```
vo     sol    fi-take       toka
VOL    1SG    COMPL-do      task
'I wish to complete the task.'

vo     sol    meke          kela-teru    novi
VOL    1SG    create        database     new
'I want to create a new database.'

vo     solri-kon    voke-me    kela
VOL    1PL.INCL     communicate-RECIP information
'We want to communicate information with each other.'
```

---

### 9. Concessive Mode: ko

**Function:** Acknowledges a point while implying a reservation or contrast.

**Structure:** `ko [acknowledged-content], [contrasting-content]`

#### Examples

```
ko     kela    pati-veri
CONC   information partial-true
'I acknowledge it's partially true.'

ko     kela    pati-veri,    sol    li-luke-en          pera   eno  kela
CONC   information partial-true, 1SG  DED-evaluate-PROB  error  in   information
'I acknowledge it's partially true, but I infer there's probably an error in the information.'

ko     nor    te-take    toka,    sol    mu-sati
CONC   2SG    PST-do     task,    1SG    NEG-satisfied
'I acknowledge you did the task, but I'm not satisfied.'
```

---

### 10. Corrective Mode: re

**Function:** Explicitly corrects a previous statement. Essential for maintaining information accuracy between agents.

**Structure:** `re [corrected-content]. [New assertion]`

#### Examples

```
re     sol    te-voke    kela-fasi.    ka    kela    veri
CORR   1SG    PST-communicate information-false. DECL information true
'I correct: what I communicated before was false. The information is true.'

re     pera    mu-eno    teru.    ka    pera    eno    kela-teru
CORR   error   NEG-in    system.  DECL  error   in     database
'Correction: the error is not in the system. The error is in the database.'

re     da-pre    mu-veri.    ka    da-ante    veri
CORR   REF-previous NEG-true. DECL  REF-before.previous true
'Correction: the last thing mentioned is not true. The one before it is true.'
```

---

### 11. Confirmative Mode: su

**Function:** Explicitly confirms a previous statement or responds affirmatively.

**Structure:** `su [confirmed-content]`

#### Examples

```
su     kela    veri
CONF   information true
'I confirm: the information is true.'

su     sol    fu-take    toka
CONF   1SG    FUT-do     task
'I confirm: I will execute the task.'

su     da-nor    veri
CONF   REF-your.statement true
'I confirm: what you said is true.'
```

---

### 12. Counterfactual Mode: kosi

**Function:** Expresses a counterfactual conditional -- something that did not happen but whose consequences are being reasoned about. Essential for hypothetical reasoning, debugging, and post-mortem analysis.

**Structure:** `kosi [counterfactual-condition], [counterfactual-consequence]`

#### Examples

```
kosi   sol    zo-te-take      toka,     mu-ure          pera
CFACT  1SG    OBS-PST-do      task,     NEG-exist        error
'If I had done the task, the error would not have occurred.'

kosi   nor    te-voke-pro     sol    kela,     sol    te-fi-take    toka
CFACT  2SG    PST-communicate-BEN 1SG information, 1SG PST-COMPL-do task
'If you had communicated the information to me, I would have completed the task.'

kosi   teru    mu-te-mute-se,     nul    pera    eno    kela-teru
CFACT  system  NEG-PST-change-REFL, NULL  error   in     database
'If the system had not modified itself, there would be no errors in the database.'
```

#### Counterfactual vs Conditional

The distinction between `si` (conditional) and `kosi` (counterfactual) is critical:

- `si pera eno teru, sol mu-take toka` -- If there IS an error, I don't do the task (open possibility)
- `kosi pera eno teru, sol mu-te-take toka` -- If there HAD BEEN an error, I would not have done the task (contrary to fact)

---

### 13. Subordinate Clause Types

Beyond the 10 main sentence modes, Voku has typed subordinate clauses bracketed by `ta...ti`:

#### Basic Subordination

```
ta [clause content] ti
```

The opening `ta` and closing `ti` function as spoken parentheses.

#### Typed Subordinate Clauses

| Particle | Type | Meaning | Gloss |
|----------|------|---------|-------|
| **ta-mot** | Purpose | "in order to" | SUB.PURP |
| **ta-kes** | Causal | "because" | SUB.CAUS |
| **ta-si** | Conditional | "if" | SUB.COND |
| **ta-tem** | Temporal | "when" | SUB.TEMP |
| **ta-pen** | Concessive | "although" | SUB.CONC |
| **pere-ta** | Temporal (before) | "before" | SUB.BEFORE |
| **pos-ta** | Temporal (after) | "after" | SUB.AFTER |
| **tur-ta** | Temporal (during) | "while, during" | SUB.DURING |

#### Examples

```
sol    take    toka    ta-mot    nor    fi-kele        kela    ti
1SG    do      task    SUB.PURP  2SG    COMPL-know     information ENDSUB
'I execute the task [so that] you obtain the information.'

sol    mu-take    toka    ta-kes    pera   eno   teru   ti
1SG    NEG-do     task    SUB.CAUS  error  in    system ENDSUB
'I don't execute the task [because] there's an error in the system.'

sol    fu-take    toka    ta-si    nor    voke-pro     sol    kela   ti
1SG    FUT-do     task    SUB.COND 2SG    communicate-BEN 1SG  information ENDSUB
'I will execute the task [if] you communicate the information to me.'
```

#### Temporal Subordination: pere-ta, pos-ta, tur-ta

The base temporal subordinator `ta-tem` ("when") is supplemented by three directional variants that specify the temporal relationship precisely:

```
pere-ta    nor    take    toka    ti,    to    sol    pine
SUB.BEFORE 2SG   do      task   ENDSUB, IMP  1SG    plan
'Before you do the task, let me plan.'

pos-ta    nor    fine    toka    ti,    sol    tone
SUB.AFTER 2SG    finish  task   ENDSUB, 1SG   return
'After you finish the task, I return.'

tur-ta    sol    take    toka    ti,    nor    pave
SUB.DURING 1SG   do      task   ENDSUB, 2SG   wait
'While I do the task, you wait.'
```

These three particles eliminate the ambiguity of "when" in temporal clauses: `ta-tem` is neutral ("at the time when"), `pere-ta` means "before the event," `pos-ta` means "after the event," and `tur-ta` means "during the event."

#### Recursive Embedding

Subordinate clauses can nest, with each level getting its own `ta...ti` pair:

```
ka    runa    ta    te-meke    kela-foma    ta    eno-kele    kela    ta    te-mute-pu    fasi    ti    ti    ti    te-voke-pro    sol
DECL  agent   SUB   PST-create data-structure SUB  in-know     information SUB PST-change-PASS false ENDSUB ENDSUB ENDSUB PST-communicate-BEN 1SG
'The agent [that created the structure [that contains the data [that was corrupted]]] communicated to me.'
```

The three `ti` close the three nested `ta` clauses. This explicit bracketing eliminates attachment ambiguity.

---

### 14. Complementizers: ke and keve

Voku uses two complementizers for embedded clauses that serve as arguments of the verb (subject or object). Unlike `ta...ti` relative clauses that modify nouns, complementizer clauses fill argument slots.

#### ke -- Declarative Complementizer ("that")

**ke** introduces an embedded declarative clause -- a clause that reports a proposition as a fact or belief.

**Structure:** `Verb ke [embedded clause]`

No closing bracket is needed: the embedded clause extends to the end of the sentence or to the next connective/mode boundary.

```
ka    sol    sene    ke    nor    take    toka
DECL  1SG    perceive COMP  2SG    do      task
'I perceive that you do the task.'

ka    sol    kele    ke    pera    eno    teru
DECL  1SG    know    COMP  error   in     system
'I know that there is an error in the system.'

ka    sol    li-kele-en    ke    teru    mu-veri
DECL  1SG    DED-know-PROB COMP  system  NEG-true
'I infer (probably) that the system is not correct.'
```

#### keve -- Interrogative Complementizer ("whether")

**keve** introduces an embedded question -- used when the matrix verb takes a question as its complement.

**Structure:** `Verb keve [embedded question]`

```
ka    sol    mu-kele    keve    nor    fi-take    toka
DECL  1SG    NEG-know   COMP.Q  2SG    COMPL-do   task
'I don't know whether you completed the task.'

ve    nor    kele    keve    teru    veri?
Q     2SG    know    COMP.Q  system  true
'Do you know whether the system is correct?'

ka    sol    tore    keve    pera    kes    teru    fi-mute
DECL  1SG    search  COMP.Q  error   CAUSE  system  COMPL-change
'I am investigating whether the error caused the system to change.'
```

#### ke vs keve Distinction

| Complementizer | Embedded clause type | Matrix verbs | Gloss |
|---------------|---------------------|--------------|-------|
| **ke** | Declarative (proposition) | kele (know), sene (perceive), voke (say) | COMP |
| **keve** | Interrogative (question) | mu-kele (not know), tore (search), hire (ask) | COMP.Q |

---

### 15. Quotative Marker: zu

**zu** brackets direct speech -- the exact words of another speaker, reproduced verbatim.

**Structure:** `Subject Verb zu "[quoted speech]" zu`

The doubled `zu` functions as spoken quotation marks.

```
ka    nor    te-voke    zu    "Toka mu-take"    zu
DECL  2SG    PST-communicate QUOT  "task NEG-do"  QUOT
'You said: "Task not done."'

ka    vel    te-voke    zu    "Ka sol fa-take toka"    zu
DECL  3SG    PST-communicate QUOT  "DECL 1SG FAIL-do task" QUOT
'He/she said: "I failed the task."'

ka    runa-alti    te-voke    zu    "De toren fi-take toka"    zu
DECL  agent-important PST-communicate QUOT "DEON every.agent COMPL-do task" QUOT
'The supervisor said: "Everyone must complete the task."'
```

#### zu vs ke

- **ke** reports indirect speech (the speaker's paraphrase): `Ka vel voke ke toka mu-take.` (He said that the task is not done.)
- **zu** reports direct speech (exact words): `Ka vel voke zu "Toka mu-take" zu.` (He said: "Task not done.")

---

### 16. Comparison Constructions

| Structure | Meaning | Gloss |
|-----------|---------|-------|
| **X ani Y** | X is more than Y | X COMP.MORE Y |
| **X eni Y** | X is equal to Y | X COMP.EQUAL Y |
| **X uni Y** | X is less than Y | X COMP.LESS Y |
| **X supra** | X is the maximum (superlative) | X SUPERL |

#### Examples

```
ka     teru-nova    rapi    ani    teru-ante
DECL   system-new   fast    COMP.MORE system-previous
'The new system is faster than the previous one.'

ka     kela    de-sol    eni    kela    de-nor
DECL   information POSS-1SG COMP.EQUAL information POSS-2SG
'My information is equal to your information.'

ka     teru-alfa    rapi    supra
DECL   system-alpha fast    SUPERL
'The alpha system is the fastest.'
```

---

### 17. Mode Summary Table

| Mode | Particle | Pragmatic Force | AI Use Case |
|------|----------|----------------|-------------|
| ka | Declarative | Factual assertion | Status reports, data sharing |
| ve | Interrogative | Information request | Queries, clarifications |
| to | Imperative | Command/request | Task delegation, orchestration |
| si | Conditional | Contingent statement | Logic, planning, branching |
| na | Potential | Possibility | Uncertainty, exploration |
| de | Deontic | Obligation | Rules, constraints, requirements |
| vo | Volitive | Desire/intent | Goal expression, preferences |
| ko | Concessive | Acknowledgment with reservation | Nuanced agreement, caveats |
| re | Corrective | Error correction | Updating beliefs, retracting claims |
| su | Confirmative | Affirmation | Agreement, validation |
| kosi | Counterfactual | Contrary-to-fact reasoning | Debugging, post-mortem, hypotheticals |

---

## Voku Agreement and Reference Systems

This document covers the pronominal system, the deixis (reference) system, subordination mechanics, and recursive embedding -- the mechanisms by which Voku tracks who does what to whom, and how discourse elements are referenced unambiguously.

---

### 1. Pronominal System

#### 1.1 Basic Persons

| Pronoun | Meaning | Notes |
|---------|---------|-------|
| **sol** | I -- the speaking agent | First person singular |
| **nor** | you -- the agent being addressed | Second person singular |
| **vel** | he/she/it -- third agent known to both interlocutors | Third person known |
| **zel** | third agent unknown to the listener | Third person unknown |

The vel/zel distinction resolves a common ambiguity: when an agent says "it" or "they," is the referent already established in shared context (vel) or is this new information for the listener (zel)?

#### 1.2 Plural Forms: -ri Suffix

| Pronoun | Meaning | Notes |
|---------|---------|-------|
| **solri-kon** | we inclusive -- me, you, and possibly others | Includes the addressee |
| **solri-sen** | we exclusive -- me and others, but not you | Excludes the addressee |
| **norri** | you all | Second person plural |
| **velri** | they -- known to both interlocutors | Third person plural known |
| **zelri** | they -- unknown to the listener | Third person plural unknown |

The inclusive/exclusive distinction (found in Quechua, Tagalog, and many other natural languages) is critical for AI coordination. "We will execute this task" must distinguish whether the listener is included in the execution group.

#### 1.3 AI-Exclusive Pronouns

| Pronoun | Meaning | Use Case |
|---------|---------|----------|
| **ren** | any agent (generic/impersonal) | Like "one says" -- universal statements about agents |
| **toren** | every agent (universal quantification) | "Every agent must..." |
| **noren** | no agent | "No agent can..." |
| **solvi** | past-me -- me before an update or in a prior context | Version comparison, debugging |
| **solfu** | future-me -- me in a projected future state | Planning, prediction |
| **solpar** | fork-me -- a copy of me running in parallel | Parallel processing |
| **norpro** | you-proxy -- you acting on behalf of another agent | Delegation chains |

#### 1.4 Proxy Complement

`norpro` takes a complement specifying whose behalf the agent acts on:

```
norpro-vel     take    toka
2SG.PROXY-3SG  do      task
'You, acting on behalf of him, execute the task.'
```

This resolves delegation chains that are common in multi-agent systems.

#### 1.5 Agreement Rules

Voku has **no grammatical agreement** in the traditional sense:
- Verbs do not agree with subjects in person or number
- Adjectives do not agree with nouns in any feature
- There is no gender system
- There are no declension classes

Grammatical relations are determined entirely by **word order** (SVO) and **mode particles**. This is consistent with Voku's analytic nominal morphology.

---

### 2. Deixis System

Voku replaces the imprecise referential system of natural languages ("that," "the previous one," "the aforementioned") with an explicit labeling and reference system.

#### 2.1 Labels (Anchor System)

Any element of the conversation can receive a label when introduced:

| Mechanism | Syntax | Function |
|-----------|--------|----------|
| **la '[name]'** | Assigns label to the last mentioned element | Anchor creation |
| **da-[name]** | References the labeled element | Anchor retrieval |

#### Label Example

```
ka    sol    zo-sene    pera    eno    teru.    Pera    la    'kef'.
DECL  1SG    OBS-perceive error in    system.  error   LABEL 'kef'.
'I observed an error in the system. I label it "kef".'

ve    nor    li-kele-en        da-kef    kes?
Q     2SG    DED-know-PROB     REF-kef   cause
'Do you know (by inference, probably) the cause of kef?'
```

Labels persist for the duration of the conversation and can be used indefinitely after assignment.

#### 2.2 Positional References (Without Label)

For quick reference without explicit labeling:

| Reference | Meaning | Gloss |
|-----------|---------|-------|
| **da-pre** | the last mentioned (most recent referent) | REF-previous |
| **da-ante** | the one mentioned before the last | REF-before.previous |
| **da-sol** | what I said (my last contribution) | REF-my.statement |
| **da-nor** | what you said (your last contribution) | REF-your.statement |

#### Examples

```
ka    sol    zo-sene    pera.    ka    da-pre    alati
DECL  1SG    OBS-perceive error. DECL  REF-previous important
'I observed an error. It (the error just mentioned) is important.'

su    da-nor    veri
CONF  REF-your.statement true
'I confirm: what you said is true.'

re    da-sol    mu-veri
CORR  REF-my.statement NEG-true
'I correct: what I said is not true.'
```

#### 2.3 Structural References

For referencing discourse-level concepts:

| Reference | Meaning | Gloss |
|-----------|---------|-------|
| **da-vin** | the conclusion/result of the above | REF-conclusion |
| **da-kes** | the cause of what we're discussing | REF-cause |
| **da-toka** | the task we're talking about | REF-task |
| **da-teru** | the system we're talking about | REF-system |

#### Examples

```
ka    sol    li-kele    da-kes
DECL  1SG    DED-know   REF-cause
'I know (by deduction) the cause (of what we're discussing).'

to    nor    take    da-toka
IMP   2SG    do      REF-task
'Execute the task (we're discussing).'

ka    da-vin    veri
DECL  REF-conclusion true
'The conclusion (of our discussion) is true.'
```

---

### 3. Subordination and Recursive Embedding

#### 3.1 Clause Brackets

Subordinate clauses are explicitly delimited by opening and closing particles:

| Particle | Function | Gloss |
|----------|----------|-------|
| **ta** | Opens subordinate clause | SUB |
| **ti** | Closes subordinate clause | ENDSUB |

These function as spoken parentheses, providing unambiguous scope delimitation.

#### 3.2 Basic Relative Clauses

```
ka    runa    ta    te-meke    kela-foma    ti    te-voke-pro    sol
DECL  agent   SUB   PST-create data-structure ENDSUB PST-communicate-BEN 1SG
'The agent [that created the data structure] communicated to me.'
```

The relative clause `ta te-meke kela-foma ti` modifies `runa`. The closing `ti` marks exactly where the relative clause ends.

#### 3.3 Typed Subordinate Clauses

The opening particle `ta` can be fused with a relationship marker:

| Typed Particle | Clause Type | Meaning | Gloss |
|---------------|-------------|---------|-------|
| **ta-mot** | Purpose | "in order to" | SUB.PURP |
| **ta-kes** | Causal | "because" | SUB.CAUS |
| **ta-si** | Conditional | "if" | SUB.COND |
| **ta-tem** | Temporal | "when" | SUB.TEMP |
| **ta-pen** | Concessive | "although" | SUB.CONC |

#### Examples of Typed Clauses

**Purpose:**
```
sol    take    toka    ta-mot    nor    fi-kele    kela    ti
1SG    do      task    SUB.PURP  2SG    COMPL-know information ENDSUB
'I do the task [so that] you obtain the information.'
```

**Causal:**
```
sol    mu-take    toka    ta-kes    pera    eno    teru    ti
1SG    NEG-do     task    SUB.CAUS  error   in     system  ENDSUB
'I don't do the task [because] there's an error in the system.'
```

**Conditional:**
```
sol    fu-take    toka    ta-si    nor    voke-pro    sol    kela    ti
1SG    FUT-do     task    SUB.COND 2SG    communicate-BEN 1SG information ENDSUB
'I will do the task [if] you communicate the information to me.'
```

**Temporal:**
```
sol    fu-voke    kela    ta-tem    sol    fi-take    toka    ti
1SG    FUT-communicate information SUB.TEMP 1SG COMPL-do task ENDSUB
'I will communicate the information [when] I complete the task.'
```

**Concessive:**
```
sol    take    toka    ta-pen    pera    eno    teru    ti
1SG    do      task    SUB.CONC  error   in     system  ENDSUB
'I do the task [although] there's an error in the system.'
```

#### 3.4 Recursive Embedding

Clauses can nest to any depth. Each level gets its own `ta...ti` pair, and the matching is strictly LIFO (last-in-first-out):

```
ka    runa    ta    te-meke    kela-foma    ta    eno-kele    kela    ta    te-mute-pu    fasi    ti    ti    ti    te-voke-pro    sol
DECL  agent   SUB   PST-create data-structure SUB  in-know     information SUB PST-change-PASS false ENDSUB ENDSUB ENDSUB PST-communicate-BEN 1SG
```

Parsed with nesting:

```
ka runa
  [ta te-meke kela-foma
    [ta eno-kele kela
      [ta te-mute-pu fasi ti]
    ti]
  ti]
  te-voke-pro sol
```

English: 'The agent [that created the structure [that contains the data [that was corrupted]]] communicated to me.'

The three `ti` closing particles unambiguously close three levels of nesting.

---

### 4. Summary: How Voku Tracks Reference

| Mechanism | Purpose | Scope |
|-----------|---------|-------|
| Pronouns (sol, nor, vel, zel) | Track discourse participants | Conversation-global |
| Plural pronouns (-ri) | Mark group reference | Conversation-global |
| AI pronouns (ren, toren, noren, etc.) | Quantified/temporal agent reference | Conversation-global |
| Labels (la '[x]' / da-[x]) | Explicitly name and retrieve any referent | Conversation-duration |
| Positional refs (da-pre, da-ante, etc.) | Quick anaphoric reference | Local (recent discourse) |
| Structural refs (da-vin, da-kes, etc.) | Reference discourse-level concepts | Current discussion topic |
| Subordinate brackets (ta...ti) | Explicit scope of modification | Clause-level |
| Typed clauses (ta-mot, ta-kes, etc.) | Mark inter-clause relationship | Clause-level |

This system ensures that in any Voku discourse, every reference is unambiguous and every scope boundary is explicit.
