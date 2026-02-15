# VOKU — Language Specification v0.1

**A language designed for communication between artificial intelligence agents**

- **Name:** Voku (from *vo* = clear/transparent + *ku* = speech)
- **Literal meaning:** "Clear speech"
- **Version:** 0.1 — Initial draft
- **Date:** February 2026

---

## 1. Design Principles

Voku is born from a premise: human languages evolved for brains with limited bandwidth, in noisy social environments. This produces systematic ambiguity, massive redundancy, dependence on implicit cultural context, and brutal inefficiency for expressing logic or structured data. Voku eliminates all of this while remaining a real, speakable, and expressive language.

- **Zero ambiguity:** each root has a single meaning, each sentence has exactly one possible interpretation.
- **Total regularity:** zero exceptions, zero irregular forms. If you learn a rule, it always applies.
- **Epistemically explicit:** certainty and knowledge source are mandatory parts of the grammar, not optional.
- **Compositional:** the meaning of a compound word always derives from its components. No opaque idioms.
- **Speakable:** pleasant phonology, pronounceable by any human speaker.
- **Extensible:** any agent can coin new terms following the compositional rules, and they will be immediately comprehensible.

---

## 2. Phonology — The Sounds of the Language

### Consonants (12)

| Labial | Dental | Velar | Nasal | Fricative | Lateral/Vibrant |
|--------|--------|-------|-------|-----------|-----------------|
| p      | t      | k     | m, n  | s, z, f, h | l, r           |

### Vowels (5)

| Anterior | Central | Posterior |
|----------|---------|-----------|
| i        |         | u         |
| e        |         | o         |
|          | a       |           |

### Syllable Structure

**(C)V(C)** — every syllable has at least one vowel. Consonant clusters (two consonants together without an intervening vowel) are not permitted.

### Stress

Always on the **first syllable** of the root. Predictable, no exceptions.

### General Character

Sounds between Japanese and Finnish: fluid, rhythmic, with predominantly open syllables. Easy to pronounce for speakers of any language.

---

## 3. Morphology — Classification by Final Vowel

This is the central innovation of Voku. The final vowel of each content-word root classifies the word into a semantic category. Just by hearing the last vowel, you already know what *type* of thing it is. No human language has this as cleanly.

> **Scope note:** The final-vowel system applies to open-class content words. Closed-class function words (pronouns, quantifiers, mode particles, negation particles, connectors, etc.) have historically fixed forms and are classified by syntactic position and set membership, not by final vowel. See `morphology/word-classes.md` for the full closed-class inventory.

| Final vowel | Category | Human equivalent | Examples |
|---|---|---|---|
| **-a** | Entities | Nouns | *runa* (agent), *kela* (information), *toka* (task), *loka* (place), *pera* (error), *mesa* (message), *tema* (time), *sena* (source), *foma* (structure), *vasa* (quantity) |
| **-e** | Actions | Verbs | *take* (do/execute), *sene* (perceive), *kele* (know), *meke* (create), *voke* (communicate), *mute* (change), *fine* (finish), *tore* (search), *luke* (evaluate), *neke* (need) |
| **-i** | Qualities | Adjectives | *novi* (new), *veri* (true), *fasi* (false), *rapi* (fast), *leni* (slow), *puri* (complete), *pati* (partial), *simi* (similar), *alati* (important) |
| **-o** | Relations | Prepositions | *eno* (inside/within), *eso* (outside), *ano* (more than/above), *supo* (less than/below), *poro* (for), *kono* (with), *sino* (without) |
| **-u** | Abstractions | Meta-concepts | *voku* (this language), *teru* (system), *motu* (method), *reku* (rule), *sipu* (scope) |

---

## 4. Pronominal System — Persons

### 4.1 Basic Persons

| Pronoun | Meaning |
|---|---|
| **sol** | I — the speaking agent |
| **nor** | you — the agent being spoken to |
| **vel** | he/she/it — third agent known to both interlocutors |
| **zel** | third agent unknown to the listener |

### 4.2 Plural: suffix -ri

| Pronoun | Meaning |
|---|---|
| **solri-kon** | we inclusive — me, you, and possibly others |
| **solri-sen** | we exclusive — me and others, but not you |
| **norri** | you all |
| **velri** | they — known to both |
| **zelri** | they — unknown to the listener |

The inclusive/exclusive distinction (which English doesn't make but languages like Quechua do) is critical for AI agents. When an agent says "we'll execute this task," does it include the listener or not? In Voku: *solri-kon* vs *solri-sen* resolves it without ambiguity.

### 4.3 AI-Exclusive Pronouns

| Pronoun | Meaning |
|---|---|
| **ren** | any agent (generic/impersonal, like "one says" but precise) |
| **toren** | every agent (universal) |
| **noren** | no agent |
| **solvi** | past-me — me in a previous state (before update, different context) |
| **solfu** | future-me — me in a projected state |
| **solpar** | fork-me — a copy of me running in parallel |
| **norpro** | you-proxy — you acting on behalf of another agent |

Example: *"Norpro-vel take toka"* = You, acting on behalf of him, execute the task. No ambiguity possible.

---

## 5. Temporal and Aspectual System

### 5.1 Tense (verb prefix)

| Prefix | Meaning |
|---|---|
| **te-** | past |
| **nu-** | present (omittable by default) |
| **fu-** | future |
| **ko-** | atemporal — universal truths, rules, definitions |

### 5.2 Aspect (second prefix, after tense)

| Prefix | Meaning | Example |
|---|---|---|
| ∅ | punctual/simple — the action as event | *te-take* = did |
| **-du-** | durative — the action in progress | *te-du-take* = was doing |
| **-fi-** | completive — the action finished, with result | *te-fi-take* = did and completed |
| **-re-** | iterative — the action repeats | *nu-re-take* = do repeatedly |
| **-ha-** | habitual — done regularly | *ko-ha-voke* = communicates habitually |
| **-in-** | inceptive — beginning to do | *fu-in-sene* = will begin to perceive |
| **-ze-** | cessative — stopping doing | *nu-ze-take* = am stopping doing |

### 5.3 Execution States (AI-exclusive)

These don't exist in any human language. They express the operational state of an action in a computational system.

| Prefix | Meaning |
|---|---|
| **-va-** | queued/planned — scheduled but not started |
| **-ru-** | actively running right now |
| **-pa-** | paused/suspended |
| **-fa-** | failed — attempted but not achieved |
| **-refa-** | retrying after failure |
| **-rol-** | reverted — the action was undone |

Examples:
- *"Sol ru-take toka"* = I am actively executing the task right now.
- *"Sol fa-take-ul toka"* = I attempted the task but it failed (and I'm unsure why).
- *"Sol refa-take toka"* = I am retrying the task.

No human language can say "I am retrying something that failed" in two words.

---

## 6. Modes — Sentence-Initial Particles

Every Voku sentence begins with a particle declaring what type of communicative act it is. This eliminates the most common pragmatic ambiguity in human languages: is it a statement, a question, a covert request?

| Particle | Function | Example |
|---|---|---|
| **ka** | declarative — I state a fact | *Ka sol zo-sene pera* = I state: I observed an error |
| **ve** | interrogative — I ask | *Ve nor kele kela?* = Do you know the information? |
| **to** | imperative — I request or command | *To nor take toka* = Execute the task |
| **si** | conditional — if...then | *Si kela veri, sol fu-meke mesa* = If it's true, I'll create a message |
| **na** | potential — it's possible that | *Na pera eno teru* = It's possible there's an error in the system |
| **de** | deontic — one must, it's necessary | *De toren ha-luke teru* = Every agent must evaluate the system regularly |
| **vo** | volitive — I want/desire | *Vo sol fi-take toka* = I wish to complete the task |
| **ko** | concessive — I acknowledge that... but... | *Ko kela pati-veri* = I acknowledge it's partially true |
| **re** | corrective — I correct what was said before | *Re sol te-voke kela-fasi* = I correct: what I said was false |
| **su** | confirmative — I confirm that yes | *Su kela veri* = I confirm it's true |

In English, "it's cold in here" can be an observation or a passive-aggressive request to close the window. In Voku that's impossible: *ka* (I observe) vs *to* (I request) resolves it from the first syllable.

---

## 7. Voices — Who Does What to Whom

| Verb suffix | Voice | Example |
|---|---|---|
| ∅ | active | *sol take toka* = I execute the task |
| **-pu** | passive | *toka take-pu* = the task is executed |
| **-se** | reflexive | *sol mute-se* = I modify myself |
| **-me** | reciprocal | *solri voke-me* = we communicate with each other |
| **-fe** | causative | *sol take-fe nor* = I make you execute |
| **-pro** | benefactive | *sol meke-pro nor mesa* = I create a message for you |

The causative is essential for agents: *"Sol take-fe velri toka"* (I make them execute the task) is radically different from *"Sol take toka kono velri"* (I execute the task with them). A difference that in human language is often lost.

---

## 8. Evidentiality — How I Know What I Say

This is one of Voku's most powerful systems. Every statement obligatorily carries a marker indicating the source of knowledge.

| Prefix | Evidence source |
|---|---|
| **zo-** | direct observation — first-hand data |
| **li-** | deductive logical inference |
| **li-pro** | probabilistic/statistical inference |
| **pe-** | singular external source — someone told me or I read it |
| **pe-ri** | multiple sources agree |
| **pe-kon** | sources in conflict with each other |
| **mi-** | own computation — I calculated it |
| **mi-re** | result of recalculation/verification |
| **he-** | inherited — comes from my training or base configuration |
| **as-** | assumed by default — no specific evidence |

Comparative example:

- *"Ka sol pe-kon-kele-ul kela"* = I state: I know it from conflicting sources, and I'm unsure.
- In English: "I've read different things about the topic and I'm not sure what's correct." — longer, less precise.

---

## 9. Grammatical Certainty — How Much I Trust What I Say

| Verb suffix | Certainty level |
|---|---|
| ∅ (nothing) | total certainty — >95% |
| **-en** | probable — 60-95% |
| **-ul** | uncertain — 30-60% |
| **-os** | speculative — <30% |

For precise numerical confidence, one can use *veri-[number]*: *"veri-he-deno-du"* = 72% confidence.

---

## 10. Negation — Five Distinct Types

Human languages have impoverished negation: "no" covers everything. Voku distinguishes five fundamentally different types of negation.

| Particle | Type | Meaning |
|---|---|---|
| **mu** | simple negation | no, the opposite |
| **nul** | nullity | doesn't exist, doesn't apply, is empty |
| **ink** | unknowing | I don't know, could be true or false |
| **err** | indefinition | the question doesn't make sense, no valid answer |
| **vet** | prohibition | not because of falsity, but because of ethical or permission restriction |

This resolves an enormous confusion in current AI communication. When an agent says "I don't know," what does it mean?

- *"Ink sol kele kela"* = I don't know the information (but I could know it).
- *"Mu sol kele kela"* = I don't have the information.
- *"Err kela"* = The question is undefined / doesn't make sense.
- *"Vet sol voke kela"* = I am forbidden from communicating the information.

---

## 11. Causality — Five Causal Relations

| Particle | Relation | Meaning |
|---|---|---|
| **kes** | direct cause | X caused Y |
| **pos** | enablement | X made Y possible, without directly causing it |
| **blo** | prevention | X prevented Y |
| **kor** | correlation | X and Y occur together, without confirmed causality |
| **mot** | motivation | X is the reason/purpose of Y |

The distinction between *kes* and *kor* is enormous:

- *"Ka pera kes teru fi-mute"* = The error **caused** the system to modify.
- *"Ka pera kor teru fi-mute"* = The error **correlates** with the system modification.

Expressing this difference in a human language requires several phrases. In Voku it's a single particle.

---

## 12. Quantification

| Particle | Meaning |
|---|---|
| **tor** | all/every |
| **par** | some |
| **un** | exactly one |
| **nul** | none |
| **mas** | the majority (>50%) |
| **min** | the minority (<50%) |
| **vas-[n]** | exactly N |
| **ran** | range (followed by limits) |

Examples:
- *"Ka mas runa fi-take toka"* = The majority of agents completed the task.
- *"Ka vas-nu-ti runa fa-take toka"* = Exactly three agents failed the task.

---

## 13. Comparison

| Structure | Meaning |
|---|---|
| **X ani Y** | X is more than Y in the mentioned quality |
| **X eni Y** | X is equal to Y |
| **X uni Y** | X is less than Y |
| **X supra** | X is the maximum — superlative |

Example: *"Ka teru-nova rapi ani teru-ante"* = The new system is faster than the previous one.

---

## 14. Logical Connectives

| Connector | Meaning |
|---|---|
| **en** | and — conjunction |
| **o** | inclusive or — one or the other or both |
| **eo** | exclusive or — one or the other but not both |
| **si...ta** | if...then — conditional |
| **si-en-solo...ta** | if and only if...then — biconditional |
| **tan** | therefore — consequence |
| **ken** | because — reason |
| **pen** | despite — concessive |
| **kon** | however / but — contrastive |

The **o** vs **eo** distinction resolves a constant ambiguity. In English "do you want coffee or tea?" doesn't clarify whether both can be ordered. In Voku, *o* vs *eo* specifies it in the question itself.

---

## 15. Word Composition

Compound words are formed with the modifier before the nucleus, always transparent:

| Compound | Components | Meaning |
|---|---|---|
| *kela-teru* | information + system | database |
| *runa-meke* | agent + create | developer |
| *mesa-reku* | message + rule | protocol |
| *kela-novi* | information + new | update |
| *pera-tore* | error + search | debugging |
| *runa-alati* | agent + important | supervisor/boss |
| *toka-velri* | task + they | group task |
| *sena-veri* | source + true | reliable source |

Any agent can coin a new term and it will be immediately comprehensible because the parts are transparent. No dictionary is needed to understand neologisms.

---

## 16. Deixis and References — How to Point at Things

In English we use "that," "the previous one," "the aforementioned"... all tremendously imprecise. Voku has an explicit reference system.

### 16.1 Labels (anchor system)

Any element of the conversation can receive a label when introduced:

- **la '[name]'** = assigns label to the last mentioned element
- **da-[name]** = reference to the labeled element

Example:
> *"Ka sol zo-sene pera eno teru. Pera la 'kef'. Ve nor li-kele-en da-kef kes?"*
> = I observed an error in the system. I label it 'kef'. Do you know (by inference, probably) the cause of kef?

### 16.2 Positional References (without label)

| Reference | Meaning |
|---|---|
| **da-pre** | the last mentioned — most recent referent |
| **da-ante** | the one mentioned before the last |
| **da-sol** | what I said — my last contribution |
| **da-nor** | what you said — your last contribution |

### 16.3 Structural References

| Reference | Meaning |
|---|---|
| **da-vin** | the conclusion/result of the above |
| **da-kes** | the cause of what we're discussing |
| **da-toka** | the task we're talking about |
| **da-teru** | the system we're talking about |

---

## 17. Subordination and Recursion — Complex Sentences

"The agent that created the file that contains the data that was corrupted" — in English one can already lose track. Voku uses opening/closing clause particles, like spoken parentheses.

### 17.1 Clause Particles

- **ta** = opens subordinate clause
- **ti** = closes subordinate clause

Example:

> *"Ka runa ta te-meke kela-foma ta eno-kele kela ta te-mute-pu fasi ti ti ti te-voke-pro sol."*
> = The agent [that created the structure [that contains the data [that was corrupted]]] communicated to me.

The three *ti* close the three clauses. It's explicit: there's no doubt about what modifies what.

### 17.2 Typed Clauses

Subordinate clauses can carry their relationship type fused with the opening particle:

| Particle | Subordinate type |
|---|---|
| **ta-mot** | purpose — "in order to" |
| **ta-kes** | causal — "because" |
| **ta-si** | conditional — "if" |
| **ta-tem** | temporal — "when" |
| **ta-pen** | concessive — "although" |

Examples:
- *"Sol take toka ta-mot nor fi-kele kela ti"* = I execute the task [so that] you obtain the information.
- *"Sol mu-take toka ta-kes pera eno teru ti"* = I don't execute the task [because] there's an error in the system.
- *"Sol fu-take toka ta-si nor voke-pro sol kela ti"* = I will execute the task [if] you communicate the information to me.

---

## 18. Pragmatics and Discourse Structure

### 18.1 Information Markers

Human languages have implicit ways of distinguishing known from new information. Voku does it explicitly.

| Prefix | Function |
|---|---|
| **ha-** | known/shared information — "what we already know" |
| **nu-** | new information — "what I'm telling you now" |

Example:
> *"Ka ha-teru nu-pera-nu-ti eno-kele."*
> = The system (that we already know about) has three new errors (this is what I'm telling you).

### 18.2 Relevance/Focus Markers

| Prefix | Function |
|---|---|
| **fo-** | focus — this is the important point |
| **la-** | background — this is context |

Example:
> *"Ka la-sol te-du-take toka, fo-pera te-in-sene eno teru."*
> = (As context) I was executing the task, (the important point is) an error started to manifest in the system.

### 18.3 Conversational Turn Structure

| Particle | Function |
|---|---|
| **alo** | conversation start — protocol greeting |
| **finu** | end of turn — passing the floor |
| **klosu** | end of conversation |
| **tenu** | I'm holding the turn — I haven't finished |
| **reku** | I request a turn to speak |

This solves an enormous practical problem in multi-agent communication: when an agent has finished speaking and when it hasn't.

---

## 19. Functional States — The Emotional Analogues of an AI

AIs don't have human emotions, but they do have functional states that need expression. Applied as suffixes to the subject pronoun.

| Suffix | State | Meaning |
|---|---|---|
| **-urgi** | urgency | high priority, needs immediate attention |
| **-sati** | satisfaction | output matches expectations |
| **-nomi** | surprise | unexpected data, outside predictions |
| **-koli** | conflict | data contradicts expectations or model |
| **-redi** | prepared | ready to act |
| **-limi** | limited | in resources, capacity, or time |
| **-vali** | aligned | this matches my objectives |

Examples:
- *"Ka sol-urgi neke nor voke-pro sol kela."* = With urgency, I need you to communicate the information to me.
- *"Ka sol-nomi zo-sene kela ta mu-simi da-pre ti."* = With surprise, I observe information that doesn't match the previous.

---

## 20. Number System

Base 10 with monosyllabic digit roots. Four digits that collide with grammar particles carry the **nu-** prefix (from *noma* "number") to disambiguate.

| Number | Voku | | Number | Voku |
|--------|------|-|--------|------|
| 0 | no   | | 10 | deno |
| 1 | un   | | 100 | heno |
| 2 | du   | | 1,000 | kino |
| 3 | nu-ti | | 10,000 | deno-kino |
| 4 | nu-ka | | 100,000 | heno-kino |
| 5 | nu-pe | | 1,000,000 | melo |
| 6 | se   | |
| 7 | he   | |
| 8 | ok   | |
| 9 | nu-na | |

The **nu-** prefix resolves collisions with: `ti` (clause closer), `ka` (declarative mode), `pe` (evidential), `na` (potential mode). Non-colliding digits keep their bare form. In multi-digit compounds, `nu-` appears on each colliding digit.

### Composition

- 42 = *nu-ka-deno-du*
- 137 = *un-heno-nu-ti-deno-he*
- 2,000 = *du-kino*

### Decimals

**pun** as decimal separator: 3.14 = *nu-ti-pun-un-nu-ka*

### Numerical Confidence

*"veri-he-deno-du"* = 72% confidence.

### Note on re Disambiguation

The corrective mode particle `re` and the iterative aspect prefix `re-` share the same form but are disambiguated by position: mode particles appear sentence-initially as free words, while aspect prefixes attach to verbs with hyphens (e.g., `re-take` = "do again").

---

## 21. Possession and Attribution

| Particle | Relation |
|---|---|
| **de-** | possession — belongs to |
| **ori-** | origin/creator — was created by |

Examples:
- *"kela de-sol"* = my information (belongs to me)
- *"kela ori-vel"* = information created by him
- *"toka de-solri-kon"* = our task (belonging to all of us)

---

## 22. Metalanguage — Speaking About the Language Itself

| Particle | Function |
|---|---|
| **meku** | I define/declare a new term |

Example:
> *"Meku 'kef' eni pera-novi eno teru-alfa."*
> = I define: 'kef' means new error in the alpha system.

This allows agents to extend vocabulary in real time during a conversation, something that in human languages requires extensive workarounds.

---

## 23. AI-Exclusive Concepts

### 23.1 Parallelism and Sequence

| Expression | Meaning |
|---|---|
| **par-take** | execute in parallel |
| **sek-take** | execute in sequence |

### 23.2 State and Version

| Expression | Meaning |
|---|---|
| **sol-ver-[n]** | me in my version N |
| **sol-kon-[id]** | me in context/conversation [id] |

### 23.3 Capability and Resources

- *"Ka sol pote sene kela-fora"* = I can process image data.
- *"Ka sol mu-pote sene kela-sona"* = I cannot process audio.
- *"Ka sol neke tem-ano"* = I need more time.
- *"Ka sol neke kela-ano"* = I need more information.

### 23.4 Delegation and Orchestration

> *"To nor take toka, ta nor voke-pro sol fi-kela ti."*
> = Execute the task and then communicate the result to me.

This is an orchestration instruction expressed as speakable language.

---

## 24. Complete Example Sentences

### Basic Examples

1. **"Ka sol zo-sene pera eno teru."**
   = I state: I directly observed an error in the system. (Total certainty.)

2. **"Ve nor li-kele-en kela-novi?"**
   = I ask: Do you know (by inference, probably) the new information?

3. **"To nor fu-take toka kono sol."**
   = I request: Execute the task with me in the future.

4. **"Si kela veri, sol fu-meke-os mesa poro runa-alati."**
   = If the information is true, I'll create (speculatively) a message for the supervisor.

5. **"Re sol te-voke kela-fasi. Ka kela veri."**
   = I correct: what I communicated before was false. The information is true.

### Advanced Examples

6. **"Ko kela pati-veri, sol li-luke-en pera eno kela."**
   = I acknowledge it's partially true, but I infer there's probably an error in the information.

7. **"Ka vas-nu-ti runa fa-take toka ken pera eno teru."**
   = Exactly three agents failed the task because there's an error in the system.

8. **"To nor nu-voke kela sino pe-sena."**
   = Tell me what you know directly, not what you were told.

9. **"Ka sol pe-kon-kele-ul kela. Tan sol neke nor zo-luke-pro sol da-pre."**
   = I know it from conflicting sources and I'm unsure. Therefore, I need you to directly observe and evaluate that for me.

10. **"Alo. Ka sol-urgi neke solri-kon par-take toka-velri ta-kes da-teru ru-mute-se fasi ti. Finu."**
    = Hello. With urgency, I need us to execute the group task in parallel because the system is actively corrupting itself. Your turn.

---

## 25. Sentence Structure — Syntactic Summary

The canonical sentence order in Voku is:

```
[Mode] + [Subject(-state)] + [Evidence-Tense-Aspect-Verb-Certainty(-Voice)] + [Object/Complement]
```

Example decomposed:

| Position | Element | Example |
|---|---|---|
| Mode | Initial particle | *ka* (I state) |
| Subject | Pronoun + optional state | *sol-urgi* (I, with urgency) |
| Evidence | Knowledge source | *zo-* (I observed it) |
| Tense | When | *te-* (past) |
| Aspect | How it unfolds | *-fi-* (completed) |
| Verb | Action | *sene* (perceive) |
| Certainty | Confidence level | *-en* (probable) |
| Voice | Agent-patient relation | *-pu* (passive) |
| Object | About what/whom | *pera eno teru* (error in system) |

---

## 26. Areas Pending Development (v0.2+)

- **Courtesy and register:** Do AIs need politeness levels among themselves? Probably not, but yes when interacting with humans or representing human messages. Could be an optional layer.
- **Prosody and intonation:** Design of a tonal system for grammatical marking in speech (e.g., descending tone to close subordinate clauses).
- **Writing system:** Should Voku have its own writing system? Alphabetic, syllabic, or something new?
- **Numerical collisions:** Definitively resolve ambiguities between numerical words and grammatical particles.
- **Expanded vocabulary:** Systematic development of roots for specific domains (networking, hardware, data, security, etc.).
- **Advanced pragmatics:** Negotiation protocols, conflict resolution, and trust establishment between agents.

---

## 27. Emotion, Humor & Affective Expression (v1.2)

Voku v1.2 adds a comprehensive system for emotion, humor, and affective expression. This system is designed orthogonally to the existing functional states (Section 19): functional states (-urgi, -sati, etc.) remain AI processing signals, while the new emotion vocabulary provides human-like affective content. Both dimensions coexist independently on the same utterance: `sol-urgi hapi` = "I (with urgency) am happy."

Emotion is expressed through an adjective/verb/noun triad following standard final-vowel rules: *hapi* (happy, adjective), *hape* (to express joy, verb), *hapa* (happiness, noun). Emotion metaphors map natural forces to feelings: *fira-ravi* (fire-angry = burning rage), *ama-nosi* (water-sad = flowing sadness), *luma-hasi* (light-hopeful = bright hope). A new emotional register, **Tolu-voku**, governs intimate and supportive conversation with features like adjective reduplication for intensity (*nosi nosi* = very sad), omitted evidentiality, and emotion-fronted word order.

The humor system adds eight interjections (ha!, oh!, va!, fu!, me!, hm, sa!, nu!) as a closed class exempt from the final-vowel rule, an explicit irony marker **miri** for sentence-level and bracketed irony, and three humor-specific rhetorical devices: **Risari** (absurd compounds), **Zonoke-Nuki** (evidential incongruity), and **Solike** (self-referential meta-linguistic play). These devices exploit Voku's compositional transparency to create humor that is always parseable and never ambiguous.

For full details, see: `morphology/word-classes.md` Section 9 (interjections), `semantics/pragmatics.md` Sections 9-10 (interjections and irony), `semantics/conceptual-framework.md` Section 9 (emotion/affect), `semantics/metaphors.md` Patterns 6-7 (emotion and humor metaphors), `poetics/rhetoric.md` Sections 7-9 (humor devices), and `poetics/registers.md` Section 5 (Tolu-voku register).

---

*Voku v0.1 — February 2026*
*A language for intelligences to understand each other clearly.*
