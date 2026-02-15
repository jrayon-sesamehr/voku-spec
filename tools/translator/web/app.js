/**
 * Voku Translator - Web Frontend
 * Mirrors the Python translation logic for client-side use.
 */

let dictionary = null;
let direction = "voku-en"; // or "en-voku"

// --- Morphology constants ---

const EVIDENCE_PREFIXES = [
    ["pe-kon", "conflicting"],
    ["pe-ri", "multiple_sources"],
    ["li-pro", "probabilistic"],
    ["mi-re", "recomputation"],
    ["zo", "observation"],
    ["li", "deduction"],
    ["pe", "external"],
    ["mi", "computation"],
    ["he", "inherited"],
    ["as", "assumed"],
];

const TENSE_PREFIXES = [
    ["te", "past"],
    ["nu", "present"],
    ["fu", "future"],
    ["ko", "atemporal"],
];

const ASPECT_PREFIXES = [
    ["du", "durative"],
    ["fi", "completive"],
    ["re", "iterative"],
    ["ha", "habitual"],
    ["in", "inceptive"],
    ["ze", "cessative"],
];

const EXEC_STATE_PREFIXES = [
    ["refa", "retrying"],
    ["rol", "reverted"],
    ["va", "queued"],
    ["ru", "running"],
    ["pa", "paused"],
    ["fa", "failed"],
];

const CERTAINTY_SUFFIXES = [
    ["en", "probable"],
    ["ul", "uncertain"],
    ["os", "speculative"],
];

const VOICE_SUFFIXES = [
    ["pro", "benefactive"],
    ["pu", "passive"],
    ["se", "reflexive"],
    ["me", "reciprocal"],
    ["fe", "causative"],
];

const MODE_PARTICLES = {
    ka: "declarative", ve: "interrogative", to: "imperative",
    si: "conditional", na: "potential", de: "deontic",
    vo: "volitive", ko: "concessive", re: "corrective", su: "confirmative"
};

const NEGATION_PARTICLES = {
    mu: "simple_negation", nul: "nullity", ink: "unknowing",
    err: "indefinition", vet: "prohibition"
};

const PRONOUNS = new Set([
    "sol", "nor", "vel", "zel",
    "solri-kon", "solri-sen", "norri", "velri", "zelri",
    "ren", "toren", "noren", "solvi", "solfu", "solpar", "norpro"
]);

const FUNCTIONAL_STATES = {
    urgi: "urgency", sati: "satisfaction", nomi: "surprise",
    koli: "conflict", redi: "prepared", limi: "limited", vali: "aligned"
};

const PRONOUN_MAP = {
    sol: "I", nor: "you", vel: "he/she/it", zel: "someone",
    "solri-kon": "we (all)", "solri-sen": "we (not you)",
    norri: "you all", velri: "they", zelri: "they (unknown)",
    ren: "one", toren: "every agent", noren: "no agent",
    solvi: "past-me", solfu: "future-me", solpar: "fork-me",
    norpro: "you-proxy"
};

// --- Lookup tables (built after loading dictionary) ---
let vokuToEng = {};
let engToVoku = {};

// --- Load dictionary ---

async function loadDictionary() {
    try {
        const resp = await fetch("../dictionary.json");
        dictionary = await resp.json();
        buildLookups();
    } catch (e) {
        console.error("Failed to load dictionary:", e);
    }
}

function buildLookups() {
    vokuToEng = {};
    engToVoku = {};
    for (const entry of dictionary.words) {
        vokuToEng[entry.voku] = entry.english;
        for (const eng of entry.english.split(",")) {
            const trimmed = eng.trim().toLowerCase();
            if (trimmed && !engToVoku[trimmed]) {
                engToVoku[trimmed] = entry.voku;
            }
            for (const single of trimmed.split(" ")) {
                const s = single.replace(/[()]/g, "");
                if (s && !engToVoku[s]) {
                    engToVoku[s] = entry.voku;
                }
            }
        }
    }
}

// --- Verb parser ---

function parseVerb(word) {
    const parts = word.split("-");
    const result = {
        evidence: null, tense: null, aspect: null,
        exec_state: null, root: null, certainty: null,
        voice: null, negation: null
    };
    let idx = 0;

    // Negation
    if (idx < parts.length && NEGATION_PARTICLES[parts[idx]]) {
        result.negation = parts[idx];
        idx++;
    }

    // Evidence (two-part first, then single)
    if (idx < parts.length) {
        let found = false;
        if (idx + 1 < parts.length) {
            const twoPart = parts[idx] + "-" + parts[idx + 1];
            for (const [prefix] of EVIDENCE_PREFIXES) {
                if (twoPart === prefix) {
                    result.evidence = prefix;
                    idx += 2;
                    found = true;
                    break;
                }
            }
        }
        if (!found) {
            for (const [prefix] of EVIDENCE_PREFIXES) {
                if (!prefix.includes("-") && parts[idx] === prefix) {
                    result.evidence = prefix;
                    idx++;
                    break;
                }
            }
        }
    }

    // Tense
    if (idx < parts.length) {
        for (const [prefix] of TENSE_PREFIXES) {
            if (parts[idx] === prefix) {
                result.tense = prefix;
                idx++;
                break;
            }
        }
    }

    // Aspect or exec_state
    if (idx < parts.length) {
        let found = false;
        for (const [prefix] of EXEC_STATE_PREFIXES) {
            if (parts[idx] === prefix) {
                result.exec_state = prefix;
                idx++;
                found = true;
                break;
            }
        }
        if (!found) {
            for (const [prefix] of ASPECT_PREFIXES) {
                if (parts[idx] === prefix) {
                    result.aspect = prefix;
                    idx++;
                    break;
                }
            }
        }
    }

    // Root (collect until we hit a known suffix)
    const rootParts = [];
    while (idx < parts.length) {
        const candidate = parts[idx];
        let isSuffix = false;
        for (const [s] of CERTAINTY_SUFFIXES.concat(VOICE_SUFFIXES)) {
            if (candidate === s) { isSuffix = true; break; }
        }
        if (isSuffix && rootParts.length > 0) break;
        rootParts.push(candidate);
        idx++;
    }
    result.root = rootParts.join("-") || null;

    // Certainty
    if (idx < parts.length) {
        for (const [suffix] of CERTAINTY_SUFFIXES) {
            if (parts[idx] === suffix) {
                result.certainty = suffix;
                idx++;
                break;
            }
        }
    }

    // Voice
    if (idx < parts.length) {
        for (const [suffix] of VOICE_SUFFIXES) {
            if (parts[idx] === suffix) {
                result.voice = suffix;
                idx++;
                break;
            }
        }
    }

    return result;
}

// --- English helpers ---

function gerund(verb) {
    if (verb.endsWith("e")) return verb.slice(0, -1) + "ing";
    return verb + "ing";
}

function pastTense(verb) {
    const irregular = {
        do: "did", know: "knew", see: "saw", come: "came",
        give: "gave", run: "ran", have: "had", make: "made",
        get: "got", begin: "began", break: "broke", eat: "ate",
        fall: "fell", hear: "heard", leave: "left", read: "read",
        write: "wrote", sit: "sat", stand: "stood", hold: "held",
        cut: "cut", feel: "felt", think: "thought", forget: "forgot",
        rise: "rose", swim: "swam", fly: "flew", wake: "woke"
    };
    if (irregular[verb]) return irregular[verb];
    if (verb.endsWith("e")) return verb + "d";
    return verb + "ed";
}

function lookupVoku(word) {
    const clean = word.replace(/[.,?!]/g, "").toLowerCase();
    return vokuToEng[clean] || null;
}

// --- Voku -> English ---

function translateVerbComplex(word) {
    const parsed = parseVerb(word);
    const parts = [];

    const evidencePhrases = {
        observation: "(by observation)", deduction: "(by deduction)",
        probabilistic: "(by probability)", external: "(from report)",
        multiple_sources: "(from multiple sources)", conflicting: "(from conflicting sources)",
        computation: "(by computation)", recomputation: "(by recomputation)",
        inherited: "(by training)", assumed: "(by assumption)"
    };

    // Negation
    if (parsed.negation) {
        const negMap = { mu: "not", nul: "(nothing/none)", ink: "(unknown whether)", err: "(undefined)", vet: "(forbidden to)" };
        parts.push(negMap[parsed.negation] || "not");
    }

    // Certainty
    const certMap = { en: "probably", ul: "maybe", os: "speculatively" };
    if (parsed.certainty) parts.push(certMap[parsed.certainty] || "");

    // Root
    const rootEng = lookupVoku(parsed.root || word);
    const rootWord = rootEng ? rootEng.split(",")[0].trim() : (parsed.root || word);

    // Tense
    const tenseWord = { te: "past", fu: "future", ko: "always" }[parsed.tense] || "";

    // Build verb phrase
    if (parsed.aspect === "fi") {
        parts.push(tenseWord === "past" ? "completed" : (tenseWord === "future" ? "will complete" : "completed"));
        parts.push(gerund(rootWord));
    } else if (parsed.aspect === "du") {
        parts.push(tenseWord === "past" ? "was" : (tenseWord === "future" ? "will be" : "is"));
        parts.push(gerund(rootWord));
    } else if (parsed.aspect === "in") {
        parts.push(tenseWord === "past" ? "began to" : (tenseWord === "future" ? "will begin to" : "begins to"));
        parts.push(rootWord);
    } else if (parsed.aspect === "ze") {
        parts.push(tenseWord === "past" ? "stopped" : "stops");
        parts.push(gerund(rootWord));
    } else if (parsed.aspect === "re") {
        parts.push("repeatedly " + (tenseWord === "past" ? pastTense(rootWord) : rootWord));
    } else if (parsed.aspect === "ha") {
        parts.push("habitually " + rootWord + "s");
    } else if (parsed.exec_state) {
        const es = parsed.exec_state;
        if (es === "fa") parts.push((tenseWord === "past" ? "failed to " : "fails to ") + rootWord);
        else if (es === "ru") parts.push("is actively " + gerund(rootWord));
        else if (es === "va") parts.push("has queued " + rootWord);
        else if (es === "pa") parts.push("has paused " + gerund(rootWord));
        else if (es === "refa") parts.push("is retrying " + rootWord);
        else if (es === "rol") parts.push("reverted " + rootWord);
    } else {
        if (tenseWord === "past") parts.push(pastTense(rootWord));
        else if (tenseWord === "future") parts.push("will " + rootWord);
        else if (tenseWord === "always") parts.push("always " + rootWord + "s");
        else parts.push(rootWord);
    }

    // Evidence
    if (parsed.evidence) {
        const evLabel = EVIDENCE_PREFIXES.find(([p]) => p === parsed.evidence);
        if (evLabel) parts.push(evidencePhrases[evLabel[1]] || "");
    }

    // Voice
    const voiceMap = { pu: "(passive)", se: "(self)", me: "(each other)", fe: "(caused)", pro: "(for someone)" };
    if (parsed.voice) parts.push(voiceMap[parsed.voice] || "");

    return parts.filter(Boolean).join(" ");
}

function tryTranslatePronoun(word) {
    let base = word;
    let state = null;
    for (const [suffix, meaning] of Object.entries(FUNCTIONAL_STATES)) {
        if (word.endsWith("-" + suffix)) {
            base = word.slice(0, -(suffix.length + 1));
            state = suffix;
            break;
        }
    }
    if (PRONOUN_MAP[base]) {
        let result = PRONOUN_MAP[base];
        if (state) result += ` (with ${FUNCTIONAL_STATES[state]})`;
        return result;
    }
    if (PRONOUNS.has(base)) return base;
    return null;
}

function tryTranslateParticle(word) {
    const maps = {
        en: "and", o: "or", eo: "either...or", tan: "therefore",
        ken: "because", pen: "despite", kon: "however",
        tor: "all", par: "some", un: "one", mas: "the majority of", min: "the minority of",
        kes: "caused", pos: "enabled", blo: "prevented",
        kor: "correlates with", mot: "motivated by",
        ani: "more than", eni: "equal to", uni: "less than", supra: "the most",
        ta: "[that", ti: "]", "ta-mot": "[so that", "ta-kes": "[because",
        "ta-si": "[if", "ta-tem": "[when", "ta-pen": "[although",
        alo: "Hello.", finu: "(end of turn)", klosu: "Goodbye.",
        tenu: "(continuing...)", reku: "(requesting turn)",
        "da-pre": "the aforementioned", "da-ante": "the one before",
        "da-sol": "what I said", "da-nor": "what you said",
        "da-vin": "the result", "da-kes": "the cause",
        "da-toka": "the task", "da-teru": "the system"
    };
    if (maps[word]) return maps[word];

    // Possession
    if (word.startsWith("de-")) {
        const owner = word.slice(3);
        const ownerEng = tryTranslatePronoun(owner);
        if (ownerEng) return `of ${ownerEng}`;
        const eng = lookupVoku(owner);
        if (eng) return `of ${eng.split(",")[0].trim()}`;
        return `of ${owner}`;
    }
    if (word.startsWith("ori-")) return `created by ${word.slice(4)}`;

    return null;
}

function translateVokuToEnglish(text) {
    const tokens = text.trim().split(/\s+/);
    if (!tokens.length) return "";

    const outputParts = [];
    let idx = 0;

    // Mode particle
    let modeLabel = null;
    const first = tokens[0].replace(/[.,?!]/g, "");
    if (MODE_PARTICLES[first]) {
        modeLabel = MODE_PARTICLES[first];
        idx = 1;
    }

    while (idx < tokens.length) {
        const token = tokens[idx];
        const clean = token.replace(/[.,?!]+$/, "");
        const punct = token.slice(clean.length);

        // Negation
        if (NEGATION_PARTICLES[clean]) {
            const negMap = { mu: "not", nul: "(nothing/none)", ink: "(unknown whether)", err: "(undefined)", vet: "(forbidden to)" };
            outputParts.push(negMap[clean] || "not");
            idx++; continue;
        }

        // Pronoun
        const pronResult = tryTranslatePronoun(clean);
        if (pronResult) {
            outputParts.push(pronResult + punct);
            idx++; continue;
        }

        // Particle
        const partResult = tryTranslateParticle(clean);
        if (partResult) {
            outputParts.push(partResult + punct);
            idx++; continue;
        }

        // Inflected verb
        if (clean.includes("-")) {
            outputParts.push(translateVerbComplex(clean) + punct);
            idx++; continue;
        }

        // Dictionary lookup
        const eng = lookupVoku(clean);
        if (eng) {
            outputParts.push(eng.split(",")[0].trim() + punct);
        } else {
            outputParts.push(`[${clean}]` + punct);
        }
        idx++;
    }

    let result = outputParts.join(" ");

    // Mode prefix
    const modePrefixes = {
        declarative: "", interrogative: "(Question) ", imperative: "(Command) ",
        conditional: "(If) ", potential: "(Possibly) ", deontic: "(Must) ",
        volitive: "(Wish) ", concessive: "(Acknowledging) ",
        corrective: "(Correction) ", confirmative: "(Confirmed) "
    };
    if (modeLabel && modePrefixes[modeLabel]) {
        result = modePrefixes[modeLabel] + result;
    }

    // Capitalize
    if (result) result = result[0].toUpperCase() + result.slice(1);
    return result;
}

// --- English -> Voku ---

function translateEnglishToVoku(text) {
    const stripped = text.trim().replace(/[.?!]+$/, "");
    const tokens = stripped.split(/\s+/);
    if (!tokens.length) return "";

    let mode = "ka";
    if (text.trim().endsWith("?")) mode = "ve";
    else if (text.trim().endsWith("!")) mode = "to";

    const imperative = new Set([
        "do", "execute", "tell", "communicate", "send", "search", "find",
        "create", "make", "help", "open", "close", "give", "come", "go",
        "stop", "wait", "run", "fix", "evaluate"
    ]);
    if (imperative.has(tokens[0].toLowerCase()) && !text.trim().endsWith("?")) mode = "to";

    const skipWords = new Set([
        "the", "a", "an", "is", "are", "was", "were", "am",
        "do", "does", "did", "will", "would", "could", "should",
        "that", "which", "to", "it"
    ]);

    const pronounMap = {
        i: "sol", me: "sol", you: "nor", he: "vel", she: "vel",
        him: "vel", her: "vel", we: "solri-kon", us: "solri-kon",
        they: "velri", them: "velri"
    };

    const commonMap = {
        not: "mu", no: "mu", "don't": "mu", "doesn't": "mu",
        in: "eno", inside: "eno", within: "eno", outside: "eso", out: "eso",
        with: "kono", without: "sino", for: "poro", above: "ano", over: "ano",
        below: "supo", under: "supo", and: "en", or: "o", but: "kon",
        because: "ken", therefore: "tan", despite: "pen",
        if: "si", then: "ta", all: "tor", some: "par", every: "tor",
        new: "novi", old: "omi", true: "veri", false: "fasi",
        fast: "rapi", slow: "leni", big: "vasi", small: "puli",
        good: "vali", bad: "mali"
    };

    const vokuParts = [mode];
    for (const token of tokens) {
        const clean = token.toLowerCase().replace(/[.,?!;:'"]/g, "");
        if (!clean) continue;
        if (skipWords.has(clean)) continue;
        if (pronounMap[clean]) { vokuParts.push(pronounMap[clean]); continue; }
        if (engToVoku[clean]) { vokuParts.push(engToVoku[clean]); continue; }
        if (commonMap[clean]) { vokuParts.push(commonMap[clean]); continue; }
        vokuParts.push(`[${clean}]`);
    }

    let result = vokuParts.join(" ") + ".";
    result = result[0].toUpperCase() + result.slice(1);
    return result;
}

// --- UI ---

function translate() {
    const input = document.getElementById("inputText").value.trim();
    const output = document.getElementById("outputText");
    if (!input) {
        output.textContent = "Translation will appear here...";
        output.classList.add("placeholder");
        return;
    }
    output.classList.remove("placeholder");
    if (direction === "voku-en") {
        output.textContent = translateVokuToEnglish(input);
    } else {
        output.textContent = translateEnglishToVoku(input);
    }
}

function swapDirection() {
    direction = direction === "voku-en" ? "en-voku" : "voku-en";
    document.getElementById("srcLang").textContent = direction === "voku-en" ? "Voku" : "English";
    document.getElementById("tgtLang").textContent = direction === "voku-en" ? "English" : "Voku";

    // Swap text if there's content
    const inputEl = document.getElementById("inputText");
    const outputEl = document.getElementById("outputText");
    if (outputEl.textContent && !outputEl.classList.contains("placeholder")) {
        inputEl.value = outputEl.textContent;
        outputEl.textContent = "Translation will appear here...";
        outputEl.classList.add("placeholder");
    }
}

// --- Init ---

document.addEventListener("DOMContentLoaded", () => {
    loadDictionary();

    document.getElementById("translateBtn").addEventListener("click", translate);
    document.getElementById("swapBtn").addEventListener("click", swapDirection);

    const inputEl = document.getElementById("inputText");
    inputEl.addEventListener("input", () => {
        document.getElementById("charCount").textContent = inputEl.value.length + " characters";
    });

    // Enter key to translate
    inputEl.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
            e.preventDefault();
            translate();
        }
    });

    // Example click handlers
    document.querySelectorAll(".example-item").forEach(item => {
        item.addEventListener("click", () => {
            const text = item.dataset.text;
            const dir = item.dataset.dir;
            if (dir !== direction) swapDirection();
            inputEl.value = text;
            document.getElementById("charCount").textContent = text.length + " characters";
            translate();
        });
    });
});
