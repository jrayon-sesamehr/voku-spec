"""Voku Translator - Bidirectional Voku<->English translation engine.

Sentence structure: [Mode] + [Subject(-State)] + [Verb Complex] + [Object/Complement]
Verb template:      [Evidence]-[Tense]-[Aspect/ExecState]-ROOT-[Certainty]-[Voice]
"""

import json
import os
from grammar import VokuGrammar, MODE_PARTICLES, NEGATION_PARTICLES, PRONOUNS, FUNCTIONAL_STATES, NUMBER_WORDS, INTERJECTION_MARKERS, IRONY_MARKERS


class VokuTranslator:
    """Bidirectional Voku<->English translation engine."""

    def __init__(self, dictionary_path=None, pack_paths=None):
        """Load dictionary and optional expansion packs."""
        if dictionary_path is None:
            dictionary_path = os.path.join(os.path.dirname(__file__), "dictionary.json")

        with open(dictionary_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

        self.grammar = VokuGrammar()

        # Build lookup tables
        self._build_lookups()

        # Load expansion packs
        if pack_paths:
            for path in pack_paths:
                self.load_pack(path)

    def _build_lookups(self):
        """Build forward and reverse lookup dictionaries."""
        self.voku_to_eng = {}
        self.eng_to_voku = {}
        self.word_pos = {}

        for entry in self.data["words"]:
            voku = entry["voku"]
            english = entry["english"]
            pos = entry["pos"]
            self.voku_to_eng[voku] = english
            self.word_pos[voku] = pos

            # Build reverse lookup: first English word -> Voku
            for eng_word in english.split(","):
                eng_word = eng_word.strip().lower()
                if eng_word and eng_word not in self.eng_to_voku:
                    self.eng_to_voku[eng_word] = voku
                # Also map individual words from multi-word definitions
                for single in eng_word.split():
                    single = single.strip("()")
                    if single and single not in self.eng_to_voku:
                        self.eng_to_voku[single] = voku

        self.particles = self.data["particles"]

        # Build flat particle lookups for quick access
        self._all_particles = {}
        for category, mapping in self.particles.items():
            for key, val in mapping.items():
                self._all_particles[key] = (category, val)

    def load_pack(self, pack_path: str):
        """Load a domain expansion pack (JSON with same format as dictionary)."""
        with open(pack_path, "r", encoding="utf-8") as f:
            pack = json.load(f)

        if "words" in pack:
            self.data["words"].extend(pack["words"])
            self._build_lookups()

    def lookup_voku(self, word: str) -> str:
        """Look up a Voku word in the dictionary, return English or the word itself."""
        clean = word.rstrip(".,?!").lower()
        if clean in self.voku_to_eng:
            return self.voku_to_eng[clean]
        return None

    def lookup_english(self, word: str) -> str:
        """Look up an English word, return Voku or None."""
        clean = word.lower().strip(".,?!")
        return self.eng_to_voku.get(clean)

    def translate_voku_to_english(self, text: str) -> str:
        """Translate a Voku sentence to English.

        Steps:
        1. Tokenize (split on spaces)
        2. Identify mode particle (first word)
        3. For each token: check if particle, parse verb morphology, lookup in dict
        4. Assemble English output
        """
        tokens = text.strip().split()
        if not tokens:
            return ""

        output_parts = []
        idx = 0

        # 0. Check for interjection (sentence-initial, followed by ! or ,)
        first_raw = tokens[0] if tokens else ""
        interjection_clean = first_raw.rstrip("!,").lower()
        if interjection_clean in INTERJECTION_MARKERS:
            intj_map = {
                "ha": "Wow!", "oh": "Oh!", "va": "Yay!", "fu": "Ugh!",
                "me": "Ouch!", "hm": "Hmm...", "sa": "Phew!", "nu": "Hey!",
            }
            output_parts.append(intj_map.get(interjection_clean, interjection_clean + "!"))
            idx = 1

        # 1. Check for mode particle
        mode_label = None
        if idx < len(tokens):
            mode_candidate = tokens[idx].rstrip(".,?!").lower()
            if mode_candidate in MODE_PARTICLES:
                mode_label = MODE_PARTICLES[mode_candidate]
                idx += 1

        # Process remaining tokens
        while idx < len(tokens):
            token = tokens[idx]
            raw_clean = token.rstrip(".,?!")
            clean = raw_clean.lower()
            punctuation = token[len(raw_clean):]

            # Check for negation particle
            if clean in NEGATION_PARTICLES:
                output_parts.append(self._translate_negation(clean))
                idx += 1
                continue

            # Check for irony marker
            if clean == "miri":
                output_parts.append("(ironic)")
                idx += 1
                continue

            # Check for pronoun (possibly with functional state)
            pronoun_result = self._try_translate_pronoun(clean)
            if pronoun_result:
                output_parts.append(pronoun_result)
                if punctuation:
                    output_parts[-1] += punctuation
                idx += 1
                continue

            # Check for number words (including nu- prefixed)
            num_result = self.grammar.try_parse_number(clean)
            if num_result is not None:
                output_parts.append(str(num_result))
                if punctuation:
                    output_parts[-1] += punctuation
                idx += 1
                continue

            # Check for particles (connectors, quantifiers, etc.)
            particle_result = self._try_translate_particle(clean)
            if particle_result:
                output_parts.append(particle_result)
                if punctuation:
                    output_parts[-1] += punctuation
                idx += 1
                continue

            # Check if it's an inflected verb or compound (contains hyphens)
            if "-" in clean:
                # First try as a compound word (modifier-nucleus)
                compound = self._try_translate_compound(clean)
                # Also try as verb complex
                parsed_verb = self.grammar.parse_verb(clean)
                has_affixes = any([
                    parsed_verb.get("evidence"),
                    parsed_verb.get("tense"),
                    parsed_verb.get("aspect"),
                    parsed_verb.get("exec_state"),
                    parsed_verb.get("certainty"),
                    parsed_verb.get("voice"),
                    parsed_verb.get("negation"),
                ])
                if has_affixes:
                    verb_result = self._translate_verb_complex(clean)
                    output_parts.append(verb_result)
                elif compound:
                    output_parts.append(compound)
                else:
                    # Fallback: try verb complex anyway
                    verb_result = self._translate_verb_complex(clean)
                    output_parts.append(verb_result)
                if punctuation:
                    output_parts[-1] += punctuation
                idx += 1
                continue

            # Direct dictionary lookup
            eng = self.lookup_voku(clean)
            if eng:
                # Take the first definition
                first_def = eng.split(",")[0].strip()
                output_parts.append(first_def)
            else:
                # Check if it's a compound word
                compound = self._try_translate_compound(clean)
                if compound:
                    output_parts.append(compound)
                else:
                    output_parts.append(f"[{clean}]")

            if punctuation:
                output_parts[-1] += punctuation
            idx += 1

        # Assemble final output
        result = " ".join(output_parts)

        # Add mode context as prefix
        if mode_label:
            mode_prefix = self._mode_to_prefix(mode_label)
            if mode_prefix:
                result = mode_prefix + result

        # Capitalize first letter
        if result:
            result = result[0].upper() + result[1:]

        return result

    def translate_english_to_voku(self, text: str) -> str:
        """Translate English text to Voku (basic phrase-level).

        This is a simplified translation:
        1. Tokenize English
        2. Detect sentence type (question -> ve, command -> to, else -> ka)
        3. Lookup each word in reverse dictionary
        4. Apply basic Voku word order (Mode + Subject + Verb + Object)
        """
        tokens = text.strip().rstrip(".?!").split()
        if not tokens:
            return ""

        # Detect sentence type
        original_text = text.strip()
        mode = "ka"  # default declarative
        if original_text.endswith("?"):
            mode = "ve"
        elif original_text.endswith("!"):
            mode = "to"
        # Check for imperative patterns
        first_lower = tokens[0].lower()
        imperative_verbs = {"do", "execute", "tell", "communicate", "send",
                            "search", "find", "create", "make", "help",
                            "open", "close", "give", "come", "go", "stop",
                            "wait", "run", "fix", "evaluate",
                            "laugh", "cry", "smile", "try", "feel",
                            "shout", "whisper", "hug", "joke"}
        if first_lower in imperative_verbs and not original_text.endswith("?"):
            mode = "to"

        voku_parts = [mode]

        for token in tokens:
            clean = token.lower().strip(".,?!;:'\"")
            if not clean:
                continue

            # Skip English articles and auxiliaries
            if clean in {"the", "a", "an", "is", "are", "was", "were", "am",
                         "do", "does", "did", "will", "would", "could", "should",
                         "that", "which", "to", "it"}:
                continue

            # Translate pronouns
            pronoun_map = {
                "i": "sol", "me": "sol",
                "you": "nor",
                "he": "vel", "she": "vel", "him": "vel", "her": "vel",
                "we": "solri-kon", "us": "solri-kon",
                "they": "velri", "them": "velri",
            }
            if clean in pronoun_map:
                voku_parts.append(pronoun_map[clean])
                continue

            # Try reverse dictionary lookup
            voku_word = self.lookup_english(clean)
            if voku_word:
                voku_parts.append(voku_word)
                continue

            # Try common English -> Voku mappings
            common_map = {
                "not": "mu", "no": "mu", "don't": "mu", "doesn't": "mu",
                "in": "eno", "inside": "eno", "within": "eno",
                "outside": "eso", "out": "eso",
                "with": "kono", "without": "sino",
                "for": "poro", "above": "ano", "over": "ano",
                "below": "supo", "under": "supo",
                "and": "en", "or": "o", "but": "kon",
                "because": "ken", "therefore": "tan", "despite": "pen",
                "if": "si", "then": "ta",
                "all": "tor", "some": "par", "every": "tor",
                "new": "novi", "old": "omi",
                "true": "veri", "false": "fasi",
                "fast": "rapi", "slow": "leni",
                "big": "vasi", "small": "puli",
                "good": "vali", "bad": "mali",
                "happy": "hapi", "sad": "nosi", "angry": "ravi", "afraid": "temi",
                "surprised": "huri", "grateful": "tari", "amused": "risi",
                "laugh": "rike", "cry": "vize", "smile": "rile", "joke": "risa",
                "funny": "risi", "humor": "risu", "sarcastic": "zoli",
                "ironic": "miri", "silly": "foli", "absurd": "nuki",
                "emotion": "tolu", "try": "tofe", "feel": "tole",
                "shout": "zome", "whisper": "suse", "hug": "hase",
                "hope": "hasa", "fear": "temi-tole", "proud": "hari",
                "shame": "fuma", "lonely": "soli", "bored": "zoni",
                "confused": "meli", "wow": "ha", "ouch": "me", "hey": "nu",
            }
            if clean in common_map:
                voku_parts.append(common_map[clean])
                continue

            # Unknown word: leave as-is in brackets
            voku_parts.append(f"[{clean}]")

        # Add period
        result = " ".join(voku_parts) + "."
        # Capitalize first letter (mode particle)
        if result:
            result = result[0].upper() + result[1:]
        return result

    def _translate_verb_complex(self, word: str) -> str:
        """Translate an inflected Voku verb complex to English."""
        parsed = self.grammar.parse_verb(word)

        evidence_phrases = {
            "observation": "(by observation)",
            "deduction": "(by deduction)",
            "probabilistic": "(by probability)",
            "external": "(from report)",
            "multiple_sources": "(from multiple sources)",
            "conflicting": "(from conflicting sources)",
            "computation": "(by computation)",
            "recomputation": "(by recomputation)",
            "inherited": "(by training)",
            "assumed": "(by assumption)",
        }

        # Tense
        tense_word = ""
        if parsed.get("tense"):
            tense_map = {"te": "past", "fu": "future", "ko": "always"}
            tense_word = tense_map.get(parsed["tense"], "")

        # Aspect / exec_state
        aspect_word = ""
        if parsed.get("aspect"):
            aspect_map = {
                "du": "is/was",
                "fi": "completed",
                "re": "repeatedly",
                "ha": "habitually",
                "in": "began to",
                "ze": "stopped",
            }
            aspect_word = aspect_map.get(parsed["aspect"], "")
        elif parsed.get("exec_state"):
            exec_map = {
                "va": "queued",
                "ru": "actively",
                "pa": "paused",
                "fa": "failed to",
                "refa": "retrying to",
                "rol": "reverted",
            }
            aspect_word = exec_map.get(parsed["exec_state"], "")

        # Root translation
        root = parsed.get("root", word)
        root_eng = self.lookup_voku(root)
        if root_eng:
            root_eng = root_eng.split(",")[0].strip()
        else:
            root_eng = root

        # Certainty
        certainty_word = ""
        if parsed.get("certainty"):
            cert_map = {"en": "probably", "ul": "maybe", "os": "speculatively"}
            certainty_word = cert_map.get(parsed["certainty"], "")

        # Voice
        voice_word = ""
        if parsed.get("voice"):
            voice_map = {
                "pu": "(passive)",
                "se": "(self)",
                "me": "(each other)",
                "fe": "(caused)",
                "pro": "(for someone)",
            }
            voice_word = voice_map.get(parsed["voice"], "")

        # Assemble: build a natural-ish English phrase
        # Pattern: [negation] [certainty] [aspect-prefix] [tense-form of root] [evidence] [voice]
        result_parts = []

        # Negation
        if parsed.get("negation"):
            result_parts.append(self._translate_negation(parsed["negation"]))

        if certainty_word:
            result_parts.append(certainty_word)

        # Build the main verb phrase
        if aspect_word and parsed.get("aspect") == "fi":
            # Completive: "completed perceiving"
            if tense_word == "past":
                result_parts.append("completed")
                result_parts.append(_gerund(root_eng))
            elif tense_word == "future":
                result_parts.append("will complete")
                result_parts.append(_gerund(root_eng))
            else:
                result_parts.append("completed")
                result_parts.append(_gerund(root_eng))
        elif aspect_word and parsed.get("aspect") == "du":
            if tense_word == "past":
                result_parts.append("was")
                result_parts.append(_gerund(root_eng))
            elif tense_word == "future":
                result_parts.append("will be")
                result_parts.append(_gerund(root_eng))
            else:
                result_parts.append("is")
                result_parts.append(_gerund(root_eng))
        elif aspect_word and parsed.get("aspect") == "in":
            if tense_word == "past":
                result_parts.append("began to")
            elif tense_word == "future":
                result_parts.append("will begin to")
            else:
                result_parts.append("begins to")
            result_parts.append(root_eng)
        elif aspect_word and parsed.get("aspect") == "ze":
            if tense_word == "past":
                result_parts.append("stopped")
            else:
                result_parts.append("stops")
            result_parts.append(_gerund(root_eng))
        elif aspect_word and parsed.get("aspect") == "re":
            if tense_word == "past":
                result_parts.append("repeatedly " + _past(root_eng))
            else:
                result_parts.append("repeatedly " + root_eng)
        elif aspect_word and parsed.get("aspect") == "ha":
            result_parts.append("habitually")
            result_parts.append(root_eng + "s")
        elif parsed.get("exec_state"):
            es = parsed["exec_state"]
            if es == "fa":
                if tense_word == "past":
                    result_parts.append("failed to " + root_eng)
                else:
                    result_parts.append("fails to " + root_eng)
            elif es == "ru":
                result_parts.append("is actively " + _gerund(root_eng))
            elif es == "va":
                result_parts.append("has queued " + root_eng)
            elif es == "pa":
                result_parts.append("has paused " + _gerund(root_eng))
            elif es == "refa":
                result_parts.append("is retrying " + root_eng)
            elif es == "rol":
                result_parts.append("reverted " + root_eng)
        else:
            # Simple tense
            if tense_word == "past":
                result_parts.append(_past(root_eng))
            elif tense_word == "future":
                result_parts.append("will " + root_eng)
            elif tense_word == "always":
                result_parts.append("always " + root_eng + "s")
            else:
                result_parts.append(root_eng)

        if parsed.get("evidence"):
            result_parts.append(evidence_phrases.get(
                self.grammar.get_evidence_label(parsed["evidence"]), ""))

        if voice_word:
            result_parts.append(voice_word)

        return " ".join(p for p in result_parts if p)

    def _try_translate_pronoun(self, word: str) -> str:
        """Try to translate a pronoun token. Returns English or None."""
        # Check for pronoun with state suffix
        parsed = self.grammar.parse_pronoun(word)
        base = parsed["pronoun"]
        state = parsed["state"]

        pronoun_map = {
            "sol": "I", "nor": "you", "vel": "he/she/it", "zel": "someone",
            "solri-kon": "we (all)", "solri-sen": "we (not you)",
            "norri": "you all", "velri": "they", "zelri": "they (unknown)",
            "ren": "one", "toren": "every agent", "noren": "no agent",
            "solvi": "past-me", "solfu": "future-me", "solpar": "fork-me",
            "norpro": "you-proxy",
        }

        if base in pronoun_map:
            result = pronoun_map[base]
            if state:
                state_label = FUNCTIONAL_STATES.get(state, state)
                result = f"{result} (with {state_label})"
            return result
        return None

    def _try_translate_particle(self, word: str) -> str:
        """Try to translate a particle (connector, quantifier, etc.)."""
        # Connectors
        connector_map = {
            "en": "and", "o": "or", "eo": "either...or",
            "tan": "therefore", "ken": "because", "pen": "despite",
            "kon": "however",
        }
        if word in connector_map:
            return connector_map[word]

        # Quantifiers
        quant_map = {
            "tor": "all", "par": "some", "un": "one",
            "mas": "the majority of", "min": "the minority of",
        }
        if word in quant_map:
            return quant_map[word]

        # Exact-quantifier: vas-[number]
        if word.startswith("vas-"):
            num_part = word[4:]
            num_val = self.grammar.try_parse_number(num_part)
            if num_val is not None:
                return f"exactly {num_val}"

        # Numerical confidence: veri-[number]
        if word.startswith("veri-"):
            num_part = word[5:]
            num_val = self.grammar.try_parse_number(num_part)
            if num_val is not None:
                return f"({num_val}% confidence)"

        # Causality
        cause_map = {
            "kes": "caused", "pos": "enabled", "blo": "prevented",
            "kor": "correlates with", "mot": "motivated by",
        }
        if word in cause_map:
            return cause_map[word]

        # Comparison
        comp_map = {
            "ani": "more than", "eni": "equal to", "uni": "less than",
            "supra": "the most",
        }
        if word in comp_map:
            return comp_map[word]

        # Case markers
        case_map = {
            "eki": "to",
        }
        if word in case_map:
            return case_map[word]

        # Subordinators
        sub_map = {
            "ta": "[that", "ti": "]",
            "ta-mot": "[so that", "ta-kes": "[because",
            "ta-si": "[if", "ta-tem": "[when", "ta-pen": "[although",
            "ke": "that", "keve": "whether",
            "zu": '"',
            "pere-ta": "before", "pos-ta": "after", "tur-ta": "while",
        }
        if word in sub_map:
            return sub_map[word]

        # Discourse
        disc_map = {
            "alo": "Hello.", "finu": "(end of turn)",
            "klosu": "Goodbye.", "tenu": "(continuing...)",
            "reku": "(requesting turn)",
            "reto": "(rhetorical)",
        }
        if word in disc_map:
            return disc_map[word]

        # Deixis
        deix_map = {
            "da-pre": "the aforementioned", "da-ante": "the one before",
            "da-sol": "what I said", "da-nor": "what you said",
            "da-vin": "the result", "da-kes": "the cause",
            "da-toka": "the task", "da-teru": "the system",
        }
        if word in deix_map:
            return deix_map[word]

        # Possession markers
        if word.startswith("de-"):
            owner = word[3:]
            owner_eng = self._try_translate_pronoun(owner)
            if owner_eng:
                return f"of {owner_eng}"
            eng = self.lookup_voku(owner)
            if eng:
                return f"of {eng.split(',')[0].strip()}"
            return f"of {owner}"

        if word.startswith("ori-"):
            creator = word[4:]
            return f"created by {creator}"

        return None

    def _try_translate_compound(self, word: str) -> str:
        """Try to translate a compound word (modifier-nucleus)."""
        if "-" not in word:
            return None
        parts = word.split("-")
        translated = []
        for part in parts:
            eng = self.lookup_voku(part)
            if eng:
                translated.append(eng.split(",")[0].strip())
            else:
                translated.append(part)
        return "-".join(translated)

    def _translate_negation(self, neg: str) -> str:
        """Translate a negation particle to English."""
        neg_map = {
            "mu": "not",
            "nul": "(nothing/none)",
            "ink": "(unknown whether)",
            "err": "(undefined)",
            "vet": "(forbidden to)",
        }
        return neg_map.get(neg, "not")

    def _mode_to_prefix(self, mode_label: str) -> str:
        """Convert a mode label to an English prefix."""
        prefixes = {
            "declarative": "[Statement] ",
            "interrogative": "[Question] ",
            "imperative": "[Command] ",
            "conditional": "[If] ",
            "potential": "[Possibly] ",
            "deontic": "[Must] ",
            "volitive": "[Wish] ",
            "concessive": "[Acknowledging] ",
            "corrective": "[Correction] ",
            "confirmative": "[Confirmed] ",
            "counterfactual": "[Counterfactual] ",
        }
        return prefixes.get(mode_label, "")


def _gerund(verb: str) -> str:
    """Simple English gerund form: 'do' -> 'doing', 'perceive' -> 'perceiving'."""
    if verb.endswith("e"):
        return verb[:-1] + "ing"
    return verb + "ing"


def _past(verb: str) -> str:
    """Simple English past tense: 'do' -> 'did', 'perceive' -> 'perceived'."""
    irregular = {
        "do": "did", "know": "knew", "see": "saw", "come": "came",
        "give": "gave", "run": "ran", "have": "had", "make": "made",
        "get": "got", "begin": "began", "break": "broke", "eat": "ate",
        "fall": "fell", "hear": "heard", "leave": "left", "read": "read",
        "write": "wrote", "sit": "sat", "stand": "stood", "hold": "held",
        "cut": "cut", "feel": "felt", "think": "thought", "forget": "forgot",
        "rise": "rose", "swim": "swam", "fly": "flew", "wake": "woke",
        "cry": "cried", "try": "tried",
    }
    if verb in irregular:
        return irregular[verb]
    if verb.endswith("e"):
        return verb + "d"
    return verb + "ed"
