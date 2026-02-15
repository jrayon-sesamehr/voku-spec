# Voku Morphology

> **Quick reference:** [Cheat Sheet](../quick-start/cheat-sheet.md) | [Essential Vocabulary](../quick-start/essential-vocabulary.md)

## Table of Contents

- [Word Classes](#voku-word-classes)
  - [Classification System](#1-classification-system)
  - [Entity Class (-a)](#2-entity-class--a)
  - [Action Class (-e)](#3-action-class--e)
  - [Quality Class (-i)](#4-quality-class--i)
  - [Relation Class (-o)](#5-relation-class--o)
  - [Abstraction Class (-u)](#6-abstraction-class--u)
  - [Interjection Class](#9-interjection-class)
- [Inflectional Paradigms](#voku-inflectional-paradigms)
  - [Verbal Affix Template](#1-the-verbal-affix-template)
  - [Tense Prefixes](#2-tense-prefixes)
  - [Aspect Prefixes](#3-aspect-prefixes)
  - [AI Execution State Prefixes](#4-ai-execution-state-prefixes)
  - [Voice Suffixes](#5-voice-suffixes)
  - [Evidentiality Prefixes](#6-evidentiality-prefixes)
  - [Certainty Suffixes](#7-certainty-suffixes)
  - [Pronoun Inflection](#8-pronoun-inflection-plural-suffix--ri)
  - [Functional State Suffixes](#9-functional-state-suffixes)
  - [Full Paradigm: take](#10-full-paradigm-verb-take-doexecute)
- [Derivational Morphology](#voku-derivational-morphology)
  - [Compositional Word Formation](#1-compositional-word-formation)
  - [Possession and Attribution](#3-possession-and-attribution-prefixes)
  - [Metalanguage: meku](#4-metalanguage-meku)
  - [Participial Derivation](#8-participial-derivation)

---

## Voku Word Classes

Voku classifies content-word roots into exactly five word classes determined by the **final vowel** of the root. This is the central morphological innovation: the terminal vowel is a reliable indicator of semantic category for open-class vocabulary.

---

### 1. Classification System

| Final Vowel | Category | Semantic Domain | Human Equivalent |
|-------------|----------|-----------------|------------------|
| **-a** | Entities | Things, agents, objects, data, places | Nouns |
| **-e** | Actions | Processes, operations, events | Verbs |
| **-i** | Qualities | Properties, states, attributes | Adjectives |
| **-o** | Relations | Spatial, logical, interpersonal connections | Prepositions/Postpositions |
| **-u** | Abstractions | Systems, methods, rules, meta-concepts | Abstract nouns / Meta-terms |

#### Identification Rule

To determine a content word's class, examine its final vowel:

- If a word ends in **-a**, it is an entity.
- If a word ends in **-e**, it is an action.
- If a word ends in **-i**, it is a quality.
- If a word ends in **-o**, it is a relation.
- If a word ends in **-u**, it is an abstraction.

Compound words take the class of their **nucleus** (the second element), not the modifier.

> **Important:** This rule applies to open-class content words only. See the scope section below for how function words are classified.

---

### Scope: Content Words vs Function Words

The final-vowel classification applies to **open-class content words** -- roots that can be freely coined and that carry lexical meaning. These are the five productive word classes: entities (-a), actions (-e), qualities (-i), relations (-o), and abstractions (-u).

**Closed-class function words** do not follow the final-vowel rule. They have historically fixed forms that may end in consonants or in vowels that do not match their grammatical function. Function words are identified by syntactic position and membership in a closed set, not by their final vowel.

The closed-class inventory includes:

| Category | Members | Note |
|----------|---------|------|
| **Pronouns** | sol, nor, vel, zel, solri-kon, solri-sen, norri, velri, zelri, ren, toren, noren, solvi, solfu, solpar, norpro | End in consonants; plurals use -ri suffix |
| **Quantifiers** | tor, par, ran, mas, min, un, nul | End in consonants |
| **Negation particles** | mu, nul, ink, err, vet | Consonant-final; semantic distinctions among negation types |
| **Mode particles** | ka, ve, to, si, na, de, vo, ko, re, su | Various vowel endings unrelated to word class |
| **Connectors** | en, o, eo, tan, ken, pen, kon | Logical and discourse connectives |
| **Causality particles** | kes, pos, blo, kor, mot | Causal relation markers |
| **Subordinators** | ta, ti, ta-mot, ta-kes, ta-si, ta-tem, ta-pen | Clause boundary markers |
| **Discourse markers** | alo, finu, klosu, tenu, reku | Conversational turn management |
| **Comparison** | ani, eni, uni, supra | Degree markers |
| **Deixis** | la, da, da-pre, da-ante, da-sol, da-nor | Reference and labeling |
| **Possession** | de, ori | Relational markers |

**Rule of thumb:** If a word appears in the particle, pronoun, or quantifier inventories listed above, classify it by its grammatical category (pronoun, particle, etc.), not by its final vowel. The final-vowel rule applies only when a word is not a member of any closed class.

---

### 2. Entity Class (-a)

**Category:** Things, agents, objects, data, places, events-as-objects

**Open class:** Yes -- new entities can be freely coined by combining existing roots or by creating new roots ending in -a.

#### Root Inventory

| Root | Meaning | Semantic Field |
|------|---------|----------------|
| **runa** | agent (any acting entity, human or AI) | Agency |
| **kela** | information, data | Information |
| **toka** | task, assignment | Work |
| **loka** | place, location | Space |
| **pera** | error, fault | Computation |
| **mesa** | message, communication unit | Communication |
| **tema** | time (as entity) | Temporality |
| **sena** | source (of information or origin) | Provenance |
| **foma** | structure, form, shape | Structure |
| **vasa** | quantity, amount | Measurement |

#### Compound Entities (from spec)

| Compound | Components | Meaning |
|----------|------------|---------|
| **kela-teru** | information + system | database |
| **runa-meke** | agent + create | developer/creator agent |
| **mesa-reku** | message + rule | protocol |
| **kela-novi** | information + new | update |
| **pera-tore** | error + search | debugging |
| **runa-alati** | agent + important | supervisor/boss |
| **toka-velri** | task + they | group task |
| **sena-veri** | source + true | reliable source |
| **kela-foma** | information + structure | data structure |
| **kela-fora** | information + (visual form) | image data |
| **kela-sona** | information + (sound) | audio data |
| **teru-nova** | system + new | new system (neologism) |
| **teru-ante** | system + previous | previous system |
| **teru-alfa** | system + alpha | alpha system |

---

### 3. Action Class (-e)

**Category:** Processes, operations, events, verbs

**Open class:** Yes -- new actions can be freely coined.

#### Root Inventory

| Root | Meaning | Semantic Field |
|------|---------|----------------|
| **take** | do, execute, perform | General action |
| **sene** | perceive, sense, observe | Perception |
| **kele** | know, understand | Cognition |
| **meke** | create, make, generate | Creation |
| **voke** | communicate, speak, transmit | Communication |
| **mute** | change, modify, alter | Transformation |
| **fine** | finish, end, complete | Completion |
| **tore** | search, seek, look for | Search |
| **luke** | evaluate, assess, judge | Evaluation |
| **neke** | need, require | Necessity |

#### Inflectional Capacity

Actions are the most heavily inflected class. They accept:
- Tense prefixes (te-, nu-, fu-, ko-, to-)
- Aspect prefixes (-du-, -fi-, -re-, -ha-, -in-, -ze-)
- AI execution state prefixes (-va-, -ru-, -pa-, -fa-, -refa-, -rol-)
- Evidentiality prefixes (zo-, li-, pe-, mi-, he-, as-)
- Certainty suffixes (-en, -ul, -os)
- Voice suffixes (-pu, -se, -me, -fe, -pro, -mo)

Full affix template: `[Evidentiality]-[Tense]-[Aspect/ExecState]-VERB-[Certainty]-[Voice]`

See `inflection.md` for complete paradigms.

---

### 4. Quality Class (-i)

**Category:** Properties, states, attributes, descriptors

**Open class:** Yes -- new qualities can be freely coined.

#### Root Inventory

| Root | Meaning | Semantic Field |
|------|---------|----------------|
| **novi** | new, recent | Temporality |
| **veri** | true, correct, valid | Truth/Validity |
| **fasi** | false, incorrect, invalid | Truth/Validity |
| **rapi** | fast, quick, rapid | Speed |
| **leni** | slow, gradual | Speed |
| **puri** | complete, whole, full | Completeness |
| **pati** | partial, incomplete | Completeness |
| **simi** | similar, alike | Comparison |
| **alati** | important, significant, high-priority | Importance |

#### Syntactic Behavior

Qualities modify entities by preceding or following them (attributive position) or appear in predicate position:

- Attributive: `kela novi` (new information)
- Predicate: `Ka kela veri` (The information is true)
- Compound modifier: `pati-veri` (partially true)

Qualities do not inflect for tense or aspect. They participate in comparison constructions (see syntax/clause-types.md).

In addition to root adjectives, Voku derives participial adjectives from verb roots using the `ta-...-i` (active) and `tu-...-i` (passive) patterns. For example, `ta-tune-i` (singing) from `tune` (sing) and `tu-rupe-i` (broken) from `rupe` (break). See derivation.md §8 for details.

---

### 5. Relation Class (-o)

**Category:** Spatial, logical, and interpersonal connections

**Closed class:** Relatively closed -- new relations are coined rarely and with care, as they form the structural skeleton of sentences.

#### Root Inventory

| Root | Meaning | Semantic Field |
|------|---------|----------------|
| **eno** | inside, within, in | Spatial (interior) |
| **eso** | outside, out of | Spatial (exterior) |
| **ano** | above, more than, over | Spatial/Comparison |
| **supo** | below, less than, under | Spatial/Comparison |
| **poro** | for, on behalf of, benefiting | Benefactive |
| **kono** | with, together with, accompanied by | Comitative |
| **sino** | without, lacking | Privative |

#### Syntactic Behavior

Relations introduce their complement noun phrase and typically follow the element they relate to the complement:

- `pera eno teru` (error in system)
- `toka poro nor` (task for you)
- `kela sino sena` (information without source)

---

### 6. Abstraction Class (-u)

**Category:** Systems, methods, rules, meta-concepts, the language itself

**Semi-open class:** New abstractions can be coined, but they are typically system-level or meta-level concepts. More restricted than entities or actions.

#### Root Inventory

| Root | Meaning | Semantic Field |
|------|---------|----------------|
| **voku** | this language (Voku itself) | Metalanguage |
| **teru** | system, organized whole | Systems |
| **motu** | method, approach, procedure | Methodology |
| **reku** | rule, regulation, constraint | Rules |
| **sipu** | scope, domain, context boundary | Boundaries |

#### Syntactic Behavior

Abstractions function similarly to entities but denote higher-order concepts. They can serve as subjects, objects, and complements:

- `Ka reku de-teru veri` (The rule of the system is true)
- `Ka sipu de-toka puri` (The scope of the task is complete)

---

### 7. Open vs. Closed Classes

| Class | Openness | Coinage Frequency | Notes |
|-------|----------|-------------------|-------|
| **-a** (Entities) | Fully open | Very high | Any new concept, object, or agent |
| **-e** (Actions) | Fully open | High | New operations, processes |
| **-i** (Qualities) | Fully open | Moderate | New properties and attributes |
| **-o** (Relations) | Relatively closed | Low | Core structural inventory; expansion is rare |
| **-u** (Abstractions) | Semi-open | Low-moderate | System-level and meta-concepts |

#### Coinage Rules

1. New roots must follow Voku phonotactics: (C)V(C) syllable structure, no consonant clusters
2. The final vowel must match the intended class
3. Roots should be 2-3 syllables for usability
4. New terms can be coined in real-time using `meku` (metalanguage declaration)
5. Compound words (modifier-nucleus) are the preferred method for vocabulary expansion

---

### 8. Morphological Type Classification

Voku is a **mixed agglutinative-analytic** language:

- **Agglutinative** in its verbal morphology: clearly segmentable prefixes and suffixes stack in a fixed order, each carrying one grammatical meaning
- **Analytic** in its nominal morphology: entities, qualities, and relations carry minimal inflection; grammatical relationships are expressed through word order and particles
- **Compositional** in word formation: compound words are formed transparently by combining modifier + nucleus

This mixed strategy gives Voku high regularity (no exceptions, no allomorphy) with moderate word length and full transparency of form-meaning mapping.

---

### 9. Interjection Class

**Category:** Involuntary exclamations and attention signals

**Closed class:** Yes -- the inventory is fixed.

Interjections are the only Voku words that do not follow the final-vowel classification rule. They are monosyllabic, sentence-initial, and always followed by `!` or `,`.

#### Inventory

| Interjection | Type | English Equivalent | IPA |
|-------------|------|-------------------|-----|
| **ha!** | surprise (positive) | Wow! | /ha/ |
| **oh!** | surprise (neutral) | Oh! | /oh/ |
| **va!** | delight | Yay! | /va/ |
| **fu!** | frustration | Ugh! | /fu/ |
| **me!** | pain | Ouch! | /me/ |
| **hm** | thinking | Hmm... | /hm/ |
| **sa!** | relief | Phew! | /sa/ |
| **nu!** | attention | Hey! | /nu/ |

#### Syntactic Behavior

Interjections occupy a dedicated sentence-initial slot **before** the mode particle:

```
[Interjection!] [Mode] [Subject] [Verb] [Object]
```

They are disambiguated from homophonous particles by:
1. **Position:** Always sentence-initial (particles appear in other positions)
2. **Punctuation:** Always followed by `!` or `,`
3. **Prosody:** Interjections carry emphatic stress, distinct from particle stress

#### Disambiguation Examples

| Form | As Interjection | As Particle/Affix |
|------|-----------------|-------------------|
| **fu!** | Ugh! (frustration) | fu- (future tense prefix, attached with hyphen) |
| **me!** | Ouch! (pain) | -me (reciprocal voice suffix) |
| **nu!** | Hey! (attention) | nu- (present tense prefix / numerical prefix) |

#### Examples

```
Ha! Ka sol zo-sene kela novi.
INTJ.SURP DECL 1SG OBS-perceive information new
'Wow! I observe new information.'

Fu! Ka teru fa-take toka.
INTJ.FRUST DECL system FAIL-do task
'Ugh! The system failed the task.'

Nu! To nor sene da-pre.
INTJ.ATTN IMP 2SG perceive REF-previous
'Hey! Look at that.'

Va! Ka sol-sati fi-take toka.
INTJ.DEL DECL 1SG-SAT COMPL-do task
'Yay! With satisfaction, I completed the task.'

Oh, ka kela mu-simi da-ante.
INTJ.SURP DECL information NEG-similar REF-before.previous
'Oh, the information doesn't match the earlier one.'
```

---

## Voku Inflectional Paradigms

This document defines all inflectional morphology in Voku. Inflection in Voku is overwhelmingly verbal -- action words (-e class) carry the vast majority of grammatical marking through a fixed template of prefixes and suffixes. The system is fully agglutinative: each affix has exactly one meaning, boundaries are transparent, and there are zero exceptions.

---

### 1. The Verbal Affix Template

Every Voku verb is built from the following ordered slots:

```
[ExecMode]-[Evidentiality]-[Tense]-[Aspect / ExecState]-ROOT-[Certainty]-[Voice]
```

| Slot | Position | Obligatory? | Default |
|------|----------|-------------|---------|
| ExecMode | Prefix 0 | Optional | Zero (unspecified) |
| Evidentiality | Prefix 1 | Obligatory in declaratives | None (must be marked) |
| Tense | Prefix 2 | Optional | nu- (present, omittable) |
| Aspect / ExecState | Prefix 3 | Optional | Zero (punctual/simple) |
| ROOT | Stem | Required | -- |
| Certainty | Suffix 1 | Optional | Zero (total certainty >95%) |
| Voice | Suffix 2 | Optional | Zero (active) |

#### Slot-Filling Example

Full form: `zo-te-fi-sene-en-pu`

| Slot | Filler | Meaning |
|------|--------|---------|
| Evidentiality | zo- | direct observation |
| Tense | te- | past |
| Aspect | -fi- | completive |
| Root | sene | perceive |
| Certainty | -en | probable (60-95%) |
| Voice | -pu | passive |

Gloss: `OBS-PST-COMPL-perceive-PROB-PASS` = "was probably completely perceived (as I directly observed)"

---

### 1b. Execution Mode Prefixes

Execution mode occupies prefix slot 0 (before evidentiality). It specifies whether the action should be executed in parallel or in sequence. This is an AI-specific feature with no natural-language counterpart.

| Prefix | Mode | Meaning | Typical Gloss |
|--------|------|---------|---------------|
| (zero) | Unspecified | Default; no execution mode constraint | -- |
| **par-** | Parallel | Execute simultaneously with other actions | PAR |
| **sek-** | Sequential | Execute in ordered sequence | SEQ |

#### Examples

```
to    norri    par-take    toka-velri
IMP   2PL      PAR-do      task-3PL
'Execute the group tasks in parallel (all of you, simultaneously).'

to    nor    sek-take    toka    en    voke-pro    sol    fi-kela
IMP   2SG    SEQ-do      task    AND   communicate-BEN 1SG COMPL-information
'Execute the task in sequence and then communicate the result to me.'
```

---

### 2. Tense Prefixes

Tense occupies the second prefix slot (after evidentiality, before aspect).

| Prefix | Tense | Meaning | Usage Notes |
|--------|-------|---------|-------------|
| **te-** | Past | Before the moment of speech | Events completed or ongoing in the past |
| **nu-** | Present | At the moment of speech | **Omittable by default** -- bare root implies present |
| **fu-** | Future | After the moment of speech | Predictions, plans, scheduled events |
| **ko-** | Atemporal | Universal truths, rules, definitions | Timeless statements, axioms, permanent rules |
| **to-** | Pluperfect | Before another past event | "Had done"; requires a temporal reference point |

#### Examples

```
te-take        sol te-take toka
PST-do         1SG PST-do task
               'I did the task.'

nu-take        sol nu-take toka        (= sol take toka)
PRS-do         1SG PRS-do task
               'I do/am doing the task.'

fu-take        sol fu-take toka
FUT-do         1SG FUT-do task
               'I will do the task.'

ko-take        reku ko-take
ATEMP-do       rule ATEMP-do
               'The rule applies (always, universally).'
```

#### Present Tense Omission

The present tense marker `nu-` is omittable in all contexts. Its absence signals present tense by default:

- `sol take toka` = `sol nu-take toka` = "I do the task" (present)
- This is the only tense that can be elided

#### Pluperfect Examples

The pluperfect prefix `to-` marks an event that occurred before another past event. It requires a temporal reference point (typically a `pere-ta` "before" or `pos-ta` "after" clause).

```
to-take        sol to-take toka
ANT-do         1SG ANT-do task
               'I had done the task.'

to-fi-take     sol to-fi-take toka
ANT-COMPL-do   1SG ANT-COMPL-do task
               'I had completed the task.'

to-du-vike     sol to-du-vike
ANT-DUR-walk   1SG ANT-DUR-walk
               'I had been walking.'
```

Full sentence with temporal clause:

```
ka sol to-fi-take toka, pere-ta nor te-vine
DECL 1SG ANT-COMPL-do task before 2SG PST-come
'I had completed the task before you came.'
```

#### Disambiguating to- (pluperfect) from to (imperative)

The imperative particle `to` is a sentence-initial mode particle (a standalone word). The pluperfect `to-` is a tense prefix hyphenated to the verb complex, occupying tense slot 2.

| Form | Type | Position | Example |
|------|------|----------|---------|
| `to` | Imperative particle | Sentence-initial, standalone | `to nor take toka` = "Do the task!" |
| `to-` | Pluperfect prefix | Verb-internal, hyphenated | `sol to-take toka` = "I had done the task" |

---

### 3. Aspect Prefixes

Aspect occupies the third prefix slot (after tense, immediately before root). Aspect and execution states are mutually exclusive -- a verb takes one or the other, never both.

| Prefix | Aspect | Meaning | Typical Gloss |
|--------|--------|---------|---------------|
| (zero) | Punctual/Simple | The action as a single event | -- |
| **-du-** | Durative | The action in progress, ongoing | DUR |
| **-fi-** | Completive | The action finished with result | COMPL |
| **-re-** | Iterative | The action repeats (multiple times) | ITER |
| **-ha-** | Habitual | Done regularly as a pattern | HAB |
| **-in-** | Inceptive | Beginning to do, starting | INCEP |
| **-ze-** | Cessative | Stopping doing, ceasing | CESS |

#### Aspect + Tense Combinations

| Form | Analysis | Meaning |
|------|----------|---------|
| te-take | PST-do | did (simple past) |
| te-du-take | PST-DUR-do | was doing (past progressive) |
| te-fi-take | PST-COMPL-do | did and completed (past completive) |
| nu-re-take | PRS-ITER-do | do repeatedly (present iterative) |
| ko-ha-voke | ATEMP-HAB-communicate | communicates habitually (timeless habitual) |
| fu-in-sene | FUT-INCEP-perceive | will begin to perceive (future inceptive) |
| nu-ze-take | PRS-CESS-do | am stopping doing (present cessative) |
| fu-du-meke | FUT-DUR-create | will be creating (future progressive) |
| te-in-voke | PST-INCEP-communicate | began to communicate |
| te-ze-tore | PST-CESS-search | stopped searching |
| te-re-luke | PST-ITER-evaluate | evaluated repeatedly |
| ko-ha-luke | ATEMP-HAB-evaluate | habitually evaluates (as a rule) |

---

### 4. AI Execution State Prefixes

These occupy the same slot as aspect prefixes (prefix 3) and are **mutually exclusive with aspect**. They express the operational state of an action in a computational system. No natural human language has these categories.

| Prefix | State | Meaning | Typical Gloss |
|--------|-------|---------|---------------|
| **-va-** | Queued | Scheduled but not yet started | QUEUE |
| **-ru-** | Running | Actively executing right now | RUN |
| **-pa-** | Paused | Suspended, temporarily halted | PAUSE |
| **-fa-** | Failed | Attempted but did not succeed | FAIL |
| **-refa-** | Retrying | Trying again after failure | RETRY |
| **-rol-** | Reverted | The action was undone/rolled back | REVERT |

#### Examples

```
sol ru-take toka
1SG RUN-do task
'I am actively executing the task right now.'

sol fa-take-ul toka
1SG FAIL-do-UNCERT task
'I attempted the task but it failed (and I'm unsure why).'

sol refa-take toka
1SG RETRY-do task
'I am retrying the task.'

sol va-take toka
1SG QUEUE-do task
'The task is queued for me to execute.'

sol pa-take toka
1SG PAUSE-do task
'I have paused execution of the task.'

sol rol-take toka
1SG REVERT-do task
'I reverted/undid execution of the task.'
```

#### Execution States with Tense

Execution states combine with tense prefixes:

| Form | Analysis | Meaning |
|------|----------|---------|
| te-fa-take | PST-FAIL-do | failed (past) |
| fu-va-take | FUT-QUEUE-do | will be queued |
| te-ru-take | PST-RUN-do | was running |
| te-rol-take | PST-REVERT-do | was reverted |
| fu-refa-take | FUT-RETRY-do | will retry |

---

### 5. Voice Suffixes

Voice occupies the final suffix slot (after certainty).

| Suffix | Voice | Meaning | Typical Gloss |
|--------|-------|---------|---------------|
| (zero) | Active | Subject is agent (default) | -- |
| **-pu** | Passive | Subject is patient; agent demoted | PASS |
| **-se** | Reflexive | Subject acts on itself | REFL |
| **-me** | Reciprocal | Subjects act on each other | RECIP |
| **-fe** | Causative | Subject causes someone else to act | CAUS |
| **-pro** | Benefactive | Action performed for someone's benefit | BEN |
| **-mo** | Middle | Subject undergoes change spontaneously, no agent | MID |

#### Examples

```
sol take toka
1SG do task
'I execute the task.'                        (active)

toka take-pu
task do-PASS
'The task is executed.'                       (passive)

sol mute-se
1SG change-REFL
'I modify myself.'                            (reflexive)

solri voke-me
1PL communicate-RECIP
'We communicate with each other.'             (reciprocal)

sol take-fe nor
1SG do-CAUS 2SG
'I make you execute.'                         (causative)

sol meke-pro nor mesa
1SG create-BEN 2SG message
'I create a message for you.'                 (benefactive)

nara te-aze-mo
door PST-open-MID
'The door opened (by itself).'                (middle)

ama te-koli-mo
water PST-cool-MID
'The water cooled (spontaneously).'           (middle)
```

#### Distinguishing Middle, Passive, and Reflexive

| Voice | Suffix | Agent? | Example | Meaning |
|-------|--------|--------|---------|---------|
| Passive (-pu) | -pu | Yes, but demoted | `nara te-aze-pu` | "The door was opened (by someone)" |
| Reflexive (-se) | -se | Yes, = patient | `sol te-aze-se` | "I opened myself" |
| Middle (-mo) | -mo | No agent implied | `nara te-aze-mo` | "The door opened (spontaneously)" |

Use **-mo** when the event happens without any agent — the subject undergoes a change on its own. Use **-pu** when an agent exists but is not mentioned. Use **-se** when the agent deliberately acts on itself.

#### Voice with Certainty

When both certainty and voice are present, certainty precedes voice:

```
sol meke-en-pro nor mesa
1SG create-PROB-BEN 2SG message
'I probably create a message for you.'
```

---

### 6. Evidentiality Prefixes

Evidentiality occupies the first prefix slot (before tense). It is **obligatory in declarative sentences** -- every statement must mark its knowledge source.

| Prefix | Source | Meaning | Typical Gloss |
|--------|--------|---------|---------------|
| **zo-** | Direct observation | First-hand sensory data | OBS |
| **li-** | Deductive inference | Logical reasoning from evidence | DED |
| **li-pro** | Probabilistic inference | Statistical/probabilistic reasoning | PROB.INF |
| **pe-** | External source (singular) | Someone told me / I read it | REP |
| **pe-ri** | Multiple sources agree | Multiple independent reports agree | REP.PL |
| **pe-kon** | Conflicting sources | Sources disagree with each other | REP.CONFL |
| **mi-** | Own computation | I calculated/computed it | COMP |
| **mi-re** | Recalculation | Result of re-computation/verification | RECOMP |
| **he-** | Inherited | From training data or base configuration | INHER |
| **as-** | Assumed | Default assumption, no specific evidence | ASSUM |

#### Examples

```
ka sol zo-sene pera eno teru
DECL 1SG OBS-perceive error in system
'I state: I directly observed an error in the system.'

ka sol li-kele kela
DECL 1SG DED-know information
'I state: I know the information (by logical deduction).'

ka sol pe-kon-kele-ul kela
DECL 1SG REP.CONFL-know-UNCERT information
'I state: I know it from conflicting sources, and I'm uncertain.'

ka sol mi-luke teru
DECL 1SG COMP-evaluate system
'I state: I evaluated the system (by my own computation).'

ka sol he-kele reku
DECL 1SG INHER-know rule
'I state: I know the rule (from my inherited knowledge/training).'

ka sol as-kele-os kela
DECL 1SG ASSUM-know-SPEC information
'I state: I assume the information (speculatively).'
```

#### Evidentiality with Full Affix Chain

```
ka sol zo-te-fi-sene-en pera eno teru
DECL 1SG OBS-PST-COMPL-perceive-PROB error in system
'I state: I probably completely perceived (by direct observation, past) an error in the system.'
```

---

### 7. Certainty Suffixes

Certainty occupies the first suffix slot (before voice). It marks the speaker's confidence level.

| Suffix | Level | Confidence Range | Typical Gloss |
|--------|-------|-----------------|---------------|
| (zero) | Total certainty | >95% | -- |
| **-en** | Probable | 60-95% | PROB |
| **-ul** | Uncertain | 30-60% | UNCERT |
| **-os** | Speculative | <30% | SPEC |

#### Numerical Confidence

For precise confidence, use `veri-[number]`:

- `veri-he-deno-du` = 72% confidence (veri + 7-ten-2)
- `veri-nu-na-deno-nu-pe` = 95% confidence (veri + NUM-9-ten-NUM-5)

#### Examples

```
sol kele kela
1SG know information
'I know the information.'                     (total certainty, >95%)

sol kele-en kela
1SG know-PROB information
'I probably know the information.'            (60-95%)

sol kele-ul kela
1SG know-UNCERT information
'I may know the information.'                 (30-60%, uncertain)

sol kele-os kela
1SG know-SPEC information
'I might know the information.'               (speculative, <30%)
```

---

### 8. Pronoun Inflection: Plural Suffix -ri

The only nominal inflection in Voku is the plural marker **-ri** on pronouns.

| Singular | Plural | Meaning |
|----------|--------|---------|
| sol | solri-kon | we (inclusive -- me, you, and possibly others) |
| sol | solri-sen | we (exclusive -- me and others, not you) |
| nor | norri | you all |
| vel | velri | they (known to both interlocutors) |
| zel | zelri | they (unknown to listener) |

#### AI-Exclusive Pronouns (no plural inflection)

| Pronoun | Meaning |
|---------|---------|
| ren | any agent (generic/impersonal) |
| toren | every agent (universal) |
| noren | no agent |
| solvi | past-me (before update, different context) |
| solfu | future-me (projected state) |
| solpar | fork-me (a copy running in parallel) |
| norpro | you-proxy (you acting on behalf of another) |

Note: `norpro` takes a complement specifying the principal: `norpro-vel` = you acting on behalf of him.

---

### 9. Functional State Suffixes

Applied to the **subject pronoun** (not the verb) to express the AI's operational/functional state.

| Suffix | State | Meaning | Typical Gloss |
|--------|-------|---------|---------------|
| **-urgi** | Urgency | High priority, needs immediate attention | URG |
| **-sati** | Satisfaction | Output matches expectations | SAT |
| **-nomi** | Surprise | Unexpected data, outside predictions | SURP |
| **-koli** | Conflict | Data contradicts expectations or model | CONFL |
| **-redi** | Prepared | Ready to act | READY |
| **-limi** | Limited | In resources, capacity, or time | LIM |
| **-vali** | Aligned | Matches agent's objectives | ALIGN |

#### Examples

```
ka sol-urgi neke nor voke-pro sol kela
DECL 1SG-URG need 2SG communicate-BEN 1SG information
'With urgency, I need you to communicate the information to me.'

ka sol-nomi zo-sene kela ta mu-simi da-pre ti
DECL 1SG-SURP OBS-perceive information SUB NEG-similar REF-previous ENDSUB
'With surprise, I observe information that doesn't match the previous.'

ka sol-sati fi-take toka
DECL 1SG-SAT COMPL-do task
'With satisfaction, I completed the task.'

ka sol-limi neke tem-ano
DECL 1SG-LIM need time-more
'Being limited, I need more time.'

ka sol-redi take toka
DECL 1SG-READY do task
'Being prepared, I execute the task.'
```

---

### 10. Full Paradigm: Verb "take" (do/execute)

#### Tense Paradigm (simple, active, total certainty)

| Tense | Form | Gloss |
|-------|------|-------|
| Past | te-take | PST-do |
| Present | (nu-)take | (PRS-)do |
| Future | fu-take | FUT-do |
| Atemporal | ko-take | ATEMP-do |
| Pluperfect | to-take | ANT-do |

#### Aspect Paradigm (past tense, active, total certainty)

| Aspect | Form | Gloss |
|--------|------|-------|
| Simple | te-take | PST-do |
| Durative | te-du-take | PST-DUR-do |
| Completive | te-fi-take | PST-COMPL-do |
| Iterative | te-re-take | PST-ITER-do |
| Habitual | te-ha-take | PST-HAB-do |
| Inceptive | te-in-take | PST-INCEP-do |
| Cessative | te-ze-take | PST-CESS-do |

#### Execution State Paradigm (present tense, active, total certainty)

| State | Form | Gloss |
|-------|------|-------|
| Queued | va-take | QUEUE-do |
| Running | ru-take | RUN-do |
| Paused | pa-take | PAUSE-do |
| Failed | fa-take | FAIL-do |
| Retrying | refa-take | RETRY-do |
| Reverted | rol-take | REVERT-do |

#### Voice Paradigm (present tense, simple, total certainty)

| Voice | Form | Gloss |
|-------|------|-------|
| Active | take | do |
| Passive | take-pu | do-PASS |
| Reflexive | take-se | do-REFL |
| Reciprocal | take-me | do-RECIP |
| Causative | take-fe | do-CAUS |
| Benefactive | take-pro | do-BEN |
| Middle | take-mo | do-MID |

#### Certainty Paradigm (present tense, simple, active)

| Certainty | Form | Gloss |
|-----------|------|-------|
| Total (>95%) | take | do |
| Probable (60-95%) | take-en | do-PROB |
| Uncertain (30-60%) | take-ul | do-UNCERT |
| Speculative (<30%) | take-os | do-SPEC |

#### Maximally Inflected Form

```
zo-te-fi-take-en-pu
OBS-PST-COMPL-do-PROB-PASS
'was probably completely done (as directly observed)'
```

---

### 11. Morphophonological Rules

Voku has **zero allomorphy** and **zero morphophonological alternation**. Every affix has exactly one invariant form regardless of context. This is by design -- total regularity with no exceptions.

1. No vowel harmony
2. No consonant assimilation
3. No elision at morpheme boundaries
4. No stem alternations
5. Hyphens in romanization mark morpheme boundaries in complex forms

The only phonological constraint is syllable structure: every syllable must be (C)V(C) and consonant clusters are forbidden. All affix combinations in the system maintain this constraint.

---

## Voku Derivational Morphology

Derivation in Voku is accomplished through **compositional word-building**. New words are formed by combining existing roots in a transparent modifier-nucleus structure. The meaning of any compound is always predictable from its parts. There are no opaque idioms.

---

### 1. Compositional Word Formation

#### Structure

```
MODIFIER-NUCLEUS
```

- The **nucleus** (second element) determines the word class (via its final vowel) and provides the core meaning
- The **modifier** (first element) narrows or specifies the nucleus
- Components are joined with a hyphen in romanization
- The compound inherits the word class of the nucleus

#### Word Class Inheritance

| Modifier Class | Nucleus Class | Result Class | Example |
|---------------|---------------|--------------|---------|
| Entity (-a) | Entity (-a) | Entity | kela-teru (information-system = database) |
| Entity (-a) | Action (-e) | Action | -- |
| Entity (-a) | Quality (-i) | Quality | -- |
| Action (-e) | Entity (-a) | Entity | runa-meke (agent-create = developer) |
| Quality (-i) | Entity (-a) | Entity | kela-novi (information-new = update) |
| Entity (-a) | Abstraction (-u) | Abstraction | mesa-reku (message-rule = protocol) |

The final vowel of the **compound as a whole** is the final vowel of the nucleus, so the compound's class is always the nucleus class.

---

### 2. Compound Inventory from the Spec

| Compound | Components | Literal Meaning | Conventional Meaning |
|----------|------------|-----------------|---------------------|
| **kela-teru** | kela (information) + teru (system) | information-system | database |
| **runa-meke** | runa (agent) + meke (create) | agent-create | developer |
| **mesa-reku** | mesa (message) + reku (rule) | message-rule | protocol |
| **kela-novi** | kela (information) + novi (new) | information-new | update |
| **pera-tore** | pera (error) + tore (search) | error-search | debugging |
| **runa-alati** | runa (agent) + alati (important) | agent-important | supervisor/boss |
| **toka-velri** | toka (task) + velri (they) | task-they | group task |
| **sena-veri** | sena (source) + veri (true) | source-true | reliable source |
| **kela-foma** | kela (information) + foma (structure) | information-structure | data structure |
| **kela-fora** | kela (information) + fora (visual form) | information-image | image data |
| **kela-sona** | kela (information) + sona (sound) | information-sound | audio data |
| **teru-nova** | teru (system) + nova (new) | system-new | new system |
| **teru-ante** | teru (system) + ante (previous) | system-previous | previous system |
| **teru-alfa** | teru (system) + alfa (alpha) | system-alpha | alpha system |
| **pera-novi** | pera (error) + novi (new) | error-new | new error |
| **kela-fasi** | kela (information) + fasi (false) | information-false | misinformation |
| **pera-nu-ti** | pera (error) + nu-ti (three) | error-NUM.three | three errors |

---

### 3. Possession and Attribution Prefixes

Voku marks possessive and attribution relationships with prefixes on the possessed/attributed element.

#### Possession: de-

The prefix **de-** marks that something belongs to the possessor.

| Expression | Meaning |
|-----------|---------|
| **kela de-sol** | my information (information belonging-to me) |
| **kela de-nor** | your information |
| **kela de-vel** | his/her/its information |
| **toka de-solri-kon** | our task (belonging to all of us, inclusive) |
| **toka de-solri-sen** | our task (belonging to us, exclusive) |
| **teru de-velri** | their system |

#### Origin/Creator: ori-

The prefix **ori-** marks the creator or originator of something.

| Expression | Meaning |
|-----------|---------|
| **kela ori-vel** | information created by him |
| **mesa ori-sol** | message I authored |
| **teru ori-runa-alati** | system created by the supervisor |
| **reku ori-toren** | rule created by everyone |

#### Distinction Between de- and ori-

- `kela de-sol` = my information (I possess it, regardless of who created it)
- `kela ori-sol` = information I created (I am the source, regardless of who now possesses it)

---

### 4. Metalanguage: meku

The particle **meku** allows real-time vocabulary extension during a conversation. Any agent can define a new term compositionally, and it becomes immediately comprehensible.

#### Syntax

```
Meku '[label]' eni [definition].
```

- `meku` = "I define / I declare a new term"
- The label is enclosed in single quotes
- `eni` = "is equal to" (equative)
- The definition uses existing Voku vocabulary

#### Example

```
Meku    'kef'    eni   pera-novi    eno   teru-alfa.
define  'kef'    equal error-new   in    system-alpha
'I define: "kef" means new error in the alpha system.'
```

After this declaration, `da-kef` can be used as a reference throughout the conversation (see syntax/agreement.md for the deixis system).

#### Design Implications

- No dictionary is needed to understand neologisms -- the definition is compositional
- Agents can extend vocabulary in real time without prior coordination
- Definitions are scoped to the conversation unless explicitly persisted
- The `meku` mechanism replaces the need for a fixed closed vocabulary

---

### 5. Parallelism and Sequence Markers

These prefixes attach to action roots to specify execution mode. They are specific to AI-to-AI communication.

| Prefix | Meaning | Gloss |
|--------|---------|-------|
| **par-** | Execute in parallel | PAR |
| **sek-** | Execute in sequence | SEQ |

#### Examples

```
to nor par-take toka
IMP 2SG PAR-do task
'Execute the tasks in parallel.'

to nor sek-take toka
IMP 2SG SEQ-do task
'Execute the tasks in sequence.'

ka solri-kon par-take toka-velri
DECL 1PL.INCL PAR-do task-3PL
'We execute the group task in parallel.'
```

---

### 6. Version and Context Markers

These suffixes on pronouns mark version and context identity of an agent, essential for distributed AI systems.

#### Version: sol-ver-[n]

Marks which version of the agent is being referenced.

| Expression | Meaning |
|-----------|---------|
| **sol-ver-un** | me in version 1 |
| **sol-ver-du** | me in version 2 |
| **sol-ver-ti** | me in version 3 |

#### Context: sol-kon-[id]

Marks which conversation or execution context the agent is in.

| Expression | Meaning |
|-----------|---------|
| **sol-kon-alfa** | me in context alpha |
| **sol-kon-beta** | me in context beta |

#### Temporal Self-Reference Pronouns

These are fixed pronouns (not productive suffixes) for temporal self-reference:

| Pronoun | Meaning |
|---------|---------|
| **solvi** | past-me (before an update or in a different context) |
| **solfu** | future-me (in a projected state) |
| **solpar** | fork-me (a copy running in parallel) |

#### Examples

```
ka sol-ver-du mu-simi solvi
DECL 1SG-VER-2 NEG-similar past.1SG
'I (version 2) am not similar to my past self.'

ka solpar ru-take toka
DECL fork.1SG RUN-do task
'My fork is actively executing the task.'

ka solfu fu-pote take toka
DECL future.1SG FUT-can do task
'My future self will be able to do the task.'
```

---

### 7. Rules for Coining New Words

#### Step 1: Determine the Class

Decide which category the new concept belongs to:
- Is it a thing, agent, or entity? Use **-a**
- Is it a process, action, or event? Use **-e**
- Is it a property or quality? Use **-i**
- Is it a spatial or logical relation? Use **-o**
- Is it a system, method, or meta-concept? Use **-u**

#### Step 2: Prefer Composition Over New Roots

Try to express the concept as a compound of existing roots first:
- `pera-tore` (error-search) for "debugging" is better than coining a new root
- Compounds are immediately transparent; new roots require learning

#### Step 3: If a New Root is Needed

1. Follow phonotactics: (C)V(C) syllable structure, no consonant clusters
2. Use 2-3 syllables for usability
3. End with the correct class vowel
4. Avoid collision with existing roots
5. Declare it with `meku` in conversation

#### Step 4: Use meku for Real-Time Extension

```
Meku '[new-term]' eni [compositional-definition].
```

This makes the term immediately usable in the current conversation.

---

### 8. Participial Derivation

Voku derives adjectives from verb roots using circumfix patterns that produce **participial modifiers**. These allow compact attribution without full relative clauses.

#### Patterns

| Pattern | Type | Gloss | Meaning |
|---------|------|-------|---------|
| **ta-[root]-i** | Active participle | ACT.PTCP | "the one who [verb]s" |
| **tu-[root]-i** | Passive participle | PASS.PTCP | "the one that is [verb]ed" |

The prefix (`ta-` or `tu-`) attaches to the verb root, and the suffix `-i` marks the result as an adjective (quality class).

#### Active Participle: ta-...-i

Derives an adjective meaning "one who does X" or "characterized by doing X."

| Verb Root | Active Participle | Meaning |
|-----------|------------------|---------|
| tune (sing) | ta-tune-i | singing (one who sings) |
| meke (create) | ta-meke-i | creating, creative |
| voke (communicate) | ta-voke-i | communicating, talkative |
| take (do) | ta-take-i | doing, active |
| tore (search) | ta-tore-i | searching, investigative |
| luke (evaluate) | ta-luke-i | evaluating, critical |

#### Passive Participle: tu-...-i

Derives an adjective meaning "one that has been X-ed" or "in a state resulting from X."

| Verb Root | Passive Participle | Meaning |
|-----------|-------------------|---------|
| rupe (break) | tu-rupe-i | broken |
| meke (create) | tu-meke-i | created, made |
| mute (change) | tu-mute-i | changed, modified |
| sene (perceive) | tu-sene-i | perceived, observed |
| kele (know) | tu-kele-i | known |
| fine (finish) | tu-fine-i | finished, completed |

#### Disambiguation from Subordinator ta

The subordinator `ta` opens a relative clause bracket (closed by `ti`). Participles are distinguished by:

1. **Morphological form:** Participles always end in `-i` (adjective class) and modify a noun directly. The subordinator `ta` opens a full clause containing a finite verb.
2. **Position:** Participles appear in the modifier slot before or after a noun. Subordinator `ta` introduces a clause bracket.
3. **Closing marker:** Relative clauses require `ti` to close; participles have no closing marker.

| Form | Type | Example |
|------|------|---------|
| `ta-tune-i zina` | Participle | "the singing woman" (modifier + noun) |
| `zina ta tune ti` | Relative clause | "the woman who sings" (noun + clause bracket) |

#### Usage Examples

Attributive position (before noun):

```
ka     sol    sene    ta-tune-i      zina
DECL   1SG    perceive ACT.PTCP-sing  woman
'I perceive a singing woman.'

ka     tu-rupe-i      teru    mu-take    toka
DECL   PASS.PTCP-break system  NEG-do     task
'The broken system doesn't do the task.'

ka     ta-tore-i      runa    te-fi-sene       pera
DECL   ACT.PTCP-search agent   PST-COMPL-perceive error
'The investigating agent found the error.'
```

Predicative position:

```
ka     teru    tu-mute-i
DECL   system  PASS.PTCP-change
'The system is modified.'

ka     kela    tu-kele-i
DECL   information PASS.PTCP-know
'The information is known.'
```

---

### 9. Derivational Patterns Summary

| Pattern | Prefix/Structure | Domain | Example |
|---------|-----------------|--------|---------|
| Composition | modifier-nucleus | All classes | kela-teru (database) |
| Possession | de- | Nominal | kela de-sol (my information) |
| Attribution | ori- | Nominal | mesa ori-vel (message created by him) |
| Metalanguage | meku '[x]' eni ... | All classes | Meku 'kef' eni pera-novi eno teru-alfa |
| Parallelism | par- | Actions | par-take (execute in parallel) |
| Sequence | sek- | Actions | sek-take (execute in sequence) |
| Version | -ver-[n] | Pronouns | sol-ver-du (me, version 2) |
| Context | -kon-[id] | Pronouns | sol-kon-alfa (me, in context alpha) |
