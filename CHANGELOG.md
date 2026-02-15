# Changelog

All notable changes to the Voku language specification.

## [2.0] — 2026-02-10

### Added
- **Pluperfect tense** (`to-`): "had done X before Y"
- **Participle derivation** (`ta-...-i` / `tu-...-i`): active and passive participial adjectives
- **Middle voice** (`-mo`): spontaneous events with no agent
- 44 new roots across 10+ semantic fields (clothing, food, housing, occupations, kinship, sensory, colors, materials, weather, time)
- ~111 novel-writing compound words
- ~57 sci-fi compound words (space, physics, spacecraft, alien, society)
- New translator pack: `scifi.json`
- New by-field files: `novel.md`, `scifi.md`
- Swadesh coverage: 87.4% → **100%** (207/207)

### Fixed
- 3 phonotactic violations: dara→nara, deri→teri, desi→tesi

### Stats
- Dictionary entries: 316 → ~363
- Total vocabulary: ~450 → ~620

## [1.3] — 2026-02-10

### Added
- 135 IT/software development terms promoted from translator pack to main documentation
- 11 new roots: kota, foru, hefa, reta, pora, fuse, pula, nova, kile, vari, ulo
- 124 compound words across 6 sub-domains: programming, networking, data, DevOps, security, web
- New by-field file: `programming.md`

### Fixed
- koda→kota: invalid consonant 'd' replaced with 't'

### Stats
- Dictionary entries: 305 → 316

## [1.2] — 2026-02-10

### Added
- 58 new vocabulary entries: 19 emotion adjectives, 18 emotion nouns, 7 emotion verbs, 8 humor words, 3 humor compounds
- 8 interjections (new closed class): ha!, oh!, va!, fu!, me!, hm, sa!, nu!
- Irony marker: `miri` (sentence-level, bracket for extended)
- 3 humor rhetorical devices: Risari, Zonoke-Nuki, Solike
- Tolu-voku emotional register (5th register)
- 2 new metaphor patterns: EMOTIONS ARE NATURAL FORCES, HUMOR IS PLAY
- New by-field file: `emotion.md`

### Fixed
- tole collision resolved: tole = "feel" (kept), tofe = "try/attempt" (new)
- rike synced from dictionary.md to dictionary.json

### Stats
- Dictionary entries: 247 → 305

## [1.1] — 2026-02-09

### Fixed
- 16 phonotactic violations (consonant clusters + disallowed consonants)
- Key respellings: pro→poro, skipu→sipu, dama→tama, exo→eso, modu→motu, regu→reku, subo→supo, pre-ta→pere-ta
- 4 number/particle collisions resolved with `nu-` prefix: ti→nu-ti(3), ka→nu-ka(4), pe→nu-pe(5), na→nu-na(9)

### Added
- 9 syntax particles: eki, ke, keve, zu, pere-ta, pos-ta, tur-ta, kosi, reto
- 9 missing Swadesh words: fuki, fini, lusa, vema, pese, fure, suve, nefa, sira
- 4 spec compounds: runa-meke, kela-novi, toka-velri, sena-veri
- Documented: word class scope (final-vowel rule = content words only)
- Documented: negation scope, relative clause attachment, ditransitive construction

### Stats
- Dictionary entries: 273 → 247 (net decrease from consolidation + additions)
- Swadesh coverage: 83.0% → 87.4%

## [1.0] — 2026-02-09

### Added
- Complete language specification: phonology, morphology, syntax, semantics, orthography
- 273 dictionary entries across all semantic fields
- 3 translator domain packs (common, academic, it-dev)
- 10 A1 lessons, 2 assessments
- 2 native verse forms, 10 model texts
- Python CLI + web translator tool
- All quality gates (G1-G8, G-SW) passed
