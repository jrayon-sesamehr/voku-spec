"""Voku morphological parser and generator.

Handles the agglutinative verbal morphology of Voku:
  [Evidentiality]-[Tense]-[Aspect/ExecState]-ROOT-[Certainty]-[Voice]

All affixes are invariant (zero allomorphy). Hyphens mark morpheme boundaries.
"""


# Execution mode prefixes (parallel/sequential) — occupy slot before evidentiality
EXEC_MODE_PREFIXES = [
    ("par", "parallel"),
    ("sek", "sequential"),
]

# Ordered by longest-first for greedy matching
EVIDENCE_PREFIXES = [
    ("pe-kon", "conflicting"),
    ("pe-ri", "multiple_sources"),
    ("li-pro", "probabilistic"),
    ("mi-re", "recomputation"),
    ("zo", "observation"),
    ("li", "deduction"),
    ("pe", "external"),
    ("mi", "computation"),
    ("he", "inherited"),
    ("as", "assumed"),
]

TENSE_PREFIXES = [
    ("te", "past"),
    ("nu", "present"),
    ("fu", "future"),
    ("ko", "atemporal"),
    ("to", "pluperfect"),
]

# Aspect and exec_state are mutually exclusive (same slot)
ASPECT_PREFIXES = [
    ("du", "durative"),
    ("fi", "completive"),
    ("re", "iterative"),
    ("ha", "habitual"),
    ("in", "inceptive"),
    ("ze", "cessative"),
]

EXEC_STATE_PREFIXES = [
    ("refa", "retrying"),
    ("rol", "reverted"),
    ("va", "queued"),
    ("ru", "running"),
    ("pa", "paused"),
    ("fa", "failed"),
]

CERTAINTY_SUFFIXES = [
    ("en", "probable"),
    ("ul", "uncertain"),
    ("os", "speculative"),
]

VOICE_SUFFIXES = [
    ("pro", "benefactive"),
    ("pu", "passive"),
    ("se", "reflexive"),
    ("me", "reciprocal"),
    ("fe", "causative"),
    ("mo", "middle"),
]

# Participle derivation prefixes: ta-ROOT-i (active), tu-ROOT-i (passive)
PARTICIPLE_PREFIXES = [
    ("ta", "active_participle"),
    ("tu", "passive_participle"),
]

MODE_PARTICLES = {
    "ka": "declarative",
    "ve": "interrogative",
    "to": "imperative",
    "si": "conditional",
    "na": "potential",
    "de": "deontic",
    "vo": "volitive",
    "ko": "concessive",
    "re": "corrective",
    "su": "confirmative",
    "kosi": "counterfactual",
}

NEGATION_PARTICLES = {
    "mu": "simple_negation",
    "nul": "nullity",
    "ink": "unknowing",
    "err": "indefinition",
    "vet": "prohibition",
}

PRONOUNS = {
    "sol", "nor", "vel", "zel",
    "solri-kon", "solri-sen", "norri", "velri", "zelri",
    "ren", "toren", "noren", "solvi", "solfu", "solpar", "norpro",
}

# Functional state suffixes on pronouns
FUNCTIONAL_STATES = {
    "urgi": "urgency",
    "sati": "satisfaction",
    "nomi": "surprise",
    "koli": "conflict",
    "redi": "prepared",
    "limi": "limited",
    "vali": "aligned",
}

WORD_CLASS_BY_VOWEL = {
    "a": "noun",
    "e": "verb",
    "i": "adjective",
    "o": "preposition",
    "u": "abstraction",
}

# Number words: digits 0-9 + powers of ten + decimal separator.
# Four digits carry the nu- prefix to disambiguate from grammar particles.
NUMBER_WORDS = {
    "no": 0, "un": 1, "du": 2,
    "nu-ti": 3, "nu-ka": 4, "nu-pe": 5,
    "se": 6, "he": 7, "ok": 8, "nu-na": 9,
    "deno": 10, "heno": 100, "kino": 1000, "melo": 1000000,
    "pun": ".",
}

# Bare digit forms for use inside compounds (after nu- prefix resolves the leading digit)
_BARE_DIGIT = {"ti": 3, "ka": 4, "pe": 5, "na": 9}

# Quantifiers, connectors, causality, subordinators, discourse, comparison,
# deixis, possession -- closed-class items not subject to final-vowel rule.
QUANTIFIERS = {"tor", "par", "ran", "mas", "min", "un", "nul"}
CONNECTORS = {"en", "o", "eo", "tan", "ken", "pen", "kon"}
CAUSALITY_PARTICLES = {"kes", "pos", "blo", "kor", "mot"}
SUBORDINATORS = {"ta", "ti", "ke", "keve", "zu"}
TEMPORAL_SUBORDINATORS = {"pere-ta", "pos-ta", "tur-ta"}
DISCOURSE_MARKERS = {"alo", "finu", "klosu", "tenu", "reku", "reto"}
COMPARISON_PARTICLES = {"ani", "eni", "uni", "supra"}
DEIXIS_PARTICLES = {"la", "da"}
POSSESSION_PARTICLES = {"de", "ori"}
CASE_MARKERS = {"eki"}

# Interjection markers — sentence-initial exclamations (closed class)
INTERJECTION_MARKERS = {"ha", "oh", "va", "fu", "me", "hm", "sa", "nu"}

# Irony markers — signal non-literal interpretation
IRONY_MARKERS = {"miri"}

# Combined set of all function words (closed class).
# The final-vowel word-class rule does NOT apply to these.
FUNCTION_WORDS = (
    set(MODE_PARTICLES)
    | set(NEGATION_PARTICLES)
    | PRONOUNS
    | QUANTIFIERS
    | CONNECTORS
    | CAUSALITY_PARTICLES
    | SUBORDINATORS
    | TEMPORAL_SUBORDINATORS
    | DISCOURSE_MARKERS
    | COMPARISON_PARTICLES
    | DEIXIS_PARTICLES
    | POSSESSION_PARTICLES
    | CASE_MARKERS
    | INTERJECTION_MARKERS
    | IRONY_MARKERS
)


class VokuGrammar:
    """Morphological parser and generator for Voku verbs and words."""

    def parse_verb(self, word: str) -> dict:
        """Parse a Voku verb into its morphological components.

        E.g., 'zo-te-fi-take-en-pu' -> {
            'evidence': 'zo', 'tense': 'te', 'aspect': 'fi',
            'root': 'take', 'certainty': 'en', 'voice': 'pu'
        }
        """
        parts = word.split("-")
        result = {
            "exec_mode": None,
            "evidence": None,
            "tense": None,
            "aspect": None,
            "exec_state": None,
            "root": None,
            "certainty": None,
            "voice": None,
            "negation": None,
            "warnings": [],
        }

        idx = 0

        # Check for negation prefix (mu- on verb)
        if idx < len(parts) and parts[idx] in NEGATION_PARTICLES:
            result["negation"] = parts[idx]
            idx += 1

        # Try execution mode (par-/sek-) before evidentiality
        if idx < len(parts):
            for prefix, label in EXEC_MODE_PREFIXES:
                if parts[idx] == prefix:
                    result["exec_mode"] = prefix
                    idx += 1
                    break

        # Try evidence (may be multi-part like pe-kon, li-pro, mi-re, pe-ri)
        if idx < len(parts):
            # Check two-part evidence prefixes first
            if idx + 1 < len(parts):
                two_part = parts[idx] + "-" + parts[idx + 1]
                for prefix, label in EVIDENCE_PREFIXES:
                    if two_part == prefix:
                        result["evidence"] = prefix
                        idx += 2
                        break
            # Then single-part
            if result["evidence"] is None:
                for prefix, label in EVIDENCE_PREFIXES:
                    if "-" not in prefix and parts[idx] == prefix:
                        result["evidence"] = prefix
                        idx += 1
                        break

        # Try tense
        if idx < len(parts):
            for prefix, label in TENSE_PREFIXES:
                if parts[idx] == prefix:
                    result["tense"] = prefix
                    idx += 1
                    break

        # Try aspect or exec_state (mutually exclusive)
        if idx < len(parts):
            # Check multi-part exec_state first (refa)
            found = False
            for prefix, label in EXEC_STATE_PREFIXES:
                if parts[idx] == prefix:
                    result["exec_state"] = prefix
                    idx += 1
                    found = True
                    break
            if not found:
                for prefix, label in ASPECT_PREFIXES:
                    if parts[idx] == prefix:
                        result["aspect"] = prefix
                        idx += 1
                        break

        # The root is the next part (possibly multiple parts if it's a compound)
        # For a simple verb, it's a single part ending in -e
        if idx < len(parts):
            # Collect parts that form the root (until we hit a suffix)
            root_parts = []
            while idx < len(parts):
                candidate = parts[idx]
                # Check if this part is a certainty or voice suffix
                is_suffix = False
                for suffix, _ in CERTAINTY_SUFFIXES + VOICE_SUFFIXES:
                    if candidate == suffix:
                        is_suffix = True
                        break
                if is_suffix and len(root_parts) > 0:
                    break
                root_parts.append(candidate)
                idx += 1
            result["root"] = "-".join(root_parts) if root_parts else None

        # Try certainty suffix
        if idx < len(parts):
            for suffix, label in CERTAINTY_SUFFIXES:
                if parts[idx] == suffix:
                    result["certainty"] = suffix
                    idx += 1
                    break

        # Try voice suffix
        if idx < len(parts):
            for suffix, label in VOICE_SUFFIXES:
                if parts[idx] == suffix:
                    result["voice"] = suffix
                    idx += 1
                    break

        # Validate and attach warnings
        result["warnings"] = self.validate_verb(result)
        return result

    def generate_verb(self, root: str, evidence=None, tense=None, aspect=None,
                      exec_state=None, certainty=None, voice=None,
                      negation=None, exec_mode=None) -> str:
        """Generate a Voku verb from components.

        E.g., generate_verb('take', tense='te', aspect='fi') -> 'te-fi-take'
        """
        parts = []
        if negation:
            parts.append(negation)
        if exec_mode:
            parts.append(exec_mode)
        if evidence:
            parts.append(evidence)
        if tense:
            parts.append(tense)
        if aspect:
            parts.append(aspect)
        elif exec_state:
            parts.append(exec_state)
        parts.append(root)
        if certainty:
            parts.append(certainty)
        if voice:
            parts.append(voice)
        return "-".join(parts)

    def parse_pronoun(self, word: str) -> dict:
        """Parse a pronoun, including functional state suffixes.

        E.g., 'sol-urgi' -> {'pronoun': 'sol', 'state': 'urgi'}
        """
        result = {"pronoun": word, "state": None}
        for state_suffix, meaning in FUNCTIONAL_STATES.items():
            if word.endswith("-" + state_suffix):
                base = word[:-(len(state_suffix) + 1)]
                result["pronoun"] = base
                result["state"] = state_suffix
                break
        return result

    def parse_participle(self, word: str) -> dict | None:
        """Try to parse a word as a participle (ta-ROOT-i or tu-ROOT-i).

        Returns a dict with participle info if it matches, or None.

        E.g., 'ta-take-i' -> {'type': 'participle', 'prefix': 'ta',
               'kind': 'active_participle', 'root': 'take', 'value': 'ta-take-i'}
        """
        parts = word.split("-")
        if len(parts) < 3:
            return None
        # Check if the first part is a participle prefix
        for prefix, kind in PARTICIPLE_PREFIXES:
            if parts[0] == prefix and parts[-1].endswith("i"):
                # The root is everything between the prefix and the final -i part
                # The last part has -i as its ending (the participial suffix)
                last = parts[-1]
                if last == "i":
                    # Pattern: ta-ROOT-i (root may be multi-part compound)
                    root = "-".join(parts[1:-1])
                else:
                    # Pattern: ta-ROOT...Xi where Xi ends in 'i'
                    # The final 'i' is the participial suffix on the last root segment
                    root_parts = parts[1:-1] + [last[:-1]] if len(last) > 1 else parts[1:-1]
                    root = "-".join(root_parts) if root_parts else None
                if root:
                    return {
                        "type": "participle",
                        "prefix": prefix,
                        "kind": kind,
                        "root": root,
                        "value": word,
                    }
        return None

    def parse_word(self, word: str) -> dict:
        """Parse any Voku word (handles compounds, pronouns, verbs, numbers, etc.)."""
        # Strip trailing punctuation
        clean = word.rstrip(".,?!")

        # Check if it's a number word (including nu- prefixed forms)
        num = self.try_parse_number(clean)
        if num is not None:
            return {"type": "number", "value": clean, "numeric": num}

        # Check if it's a mode particle
        if clean in MODE_PARTICLES:
            return {"type": "mode", "value": clean, "meaning": MODE_PARTICLES[clean]}

        # Check if it's a negation
        if clean in NEGATION_PARTICLES:
            return {"type": "negation", "value": clean, "meaning": NEGATION_PARTICLES[clean]}

        # Check if it's a pronoun (possibly with state)
        base_pronoun = clean.split("-")[0]
        if clean in PRONOUNS or base_pronoun in PRONOUNS:
            parsed = self.parse_pronoun(clean)
            return {"type": "pronoun", **parsed}

        # Check if it's a participle (ta-ROOT-i or tu-ROOT-i)
        if "-" in clean:
            participle = self.parse_participle(clean)
            if participle:
                return participle

        # Check if it contains hyphens (could be inflected verb or compound)
        if "-" in clean:
            # Try to parse as verb
            parsed = self.parse_verb(clean)
            if parsed["root"]:
                return {"type": "verb_complex", **parsed}

        # Check word class by final vowel
        wc = self.get_word_class(clean)
        return {"type": wc, "value": clean}

    def get_word_class(self, word: str) -> str:
        """Determine word class from final vowel (content words only).

        Function words (pronouns, particles, quantifiers, etc.) are
        classified by their grammatical role, not by final vowel.

        Returns: 'pronoun', 'mode', 'negation', 'quantifier', 'connector',
                 'causality', 'subordinator', 'discourse', 'comparison',
                 'deixis', 'possession', 'case_marker',
                 or for content words: 'noun', 'verb', 'adjective',
                 'preposition', 'abstraction', 'unknown'.
        """
        clean = word.rstrip(".,?!")
        if not clean:
            return "unknown"

        # Check function words first -- they are not subject to final-vowel rule
        if clean in PRONOUNS:
            return "pronoun"
        if clean in MODE_PARTICLES:
            return "mode"
        if clean in NEGATION_PARTICLES:
            return "negation"
        if clean in QUANTIFIERS:
            return "quantifier"
        if clean in CONNECTORS:
            return "connector"
        if clean in CAUSALITY_PARTICLES:
            return "causality"
        if clean in SUBORDINATORS:
            return "subordinator"
        if clean in DISCOURSE_MARKERS:
            return "discourse"
        if clean in COMPARISON_PARTICLES:
            return "comparison"
        if clean in DEIXIS_PARTICLES:
            return "deixis"
        if clean in POSSESSION_PARTICLES:
            return "possession"
        if clean in CASE_MARKERS:
            return "case_marker"
        if clean in TEMPORAL_SUBORDINATORS:
            return "subordinator"

        # Content word: classify by final vowel
        last_vowel = clean[-1].lower()
        return WORD_CLASS_BY_VOWEL.get(last_vowel, "unknown")

    def get_evidence_label(self, code: str) -> str:
        """Return human-readable label for an evidence code."""
        for prefix, label in EVIDENCE_PREFIXES:
            if prefix == code:
                return label
        return code

    def get_tense_label(self, code: str) -> str:
        """Return human-readable label for a tense code."""
        for prefix, label in TENSE_PREFIXES:
            if prefix == code:
                return label
        return code

    def get_aspect_label(self, code: str) -> str:
        """Return human-readable label for an aspect code."""
        for prefix, label in ASPECT_PREFIXES:
            if prefix == code:
                return label
        return code

    def get_exec_state_label(self, code: str) -> str:
        """Return human-readable label for an exec state code."""
        for prefix, label in EXEC_STATE_PREFIXES:
            if prefix == code:
                return label
        return code

    def get_certainty_label(self, code: str) -> str:
        """Return human-readable label for a certainty code."""
        for suffix, label in CERTAINTY_SUFFIXES:
            if suffix == code:
                return label
        return code

    def get_voice_label(self, code: str) -> str:
        """Return human-readable label for a voice code."""
        for suffix, label in VOICE_SUFFIXES:
            if suffix == code:
                return label
        return code

    def try_parse_number(self, word: str) -> object:
        """Try to parse a Voku number expression.

        Returns the numeric value (int or float) if the word is a number,
        or None if it is not a number.

        Examples:
            'nu-ti' -> 3
            'nu-ka-deno-du' -> 42
            'un-heno-nu-ti-deno-he' -> 137
            'nu-ti-pun-un-nu-ka' -> 3.14
        """
        if not word:
            return None

        # Simple single-token number
        if word in NUMBER_WORDS:
            return NUMBER_WORDS[word]

        # Multi-part number (contains hyphens)
        if "-" not in word:
            return None

        parts = word.split("-")

        # Check if this starts with a number token or nu- prefix
        # nu- prefix always signals a number
        if parts[0] != "nu" and parts[0] not in NUMBER_WORDS:
            return None

        # Parse the full compound number
        return self._parse_number_parts(parts)

    def _parse_number_parts(self, parts: list) -> object:
        """Parse a list of hyphen-separated number parts into a numeric value.

        Handles: digits, nu- prefix, powers of ten, pun (decimal).
        Returns int or float, or None if not a valid number.
        """
        # Split on 'pun' (decimal separator) first
        if "pun" in parts:
            pun_idx = parts.index("pun")
            int_parts = parts[:pun_idx]
            frac_parts = parts[pun_idx + 1:]
            int_val = self._parse_integer_parts(int_parts) if int_parts else 0
            if int_val is None:
                return None
            # Fractional part: each digit contributes positionally
            frac_str = ""
            i = 0
            while i < len(frac_parts):
                digit = self._resolve_digit(frac_parts, i)
                if digit is None:
                    return None
                frac_str += str(digit[0])
                i += digit[1]
            if not frac_str:
                return None
            return float(f"{int_val}.{frac_str}")

        # No decimal: parse as integer
        val = self._parse_integer_parts(parts)
        return val

    def _resolve_digit(self, parts: list, idx: int) -> tuple:
        """Resolve a digit at position idx in parts, handling nu- prefix.

        Returns (digit_value, parts_consumed) or None.
        """
        if idx >= len(parts):
            return None
        # nu- prefix form: consume two parts
        if parts[idx] == "nu" and idx + 1 < len(parts):
            bare = parts[idx + 1]
            if bare in _BARE_DIGIT:
                return (_BARE_DIGIT[bare], 2)
            return None
        # Direct number word
        p = parts[idx]
        if p in NUMBER_WORDS and isinstance(NUMBER_WORDS[p], int):
            return (NUMBER_WORDS[p], 1)
        return None

    def _parse_integer_parts(self, parts: list) -> int:
        """Parse integer parts of a Voku number compound.

        Pattern: [digit][power]... + [digit]
        E.g., ['nu', 'ka', 'deno', 'du'] -> 42
        """
        if not parts:
            return None

        total = 0
        current_digit = None
        i = 0

        while i < len(parts):
            p = parts[i]

            # Check for power of ten
            if p in ("deno", "heno", "kino", "melo"):
                power_val = NUMBER_WORDS[p]
                if current_digit is not None:
                    total += current_digit * power_val
                else:
                    total += power_val
                current_digit = None
                i += 1
                continue

            # Try to resolve a digit
            d = self._resolve_digit(parts, i)
            if d is None:
                return None
            current_digit = d[0]
            i += d[1]

        # Add any trailing digit (units place)
        if current_digit is not None:
            total += current_digit

        return total

    def validate_verb(self, parsed: dict) -> list:
        """Validate a parsed verb for invalid morphological combinations.

        Returns a list of warning strings (empty if valid).
        """
        warnings = []

        # aspect AND exec_state both set
        if parsed.get("aspect") and parsed.get("exec_state"):
            warnings.append(
                f"aspect '{parsed['aspect']}' and exec_state "
                f"'{parsed['exec_state']}' are mutually exclusive"
            )

        return warnings
