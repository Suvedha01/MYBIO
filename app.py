import streamlit as st
from datetime import date, timedelta


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="MYBIO — Ancient Wisdom. Modern You.",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# SESSION STATE
# ============================================================

DEFAULTS = {
    "page": "Home",
    "answers": {},
    "question_index": 0,
    "profile_complete": False,
    "ayurvedic_type": "",
    "vata": 0,
    "pitta": 0,
    "kapha": 0,
    "xp": 0,
    "streak": 0,
    "started": False,
    "active_challenge": False,
    "completed_challenges": [],
    "badges": [],
    "last_reward": None,
    "last_completed_date": None,
    "journey_started": False,
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

:root {
    --cream: #FAF7F1;
    --paper: #FFFFFF;
    --paper-soft: #F5F0E7;
    --sage: #B8C9B3;
    --sage-light: #E8EFE4;
    --sage-dark: #647762;
    --peach: #E5B29D;
    --peach-light: #F7E3D9;
    --gold: #C5A46D;
    --gold-light: #F3E8D1;
    --rose: #D99A9A;
    --ink: #29332F;
    --muted: #78817B;
    --border: #E8E1D6;
    --shadow: 0 18px 50px rgba(64, 65, 54, 0.09);
}

html, body, [class*="css"] {
    font-family: "DM Sans", sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 8% 12%, rgba(229,178,157,0.20), transparent 25%),
        radial-gradient(circle at 90% 8%, rgba(184,201,179,0.30), transparent 28%),
        radial-gradient(circle at 80% 80%, rgba(197,164,109,0.12), transparent 25%),
        var(--cream);
    color: var(--ink);
}

/* Remove Streamlit chrome */
#MainMenu {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}

footer {
    visibility: hidden;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main animations */

@keyframes floatSlow {
    0%, 100% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(-14px);
    }
}

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(18px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes pulseSoft {
    0%, 100% {
        box-shadow: 0 0 0 0 rgba(197,164,109,0.12);
    }
    50% {
        box-shadow: 0 0 0 18px rgba(197,164,109,0);
    }
}

@keyframes shimmer {
    0% {
        background-position: -600px 0;
    }
    100% {
        background-position: 600px 0;
    }
}

@keyframes rotateSlow {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}

.fade-up {
    animation: fadeUp 0.7s ease both;
}

.delay-1 {
    animation-delay: 0.12s;
}

.delay-2 {
    animation-delay: 0.24s;
}

.delay-3 {
    animation-delay: 0.36s;
}


/* ============================================================
   BRAND
   ============================================================ */

.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 1.5rem;
}

.brand-symbol {
    width: 44px;
    height: 44px;
    border-radius: 14px;
    background: linear-gradient(135deg, var(--sage), var(--peach));
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    color: white;
    box-shadow: 0 8px 25px rgba(99, 112, 94, 0.18);
    animation: floatSlow 4s ease-in-out infinite;
}

.brand-name {
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 0.16em;
    color: var(--ink);
}

.brand-sub {
    font-size: 10px;
    letter-spacing: 0.18em;
    color: var(--muted);
    margin-top: 2px;
}


/* ============================================================
   NAVIGATION
   ============================================================ */

.nav-wrap {
    background: rgba(255,255,255,0.72);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(232,225,214,0.9);
    border-radius: 22px;
    padding: 8px;
    margin-bottom: 2.4rem;
    box-shadow: 0 10px 30px rgba(50,50,40,0.05);
}

.stButton > button {
    border-radius: 14px !important;
    border: 1px solid transparent !important;
    background: transparent !important;
    color: var(--muted) !important;
    font-weight: 600 !important;
    transition: all 0.25s ease !important;
    min-height: 42px;
}

.stButton > button:hover {
    transform: translateY(-2px);
    background: var(--sage-light) !important;
    color: var(--ink) !important;
    border-color: transparent !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(
        135deg,
        var(--sage-dark),
        #81947B
    ) !important;
    color: white !important;
    box-shadow: 0 10px 24px rgba(100,119,98,0.22) !important;
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 14px 30px rgba(100,119,98,0.28) !important;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    position: relative;
    overflow: hidden;
    min-height: 530px;
    border-radius: 38px;
    padding: 70px 70px;
    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.94),
            rgba(244,239,228,0.94)
        );
    border: 1px solid var(--border);
    box-shadow: var(--shadow);
    animation: fadeUp 0.8s ease both;
}

.hero::before {
    content: "";
    position: absolute;
    width: 330px;
    height: 330px;
    border-radius: 50%;
    background: rgba(184,201,179,0.34);
    right: -100px;
    top: -100px;
    animation: floatSlow 6s ease-in-out infinite;
}

.hero::after {
    content: "";
    position: absolute;
    width: 220px;
    height: 220px;
    border-radius: 50%;
    background: rgba(229,178,157,0.20);
    left: -80px;
    bottom: -80px;
    animation: floatSlow 7s ease-in-out infinite reverse;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 760px;
}

.eyebrow {
    display: inline-block;
    padding: 9px 16px;
    border-radius: 50px;
    background: var(--sage-light);
    color: var(--sage-dark);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.16em;
    margin-bottom: 24px;
}

.hero h1 {
    font-family: "Playfair Display", serif;
    font-size: clamp(48px, 6vw, 82px);
    line-height: 0.98;
    margin: 0;
    color: var(--ink);
    letter-spacing: -0.04em;
}

.hero h1 span {
    color: var(--sage-dark);
    font-style: italic;
}

.hero p {
    max-width: 650px;
    font-size: 18px;
    line-height: 1.8;
    color: var(--muted);
    margin-top: 28px;
}

.tagline {
    margin-top: 25px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: var(--gold);
}

.orbit {
    position: absolute;
    right: 8%;
    bottom: 15%;
    width: 190px;
    height: 190px;
    border: 1px solid rgba(100,119,98,0.25);
    border-radius: 50%;
    animation: rotateSlow 18s linear infinite;
}

.orbit::before {
    content: "";
    position: absolute;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: var(--peach);
    top: 8px;
    left: 50%;
    box-shadow: 0 0 25px rgba(229,178,157,0.5);
}


/* ============================================================
   SECTION HEADINGS
   ============================================================ */

.section-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 8px;
}

.section-title {
    font-family: "Playfair Display", serif;
    font-size: 38px;
    color: var(--ink);
    margin-bottom: 8px;
}

.section-description {
    color: var(--muted);
    line-height: 1.7;
    margin-bottom: 25px;
}


/* ============================================================
   FEATURE CARDS
   ============================================================ */

.feature-card {
    background: rgba(255,255,255,0.88);
    border: 1px solid var(--border);
    border-radius: 25px;
    padding: 28px;
    min-height: 200px;
    box-shadow: 0 12px 35px rgba(60,60,50,0.06);
    transition: all 0.3s ease;
    animation: fadeUp 0.7s ease both;
}

.feature-card:hover {
    transform: translateY(-7px);
    box-shadow: 0 22px 50px rgba(60,60,50,0.11);
}

.feature-icon {
    font-size: 28px;
    margin-bottom: 20px;
}

.feature-card h3 {
    font-family: "Playfair Display", serif;
    font-size: 22px;
    margin-bottom: 10px;
}

.feature-card p {
    color: var(--muted);
    line-height: 1.65;
}


/* ============================================================
   JOURNEY
   ============================================================ */

.journey-shell {
    background: rgba(255,255,255,0.86);
    border: 1px solid var(--border);
    border-radius: 32px;
    padding: 42px;
    box-shadow: var(--shadow);
    animation: fadeUp 0.6s ease both;
}

.step-number {
    color: var(--gold);
    font-weight: 700;
    font-size: 12px;
    letter-spacing: 0.14em;
}

.question-title {
    font-family: "Playfair Display", serif;
    font-size: clamp(30px, 4vw, 46px);
    line-height: 1.15;
    margin: 15px 0 12px;
    color: var(--ink);
}

.question-help {
    color: var(--muted);
    line-height: 1.7;
    margin-bottom: 30px;
}

.progress-track {
    height: 7px;
    background: #EAE5DC;
    border-radius: 20px;
    overflow: hidden;
    margin: 16px 0 35px;
}

.progress-fill {
    height: 100%;
    border-radius: 20px;
    background: linear-gradient(
        90deg,
        var(--sage-dark),
        var(--gold),
        var(--peach)
    );
    background-size: 200% 100%;
    animation: shimmer 3s linear infinite;
    transition: width 0.5s ease;
}


/* ============================================================
   ANSWER CARDS
   ============================================================ */

.answer-card {
    background: white;
    border: 1.5px solid var(--border);
    border-radius: 20px;
    padding: 18px 20px;
    margin-bottom: 10px;
    transition: all 0.25s ease;
}

.answer-card:hover {
    border-color: var(--sage);
    transform: translateX(4px);
    box-shadow: 0 10px 25px rgba(60,60,50,0.06);
}

.answer-card.selected {
    border-color: var(--sage-dark);
    background: var(--sage-light);
    box-shadow: 0 10px 25px rgba(100,119,98,0.12);
}

.answer-title {
    font-weight: 700;
    color: var(--ink);
}

.answer-description {
    font-size: 13px;
    color: var(--muted);
    margin-top: 4px;
}


/* ============================================================
   INPUTS
   ============================================================ */

div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input {
    background: white !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    color: var(--ink) !important;
}

div[data-testid="stNumberInput"] input:focus,
div[data-testid="stTextInput"] input:focus {
    border-color: var(--sage-dark) !important;
    box-shadow: 0 0 0 3px rgba(100,119,98,0.10) !important;
}


/* ============================================================
   DASHBOARD
   ============================================================ */

.metric-card {
    background: rgba(255,255,255,0.9);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 25px;
    min-height: 145px;
    box-shadow: 0 12px 35px rgba(60,60,50,0.06);
    transition: all 0.3s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
}

.metric-icon {
    font-size: 25px;
}

.metric-label {
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin-top: 12px;
}

.metric-value {
    font-family: "Playfair Display", serif;
    font-size: 31px;
    color: var(--ink);
    margin-top: 4px;
}


/* ============================================================
   RESULT CARD
   ============================================================ */

.result-card {
    background:
        linear-gradient(
            135deg,
            rgba(232,239,228,0.92),
            rgba(247,227,217,0.75)
        );
    border: 1px solid rgba(184,201,179,0.7);
    border-radius: 32px;
    padding: 40px;
    text-align: center;
    box-shadow: var(--shadow);
    animation: fadeUp 0.7s ease both;
}

.result-type {
    font-family: "Playfair Display", serif;
    font-size: 44px;
    color: var(--sage-dark);
}

.result-small {
    color: var(--muted);
    line-height: 1.7;
    max-width: 650px;
    margin: auto;
}


/* ============================================================
   CHALLENGE
   ============================================================ */

.challenge-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 32px;
    padding: 42px;
    box-shadow: var(--shadow);
    animation: fadeUp 0.7s ease both;
}

.challenge-number {
    font-size: 11px;
    font-weight: 700;
    color: var(--gold);
    letter-spacing: 0.16em;
}

.challenge-title {
    font-family: "Playfair Display", serif;
    font-size: 43px;
    margin: 12px 0;
}

.challenge-description {
    font-size: 17px;
    line-height: 1.8;
    color: var(--muted);
}

.challenge-purpose {
    margin-top: 25px;
    background: var(--paper-soft);
    border-radius: 18px;
    padding: 20px;
    color: var(--ink);
}


/* ============================================================
   REWARD
   ============================================================ */

.reward-card {
    background:
        radial-gradient(
            circle at top right,
            rgba(197,164,109,0.30),
            transparent 35%
        ),
        white;
    border: 1px solid var(--gold-light);
    border-radius: 30px;
    padding: 42px;
    text-align: center;
    box-shadow: 0 20px 55px rgba(120,95,50,0.12);
    animation: fadeUp 0.7s ease both;
}

.badge {
    display: inline-flex;
    width: 82px;
    height: 82px;
    border-radius: 50%;
    align-items: center;
    justify-content: center;
    background: var(--gold-light);
    font-size: 36px;
    margin-bottom: 18px;
    animation: pulseSoft 2.5s infinite;
}

.reward-title {
    font-family: "Playfair Display", serif;
    font-size: 34px;
}

.reward-xp {
    font-size: 18px;
    color: var(--gold);
    font-weight: 700;
    margin-top: 8px;
}


/* ============================================================
   BADGES
   ============================================================ */

.badge-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 24px;
    text-align: center;
    min-height: 160px;
    transition: all 0.3s ease;
}

.badge-card:hover {
    transform: translateY(-5px);
}

.badge-icon {
    font-size: 35px;
    margin-bottom: 10px;
}

.badge-name {
    font-weight: 700;
}

.badge-muted {
    color: var(--muted);
    font-size: 12px;
}


/* ============================================================
   EMPTY STATE
   ============================================================ */

.empty-state {
    text-align: center;
    background: rgba(255,255,255,0.7);
    border: 1px dashed #D9D1C4;
    border-radius: 32px;
    padding: 70px 35px;
    animation: fadeUp 0.7s ease both;
}

.empty-symbol {
    font-size: 48px;
    margin-bottom: 20px;
    animation: floatSlow 4s ease-in-out infinite;
}

.empty-state h2 {
    font-family: "Playfair Display", serif;
    font-size: 34px;
}

.empty-state p {
    color: var(--muted);
    max-width: 560px;
    margin: 12px auto 25px;
    line-height: 1.7;
}


/* ============================================================
   STREAK
   ============================================================ */

.streak-card {
    background:
        linear-gradient(
            135deg,
            #F7E3D9,
            #F3E8D1
        );
    border-radius: 30px;
    padding: 35px;
    box-shadow: var(--shadow);
}

.streak-number {
    font-family: "Playfair Display", serif;
    font-size: 68px;
    line-height: 1;
}

.day-pill {
    background: white;
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 14px 8px;
    text-align: center;
}

.day-pill.active {
    background: var(--sage-light);
    border-color: var(--sage);
}

.day-name {
    font-size: 11px;
    color: var(--muted);
}

.day-dot {
    font-size: 20px;
    margin-top: 7px;
}


/* ============================================================
   FOOTER
   ============================================================ */

.footer {
    text-align: center;
    margin-top: 80px;
    padding: 30px 0;
    border-top: 1px solid var(--border);
    color: var(--muted);
    font-size: 12px;
    letter-spacing: 0.05em;
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HELPERS
# ============================================================

def go_to(page):
    st.session_state.page = page
    st.rerun()


def bmi_value():
    height = st.session_state.answers.get("height", 0)
    weight = st.session_state.answers.get("weight", 0)

    if height and weight and height > 0:
        height_m = height / 100
        return round(weight / (height_m ** 2), 1)

    return None


def calculate_type():
    scores = {
        "Vata": st.session_state.vata,
        "Pitta": st.session_state.pitta,
        "Kapha": st.session_state.kapha,
    }

    ordered = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    first = ordered[0]
    second = ordered[1]

    if first[1] == 0:
        return "Balanced"

    difference = first[1] - second[1]

    if difference <= 1:
        return f"{first[0]}–{second[0]}"

    return first[0]


def calculate_dosha_scores():
    answers = st.session_state.answers

    vata = 0
    pitta = 0
    kapha = 0

    mappings = {
        "build": {
            "Lean / light": ("vata",),
            "Medium / athletic": ("pitta",),
            "Broad / solid": ("kapha",),
        },
        "appetite": {
            "Irregular": ("vata",),
            "Strong and regular": ("pitta",),
            "Steady and moderate": ("kapha",),
        },
        "digestion": {
            "Variable": ("vata",),
            "Fast": ("pitta",),
            "Slow and steady": ("kapha",),
        },
        "weather": {
            "I prefer warmth": ("vata",),
            "I prefer cool surroundings": ("pitta",),
            "I prefer mild weather": ("kapha",),
        },
        "energy": {
            "Comes in bursts": ("vata",),
            "High and focused": ("pitta",),
            "Calm and sustained": ("kapha",),
        },
        "sleep_natural": {
            "Light / easily disturbed": ("vata",),
            "Moderate": ("pitta",),
            "Deep / long": ("kapha",),
        },
        "temperament": {
            "Creative and spontaneous": ("vata",),
            "Driven and decisive": ("pitta",),
            "Patient and calm": ("kapha",),
        },
        "weight_response": {
            "Difficult to gain": ("vata",),
            "Changes relatively easily": ("pitta",),
            "Easy to gain": ("kapha",),
        },
        "routine": {
            "I prefer flexibility": ("vata",),
            "I like structure": ("pitta",),
            "I enjoy consistency": ("kapha",),
        },
    }

    for key, options in mappings.items():
        value = answers.get(key)

        if value in options:
            dosha = options[value][0]

            if dosha == "vata":
                vata += 1
            elif dosha == "pitta":
                pitta += 1
            elif dosha == "kapha":
                kapha += 1

    st.session_state.vata = vata
    st.session_state.pitta = pitta
    st.session_state.kapha = kapha
    st.session_state.ayurvedic_type = calculate_type()


def complete_profile():
    calculate_dosha_scores()

    st.session_state.profile_complete = True
    st.session_state.journey_started = True

    if st.session_state.xp < 100:
        st.session_state.xp = 100

    if st.session_state.streak == 0:
        st.session_state.streak = 1

    go_to("Ayurvedic Body Type")


# ============================================================
# QUESTIONNAIRE
# ============================================================

QUESTIONS = [
    {
        "key": "age",
        "section": "Your foundation",
        "question": "Let's begin with the basics.",
        "description": "A few simple details help shape a more relevant wellness journey.",
        "type": "number",
        "label": "Age",
        "min": 13,
        "max": 100,
        "default": 20,
        "unit": "years",
    },
    {
        "key": "sex",
        "section": "Your foundation",
        "question": "How would you like your profile tailored?",
        "description": "Choose the option that feels most comfortable.",
        "type": "choice",
        "options": [
            "Female",
            "Male",
            "Prefer not to say",
        ],
    },
    {
        "key": "height",
        "section": "Your foundation",
        "question": "How tall are you?",
        "description": "An approximate value is completely fine.",
        "type": "number",
        "label": "Height",
        "min": 100,
        "max": 230,
        "default": 165,
        "unit": "cm",
    },
    {
        "key": "weight",
        "section": "Your foundation",
        "question": "What is your approximate weight?",
        "description": "Use your current approximate weight.",
        "type": "number",
        "label": "Weight",
        "min": 25,
        "max": 250,
        "default": 60,
        "unit": "kg",
    },
    {
        "key": "goal",
        "section": "Your intention",
        "question": "What would you most like to improve?",
        "description": "Choose the direction that matters most to you right now.",
        "type": "choice",
        "options": [
            "Energy and vitality",
            "Better sleep",
            "Movement and fitness",
            "Nutrition and eating habits",
            "Stress and calm",
            "Overall balance",
        ],
    },
    {
        "key": "activity",
        "section": "Your intention",
        "question": "How active is your usual day?",
        "description": "Think about an ordinary week rather than your best week.",
        "type": "choice",
        "options": [
            "Mostly seated",
            "Lightly active",
            "Moderately active",
            "Very active",
        ],
    },
    {
        "key": "build",
        "section": "Your natural tendencies",
        "question": "Which description feels closest to your natural build?",
        "description": "There is no right or wrong answer.",
        "type": "choice",
        "options": [
            "Lean / light",
            "Medium / athletic",
            "Broad / solid",
        ],
    },
    {
        "key": "appetite",
        "section": "Your natural tendencies",
        "question": "How does your appetite usually behave?",
        "description": "Think about your normal pattern.",
        "type": "choice",
        "options": [
            "Irregular",
            "Strong and regular",
            "Steady and moderate",
        ],
    },
    {
        "key": "digestion",
        "section": "Your natural tendencies",
        "question": "How would you describe your digestion?",
        "description": "Choose the pattern that sounds most familiar.",
        "type": "choice",
        "options": [
            "Variable",
            "Fast",
            "Slow and steady",
        ],
    },
    {
        "key": "weather",
        "section": "Your natural tendencies",
        "question": "Which surroundings usually feel most comfortable?",
        "description": "Notice what your body naturally prefers.",
        "type": "choice",
        "options": [
            "I prefer warmth",
            "I prefer cool surroundings",
            "I prefer mild weather",
        ],
    },
    {
        "key": "energy",
        "section": "Your natural tendencies",
        "question": "How does your energy tend to move through the day?",
        "description": "Think about your natural rhythm.",
        "type": "choice",
        "options": [
            "Comes in bursts",
            "High and focused",
            "Calm and sustained",
        ],
    },
    {
        "key": "sleep_natural",
        "section": "Your natural tendencies",
        "question": "What is your natural sleep pattern?",
        "description": "Before considering your current schedule, think about what feels natural.",
        "type": "choice",
        "options": [
            "Light / easily disturbed",
            "Moderate",
            "Deep / long",
        ],
    },
    {
        "key": "temperament",
        "section": "Your natural tendencies",
        "question": "Which temperament sounds most like you?",
        "description": "Pick the description you identify with most.",
        "type": "choice",
        "options": [
            "Creative and spontaneous",
            "Driven and decisive",
            "Patient and calm",
        ],
    },
    {
        "key": "weight_response",
        "section": "Your natural tendencies",
        "question": "How does your weight tend to respond to changes in routine?",
        "description": "Choose the closest pattern.",
        "type": "choice",
        "options": [
            "Difficult to gain",
            "Changes relatively easily",
            "Easy to gain",
        ],
    },
    {
        "key": "routine",
        "section": "Your natural tendencies",
        "question": "What kind of routine feels most natural?",
        "description": "Your answer helps us understand your preferred rhythm.",
        "type": "choice",
        "options": [
            "I prefer flexibility",
            "I like structure",
            "I enjoy consistency",
        ],
    },
    {
        "key": "condition",
        "section": "Your health context",
        "question": "Is there anything about your health you want to keep in mind?",
        "description": "This is optional and is used only to make suggestions more mindful.",
        "type": "choice",
        "options": [
            "Nothing specific",
            "A long-term health concern",
            "Something I am currently monitoring",
            "Prefer not to say",
        ],
    },
    {
        "key": "medication",
        "section": "Your health context",
        "question": "Are you currently taking regular medication?",
        "description": "This is optional.",
        "type": "choice",
        "options": [
            "No",
            "Yes",
            "Prefer not to say",
        ],
    },
    {
        "key": "allergy",
        "section": "Your health context",
        "question": "Do you have any known food allergies or sensitivities?",
        "description": "Choose the closest option.",
        "type": "choice",
        "options": [
            "No known allergies",
            "Yes",
            "Not sure",
            "Prefer not to say",
        ],
    },
    {
        "key": "other_health",
        "section": "Your health context",
        "question": "Is there anything else you'd like to keep in mind?",
        "description": "You can keep this simple.",
        "type": "choice",
        "options": [
            "Nothing else",
            "Recovery / rest",
            "Digestive comfort",
            "Stress management",
            "Prefer not to say",
        ],
    },
    {
        "key": "diet",
        "section": "Your nourishment",
        "question": "How would you describe your usual food pattern?",
        "description": "Choose what best represents most of your meals.",
        "type": "choice",
        "options": [
            "Mostly vegetarian",
            "Vegetarian with occasional exceptions",
            "Mixed diet",
            "Prefer not to say",
        ],
    },
    {
        "key": "meals",
        "section": "Your nourishment",
        "question": "How regular are your meals?",
        "description": "Think about your normal weekdays.",
        "type": "choice",
        "options": [
            "Very irregular",
            "Somewhat irregular",
            "Mostly regular",
            "Very regular",
        ],
    },
    {
        "key": "junk",
        "section": "Your nourishment",
        "question": "How often do convenience foods enter your routine?",
        "description": "Be honest — this is about understanding your rhythm, not judging it.",
        "type": "choice",
        "options": [
            "Rarely",
            "Sometimes",
            "Often",
            "Very often",
        ],
    },
    {
        "key": "sugar",
        "section": "Your nourishment",
        "question": "How often do you reach for sweet foods or drinks?",
        "description": "Choose your usual pattern.",
        "type": "choice",
        "options": [
            "Rarely",
            "Sometimes",
            "Often",
            "Daily",
        ],
    },
    {
        "key": "sleep",
        "section": "Your daily rhythm",
        "question": "How much sleep do you usually get?",
        "description": "An approximate number is enough.",
        "type": "number",
        "label": "Sleep",
        "min": 2,
        "max": 14,
        "default": 7,
        "unit": "hours",
    },
    {
        "key": "stress",
        "section": "Your daily rhythm",
        "question": "How would you describe your current stress level?",
        "description": "Think about the past couple of weeks.",
        "type": "choice",
        "options": [
            "Low",
            "Occasional",
            "Moderate",
            "High",
        ],
    },
    {
        "key": "activity_minutes",
        "section": "Your daily rhythm",
        "question": "How much intentional movement do you usually get?",
        "description": "Walking, exercise, yoga, sport — anything counts.",
        "type": "number",
        "label": "Movement",
        "min": 0,
        "max": 300,
        "default": 30,
        "unit": "min/day",
    },
    {
        "key": "screen",
        "section": "Your daily rhythm",
        "question": "How much of your day is spent looking at screens?",
        "description": "Include study, work, entertainment and social media.",
        "type": "choice",
        "options": [
            "Less than 3 hours",
            "3–5 hours",
            "5–8 hours",
            "More than 8 hours",
        ],
    },
    {
        "key": "meal_timing",
        "section": "Your daily rhythm",
        "question": "How predictable are your meal timings?",
        "description": "Consistency can tell us a lot about your everyday rhythm.",
        "type": "choice",
        "options": [
            "Very unpredictable",
            "Somewhat unpredictable",
            "Mostly predictable",
            "Very predictable",
        ],
    },
]


# ============================================================
# NAVIGATION
# ============================================================

PAGES = [
    "Home",
    "Begin Journey",
    "My Wellness",
    "Ayurvedic Body Type",
    "Today's Challenge",
    "My Rhythm",
    "For You",
    "About",
]

st.markdown(
    """
<div class="brand">
    <div class="brand-symbol">✦</div>
    <div>
        <div class="brand-name">MYBIO</div>
        <div class="brand-sub">YOUR RHYTHM · YOUR JOURNEY</div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown('<div class="nav-wrap">', unsafe_allow_html=True)

nav_cols = st.columns(len(PAGES))

for i, page in enumerate(PAGES):
    with nav_cols[i]:
        if st.button(
            page,
            key=f"nav_{page}",
            type="primary" if st.session_state.page == page else "secondary",
            use_container_width=True,
        ):
            go_to(page)

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# HOME
# ============================================================

def home_page():

    st.markdown(
        """
<div class="hero">
    <div class="hero-content">
        <div class="eyebrow">A MORE INTENTIONAL WAY TO KNOW YOURSELF</div>

        <h1>
            Meet the <span>you</span><br>
            within.
        </h1>

        <p>
            MYBIO brings together timeless wellness wisdom and the rhythm
            of modern life to help you understand your patterns,
            build mindful habits and discover small changes that feel
            naturally yours.
        </p>

        <div class="tagline">
            ANCIENT WISDOM · MODERN YOU · INFINITE POSSIBILITIES
        </div>
    </div>

    <div class="orbit"></div>
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button(
        "Begin your journey  →",
        type="primary",
        use_container_width=False,
        key="home_begin",
    ):
        st.session_state.journey_started = True
        go_to("Begin Journey")

    st.write("")
    st.write("")

    st.markdown(
        """
<div class="section-label">THE MYBIO APPROACH</div>
<div class="section-title">Not another wellness checklist.</div>
<div class="section-description">
A gentler way to understand your everyday patterns and turn awareness
into small, meaningful actions.
</div>
""",
        unsafe_allow_html=True,
    )

    cols = st.columns(3)

    cards = [
        (
            "◌",
            "Understand your rhythm",
            "Explore the patterns behind your energy, nourishment, movement, sleep and everyday habits.",
        ),
        (
            "✦",
            "Discover your balance",
            "Explore your Ayurvedic body type through a simple, guided personal journey.",
        ),
        (
            "⌁",
            "Build small habits",
            "Take one intentional step at a time instead of trying to change everything at once.",
        ),
    ]

    for col, (icon, title, text) in zip(cols, cards):
        with col:
            st.markdown(
                f"""
<div class="feature-card">
    <div class="feature-icon">{icon}</div>
    <h3>{title}</h3>
    <p>{text}</p>
</div>
""",
                unsafe_allow_html=True,
            )

    st.write("")
    st.write("")

    st.markdown(
        """
<div class="empty-state">
    <div class="empty-symbol">✧</div>
    <h2>Your story starts with curiosity.</h2>
    <p>
        No perfect routine. No pressure to become someone else.
        Just a little space to understand where you are today.
    </p>
</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# QUESTIONNAIRE
# ============================================================

def journey_page():

    total = len(QUESTIONS)
    index = st.session_state.question_index

    if index >= total:
        index = total - 1
        st.session_state.question_index = index

    q = QUESTIONS[index]
    progress = int(((index + 1) / total) * 100)

    st.markdown(
        """
<div class="section-label">YOUR JOURNEY</div>
<div class="section-title">A few questions. A clearer picture.</div>
<div class="section-description">
There is no perfect answer. Choose what feels most true for you.
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<div class="journey-shell">

<div class="step-number">
    STEP {index + 1:02d} / {total:02d}
</div>

<div class="progress-track">
    <div class="progress-fill" style="width:{progress}%"></div>
</div>

<div style="font-size:11px; color:#C5A46D; font-weight:700; letter-spacing:.14em;">
    {q["section"].upper()}
</div>

<div class="question-title">
    {q["question"]}
</div>

<div class="question-help">
    {q["description"]}
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    current_value = st.session_state.answers.get(q["key"])

    if q["type"] == "number":

        default_value = current_value if current_value is not None else q["default"]

        value = st.number_input(
            q["label"],
            min_value=q["min"],
            max_value=q["max"],
            value=default_value,
            step=1,
            key=f"input_{q['key']}",
        )

        st.session_state.answers[q["key"]] = value

        st.caption(f"Unit: {q['unit']}")

    elif q["type"] == "choice":

        options = q["options"]

        for option_index, option in enumerate(options):

            selected = current_value == option

            if st.button(
                ("✓  " if selected else "") + option,
                key=f"answer_{q['key']}_{option_index}",
                use_container_width=True,
                type="primary" if selected else "secondary",
            ):
                st.session_state.answers[q["key"]] = option
                st.rerun()

    st.write("")
    st.write("")

    selected = st.session_state.answers.get(q["key"])

    nav_left, nav_middle, nav_right = st.columns([1, 2, 1])

    with nav_left:
        if index > 0:
            if st.button(
                "← Back",
                key=f"back_{index}",
                use_container_width=True,
            ):
                st.session_state.question_index -= 1
                st.rerun()

    with nav_right:

        button_label = (
            "Finish journey  →"
            if index == total - 1
            else "Continue  →"
        )

        if selected is not None:

            if st.button(
                button_label,
                key=f"next_{index}",
                type="primary",
                use_container_width=True,
            ):

                if index == total - 1:
                    complete_profile()
                else:
                    st.session_state.question_index += 1
                    st.rerun()

    st.write("")

    if index >= total // 2 and index < total - 1:
        st.markdown(
            """
<div style="
    text-align:center;
    color:#78817B;
    font-size:12px;
    padding:10px;
">
    ✦ You're halfway through. Keep going — your picture is beginning to take shape.
</div>
""",
            unsafe_allow_html=True,
        )


# ============================================================
# MY WELLNESS
# ============================================================

def wellness_page():

    if not st.session_state.profile_complete:

        st.markdown(
            """
<div class="section-label">MY WELLNESS</div>
<div class="section-title">Your space is waiting.</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
<div class="empty-state">
    <div class="empty-symbol">◌</div>
    <h2>Something meaningful is taking shape.</h2>
    <p>
        Complete your journey first. Your wellness space will gradually
        become a reflection of your everyday rhythm.
    </p>
</div>
""",
            unsafe_allow_html=True,
        )

        if st.button(
            "Start discovering  →",
            type="primary",
            key="wellness_start",
        ):
            go_to("Begin Journey")

        return

    bmi = bmi_value()

    st.markdown(
        """
<div class="section-label">YOUR WELLNESS</div>
<div class="section-title">A snapshot of you.</div>
<div class="section-description">
Small signals. Gentle awareness. A place to notice how your everyday choices connect.
</div>
""",
        unsafe_allow_html=True,
    )

    cols = st.columns(4)

    metrics = [
        ("✦", "Current streak", f"{st.session_state.streak} day"),
        ("◇", "XP collected", str(st.session_state.xp)),
        ("◌", "Body type", st.session_state.ayurvedic_type),
        ("⌁", "BMI", str(bmi) if bmi else "—"),
    ]

    for col, (icon, label, value) in zip(cols, metrics):
        with col:
            st.markdown(
                f"""
<div class="metric-card">
    <div class="metric-icon">{icon}</div>
    <div class="metric-label">{label}</div>
    <div class="metric-value">{value}</div>
</div>
""",
                unsafe_allow_html=True,
            )

    st.write("")
    st.write("")

    st.markdown(
        """
<div class="result-card">
    <div class="section-label">YOUR CURRENT DIRECTION</div>
    <div class="result-type">
        Keep noticing.
    </div>
    <div class="result-small">
        Wellness is not a finish line. Your profile is a starting point
        for understanding your rhythm and making small changes that feel sustainable.
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")

    if st.button(
        "Take today's challenge  →",
        type="primary",
        key="wellness_challenge",
    ):
        go_to("Today's Challenge")


# ============================================================
# AYURVEDIC BODY TYPE
# ============================================================

DOSHA_INFO = {
    "Vata": {
        "symbol": "✧",
        "quality": "Light · Creative · Dynamic",
        "description": (
            "Often associated with movement, creativity, flexibility and "
            "changing energy. Consistency and grounding routines may feel supportive."
        ),
    },
    "Pitta": {
        "symbol": "◈",
        "quality": "Focused · Warm · Driven",
        "description": (
            "Often associated with focus, intensity, determination and strong "
            "energy. Balance may come from creating space for cooling and recovery."
        ),
    },
    "Kapha": {
        "symbol": "◌",
        "quality": "Steady · Calm · Grounded",
        "description": (
            "Often associated with steadiness, patience and grounded energy. "
            "Variety and regular movement may help maintain momentum."
        ),
    },
}


def ayurvedic_page():

    if not st.session_state.profile_complete:

        st.markdown(
            """
<div class="section-label">AYURVEDIC BODY TYPE</div>
<div class="section-title">A pattern is waiting to emerge.</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
<div class="empty-state">
    <div class="empty-symbol">✧</div>
    <h2>Your result isn't ready yet.</h2>
    <p>
        Begin your journey and answer a few questions about your natural
        tendencies. Your body-type interpretation will appear when the journey is complete.
    </p>
</div>
""",
            unsafe_allow_html=True,
        )

        if st.button(
            "Discover your body type  →",
            type="primary",
            key="body_start",
        ):
            go_to("Begin Journey")

        return

    body_type = st.session_state.ayurvedic_type

    st.markdown(
        """
<div class="section-label">YOUR AYURVEDIC BODY TYPE</div>
<div class="section-title">A window into your natural rhythm.</div>
<div class="section-description">
Ayurvedic traditions describe three broad patterns of qualities.
Your result is an educational interpretation of the answers you shared.
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<div class="result-card">
    <div style="font-size:42px;">✦</div>
    <div class="section-label">YOUR CURRENT PATTERN</div>
    <div class="result-type">{body_type}</div>
    <div class="result-small">
        Your answers suggest a {body_type} pattern.
        Use this as a lens for reflection rather than a diagnosis.
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")

    cols = st.columns(3)

    for col, (name, info) in zip(cols, DOSHA_INFO.items()):
        with col:
            st.markdown(
                f"""
<div class="feature-card">
    <div class="feature-icon">{info["symbol"]}</div>
    <h3>{name}</h3>
    <div style="
        color:#C5A46D;
        font-size:12px;
        font-weight:700;
        margin-bottom:12px;
    ">
        {info["quality"]}
    </div>
    <p>{info["description"]}</p>
</div>
""",
                unsafe_allow_html=True,
            )

    st.write("")
    st.caption(
        "Educational note: Ayurvedic body-type concepts are traditional wellness concepts "
        "and should not be used to diagnose or treat medical conditions."
    )


# ============================================================
# CHALLENGES
# ============================================================

CHALLENGES = [
    {
        "title": "The Hydration Pause",
        "description": (
            "Take a quiet moment during your day and drink one full glass of water "
            "without rushing through it."
        ),
        "purpose": (
            "A tiny pause can turn an automatic habit into a mindful one."
        ),
        "badge": "💧",
        "badge_name": "Hydration Hero",
        "xp": 20,
    },
    {
        "title": "The Movement Minute",
        "description": (
            "Give yourself ten minutes of intentional movement today. Walk, stretch, "
            "dance or simply move in a way that feels comfortable."
        ),
        "purpose": (
            "Movement doesn't have to be intense to become part of your rhythm."
        ),
        "badge": "🌿",
        "badge_name": "Move With Intention",
        "xp": 25,
    },
    {
        "title": "The Mindful Plate",
        "description": (
            "Choose one meal today and slow down. Put away distractions, notice "
            "the food in front of you and give yourself time to eat."
        ),
        "purpose": (
            "Awareness can change the way an ordinary meal feels."
        ),
        "badge": "🍃",
        "badge_name": "Mindful Nourisher",
        "xp": 25,
    },
    {
        "title": "The Evening Reset",
        "description": (
            "Create twenty quiet minutes before sleep with your main screen away."
        ),
        "purpose": (
            "A gentle transition can help separate the end of the day from the beginning of rest."
        ),
        "badge": "🌙",
        "badge_name": "Evening Guardian",
        "xp": 30,
    },
]


def complete_challenge(index):

    if index not in st.session_state.completed_challenges:

        st.session_state.completed_challenges.append(index)

        challenge = CHALLENGES[index]

        st.session_state.xp += challenge["xp"]

        if st.session_state.last_completed_date != str(date.today()):
            st.session_state.streak += 1
            st.session_state.last_completed_date = str(date.today())

        if challenge["badge_name"] not in st.session_state.badges:
            st.session_state.badges.append(challenge["badge_name"])

        st.session_state.last_reward = {
            "title": challenge["badge_name"],
            "badge": challenge["badge"],
            "xp": challenge["xp"],
        }

    st.session_state.active_challenge = False
    st.rerun()


def challenge_page():

    st.markdown(
        """
<div class="section-label">TODAY'S MOMENT</div>
<div class="section-title">One small move.</div>
<div class="section-description">
Don't change everything. Choose one thing you can actually do today.
</div>
""",
        unsafe_allow_html=True,
    )

    # Show reward AFTER completion.
    if st.session_state.last_reward is not None:

        reward = st.session_state.last_reward

        st.markdown(
            f"""
<div class="reward-card">
    <div class="badge">{reward["badge"]}</div>

    <div class="section-label">YOU DID IT</div>

    <div class="reward-title">
        {reward["title"]}
    </div>

    <div class="reward-xp">
        +{reward["xp"]} XP · Streak {st.session_state.streak} day
    </div>

    <p style="
        color:#78817B;
        line-height:1.7;
        max-width:500px;
        margin:15px auto 0;
    ">
        One small action is still an action.
        Keep going at your own pace.
    </p>
</div>
""",
            unsafe_allow_html=True,
        )

        st.write("")

        if st.button(
            "Continue  →",
            type="primary",
            key="reward_continue",
        ):
            st.session_state.last_reward = None
            st.rerun()

        return

    # Find next challenge.
    next_index = None

    for i in range(len(CHALLENGES)):
        if i not in st.session_state.completed_challenges:
            next_index = i
            break

    if next_index is None:

        st.markdown(
            """
<div class="empty-state">
    <div class="empty-symbol">✦</div>
    <h2>You completed the current collection.</h2>
    <p>
        Your consistency is becoming part of your story.
        Come back as your journey continues.
    </p>
</div>
""",
            unsafe_allow_html=True,
        )

        return

    challenge = CHALLENGES[next_index]

    st.markdown(
        f"""
<div class="challenge-card">

    <div class="challenge-number">
        CHALLENGE {next_index + 1:02d}
    </div>

    <div class="challenge-title">
        {challenge["title"]}
    </div>

    <div class="challenge-description">
        {challenge["description"]}
    </div>

    <div class="challenge-purpose">
        <strong>Why this moment?</strong><br>
        {challenge["purpose"]}
    </div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    if not st.session_state.active_challenge:

        if st.button(
            "Start this challenge  →",
            type="primary",
            key=f"start_challenge_{next_index}",
        ):
            st.session_state.active_challenge = True
            st.rerun()

    else:

        st.markdown(
            """
<div style="
    text-align:center;
    padding:15px;
    color:#647762;
    font-weight:600;
">
    ✦ This moment is yours. Take your time.
</div>
""",
            unsafe_allow_html=True,
        )

        if st.button(
            "I completed it  ✓",
            type="primary",
            key=f"complete_challenge_{next_index}",
        ):
            complete_challenge(next_index)


# ============================================================
# MY RHYTHM
# ============================================================

def rhythm_page():

    st.markdown(
        """
<div class="section-label">MY RHYTHM</div>
<div class="section-title">Consistency, not perfection.</div>
<div class="section-description">
Your streak is a reminder of the moments you've chosen to show up.
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<div class="streak-card">

    <div class="section-label">CURRENT STREAK</div>

    <div class="streak-number">
        {st.session_state.streak}
    </div>

    <div style="
        color:#78817B;
        margin-top:8px;
    ">
        day{"s" if st.session_state.streak != 1 else ""}
    </div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")

    st.markdown(
        """
<div class="section-label">YOUR WEEK</div>
""",
        unsafe_allow_html=True,
    )

    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    cols = st.columns(7)

    active_count = min(st.session_state.streak, 7)

    for i, (col, day_name) in enumerate(zip(cols, days)):
        active = i >= 7 - active_count

        with col:
            st.markdown(
                f"""
<div class="day-pill {"active" if active else ""}">
    <div class="day-name">{day_name}</div>
    <div class="day-dot">{"✦" if active else "·"}</div>
</div>
""",
                unsafe_allow_html=True,
            )

    st.write("")
    st.write("")

    st.markdown(
        """
<div class="section-label">YOUR COLLECTION</div>
<div class="section-title" style="font-size:32px;">
Badges you've earned.
</div>
""",
        unsafe_allow_html=True,
    )

    if not st.session_state.badges:

        st.markdown(
            """
<div class="empty-state" style="padding:45px 25px;">
    <div class="empty-symbol">◇</div>
    <h2>Your first badge is waiting.</h2>
    <p>
        Complete a challenge to begin building your collection.
    </p>
</div>
""",
            unsafe_allow_html=True,
        )

    else:

        earned = []

        for challenge in CHALLENGES:
            if challenge["badge_name"] in st.session_state.badges:
                earned.append(challenge)

        cols = st.columns(min(4, len(earned)))

        for col, challenge in zip(cols, earned):
            with col:
                st.markdown(
                    f"""
<div class="badge-card">
    <div class="badge-icon">{challenge["badge"]}</div>
    <div class="badge-name">{challenge["badge_name"]}</div>
    <div class="badge-muted">Earned</div>
</div>
""",
                    unsafe_allow_html=True,
                )


# ============================================================
# RECOMMENDATIONS
# ============================================================

def recommendations():

    st.markdown(
        """
<div class="section-label">FOR YOU</div>
<div class="section-title">A few gentle nudges.</div>
<div class="section-description">
Suggestions shaped around the rhythm you shared — not a rigid prescription.
</div>
""",
        unsafe_allow_html=True,
    )

    if not st.session_state.profile_complete:

        st.markdown(
            """
<div class="empty-state">
    <div class="empty-symbol">✧</div>
    <h2>There is more to discover.</h2>
    <p>
        Complete your journey and this space will begin to reflect
        the patterns you've shared.
    </p>
</div>
""",
            unsafe_allow_html=True,
        )

        if st.button(
            "Begin discovering  →",
            type="primary",
            key="recommendation_start",
        ):
            go_to("Begin Journey")

        return

    answers = st.session_state.answers
    recommendations_list = []

    sleep = answers.get("sleep")

    if sleep is not None and sleep < 7:
        recommendations_list.append(
            (
                "01",
                "Make room for rest",
                "Try creating a calmer transition into sleep rather than waiting until you're already exhausted.",
                "🌙",
            )
        )

    stress = answers.get("stress")

    if stress in ["Moderate", "High"]:
        recommendations_list.append(
            (
                "02",
                "Create a pause",
                "A short breathing break, walk or quiet moment can give your day a little more space.",
                "◌",
            )
        )

    movement = answers.get("activity_minutes")

    if movement is not None and movement < 30:
        recommendations_list.append(
            (
                "03",
                "Move a little more",
                "Try adding a short walk or stretch session rather than aiming for a large workout immediately.",
                "🌿",
            )
        )

    meal_timing = answers.get("meal_timing")

    if meal_timing in ["Very unpredictable", "Somewhat unpredictable"]:
        recommendations_list.append(
            (
                "04",
                "Find one anchor meal",
                "Choose one meal of the day to keep relatively consistent. One anchor is enough to begin.",
                "🍃",
            )
        )

    if not recommendations_list:
        recommendations_list = [
            (
                "01",
                "Protect your rhythm",
                "Notice which routines already work for you and protect them before adding more changes.",
                "✦",
            ),
            (
                "02",
                "Keep it simple",
                "Choose one small habit and repeat it consistently before adding another.",
                "◇",
            ),
            (
                "03",
                "Notice before changing",
                "Spend a few minutes each day noticing your energy, mood and routines without judging them.",
                "◌",
            ),
        ]

    for number, title, text, icon in recommendations_list:

        st.markdown(
            f"""
<div class="feature-card" style="margin-bottom:15px; min-height:auto;">

    <div style="
        display:flex;
        justify-content:space-between;
        align-items:flex-start;
        gap:20px;
    ">

        <div>
            <div class="section-label">{number}</div>
            <h3>{title}</h3>
            <p>{text}</p>
        </div>

        <div style="
            font-size:34px;
            min-width:50px;
            text-align:center;
        ">
            {icon}
        </div>

    </div>

</div>
""",
            unsafe_allow_html=True,
        )

    st.caption(
        "These suggestions are for general wellness and are not medical advice."
    )


# ============================================================
# ABOUT
# ============================================================

def about_page():

    st.markdown(
        """
<div class="section-label">ABOUT MYBIO</div>

<div class="section-title">
    Ancient wisdom. Modern you.
</div>

<div class="section-description">
    MYBIO is designed around a simple idea:
    understanding yourself can be the beginning of better everyday choices.
</div>
""",
        unsafe_allow_html=True,
    )

    cols = st.columns(2)

    with cols[0]:

        st.markdown(
            """
<div class="feature-card" style="min-height:280px;">

    <div class="feature-icon">✦</div>

    <h3>A reflective journey</h3>

    <p>
        MYBIO asks you to pause and notice your patterns —
        your energy, nourishment, movement, sleep and daily rhythm.
        The goal is not perfection. It is awareness.
    </p>

</div>
""",
            unsafe_allow_html=True,
        )

    with cols[1]:

        st.markdown(
            """
<div class="feature-card" style="min-height:280px;">

    <div class="feature-icon">◌</div>

    <h3>Inspired by tradition</h3>

    <p>
        Ayurvedic concepts are presented as traditional wellness
        perspectives for reflection. They should not replace
        professional medical advice, diagnosis or treatment.
    </p>

</div>
""",
            unsafe_allow_html=True,
        )

    st.write("")
    st.write("")

    st.markdown(
        """
<div class="result-card">

    <div class="section-label">THE MYBIO PHILOSOPHY</div>

    <div class="result-type">
        Small shifts. Deeper balance.
    </div>

    <div class="result-small">
        Your journey doesn't need to look like anyone else's.
        Start where you are. Notice what matters.
        Take the next small step.
    </div>

</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# ROUTER
# ============================================================

if st.session_state.page == "Home":
    home_page()

elif st.session_state.page == "Begin Journey":
    journey_page()

elif st.session_state.page == "My Wellness":
    wellness_page()

elif st.session_state.page == "Ayurvedic Body Type":
    ayurvedic_page()

elif st.session_state.page == "Today's Challenge":
    challenge_page()

elif st.session_state.page == "My Rhythm":
    rhythm_page()

elif st.session_state.page == "For You":
    recommendations()

elif st.session_state.page == "About":
    about_page()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">
    MYBIO &nbsp;·&nbsp;
    ANCIENT WISDOM · MODERN YOU · INFINITE POSSIBILITIES
    <br><br>
    Designed for reflection, everyday wellness and intentional living.
</div>
""",
    unsafe_allow_html=True,
)
