import streamlit as st
import math
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="MYBIO — Ancient Wisdom. Modern You.",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

defaults = {
    "page": "Home",
    "profile_complete": False,
    "answers": {},
    "question_index": 0,
    "vata": 0,
    "pitta": 0,
    "kapha": 0,
    "ayurvedic_type": "",
    "streak": 0,
    "xp": 0,
    "water": 0,
    "steps": 0,
    "sleep": 0,
    "active_challenge": 0,
    "completed_challenges": [],
    "started": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

:root {
    --cream: #F7F4EC;
    --paper: #FFFDF8;
    --sage: #A9B9A0;
    --sage-light: #DCE5D7;
    --teal: #37665B;
    --teal-dark: #244D45;
    --gold: #C9A96E;
    --gold-light: #E9D8B5;
    --brown: #6F6253;
    --text: #25352F;
    --muted: #718078;
    --white: #FFFFFF;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 5% 5%, rgba(201,169,110,0.12), transparent 25%),
        radial-gradient(circle at 95% 15%, rgba(169,185,160,0.18), transparent 28%),
        linear-gradient(135deg, #F7F4EC 0%, #FBFAF5 48%, #EEF2EA 100%);
    color: var(--text);
}

/* Remove Streamlit top spacing */
.block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 1400px;
}

/* Hide default menu/footer */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* =========================================================
   FLOATING BACKGROUND
   ========================================================= */

.bg-orb-one,
.bg-orb-two,
.bg-orb-three {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
}

.bg-orb-one {
    width: 280px;
    height: 280px;
    top: 12%;
    left: -100px;
    background: rgba(169,185,160,0.16);
    filter: blur(3px);
    animation: driftOne 12s ease-in-out infinite alternate;
}

.bg-orb-two {
    width: 220px;
    height: 220px;
    right: -80px;
    bottom: 10%;
    background: rgba(201,169,110,0.10);
    filter: blur(4px);
    animation: driftTwo 15s ease-in-out infinite alternate;
}

.bg-orb-three {
    width: 100px;
    height: 100px;
    top: 45%;
    right: 18%;
    background: rgba(55,102,91,0.06);
    animation: float 7s ease-in-out infinite;
}

@keyframes driftOne {
    from { transform: translateY(0) translateX(0); }
    to { transform: translateY(50px) translateX(35px); }
}

@keyframes driftTwo {
    from { transform: translateY(0); }
    to { transform: translateY(-45px) translateX(-25px); }
}

@keyframes float {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-18px); }
}

/* =========================================================
   NAVIGATION
   ========================================================= */

.nav-wrapper {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1.5rem;
    padding: 0.7rem 0;
    position: relative;
    z-index: 5;
}

.brand {
    font-family: 'Playfair Display', serif;
    font-size: 1.65rem;
    font-weight: 700;
    color: var(--teal-dark);
    letter-spacing: 0.04em;
}

.brand span {
    color: var(--gold);
}

.nav-caption {
    color: var(--muted);
    font-size: 0.78rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button {
    border-radius: 14px !important;
    border: 1px solid rgba(55,102,91,0.14) !important;
    background: rgba(255,255,255,0.72) !important;
    color: var(--teal-dark) !important;
    font-weight: 600 !important;
    min-height: 44px !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 5px 18px rgba(55,102,91,0.06) !important;
}

.stButton > button:hover {
    transform: translateY(-3px);
    background: #FFFFFF !important;
    border-color: rgba(201,169,110,0.55) !important;
    box-shadow: 0 10px 28px rgba(55,102,91,0.12) !important;
}

.primary-button .stButton > button {
    background: var(--teal) !important;
    color: white !important;
    border: none !important;
}

/* =========================================================
   HERO
   ========================================================= */

.hero {
    position: relative;
    overflow: hidden;
    min-height: 520px;
    padding: 4rem 5rem;
    border-radius: 38px;
    background:
        linear-gradient(120deg,
        rgba(255,255,255,0.90),
        rgba(231,238,226,0.78));
    border: 1px solid rgba(55,102,91,0.10);
    box-shadow: 0 25px 70px rgba(49,75,66,0.10);
    display: flex;
    align-items: center;
    animation: appear 0.8s ease;
}

.hero::after {
    content: "";
    position: absolute;
    width: 430px;
    height: 430px;
    right: -100px;
    top: -130px;
    border-radius: 50%;
    background: radial-gradient(circle,
        rgba(201,169,110,0.28),
        rgba(201,169,110,0.03) 65%,
        transparent 70%);
    animation: pulseGlow 5s ease-in-out infinite;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 780px;
}

.eyebrow {
    display: inline-block;
    color: var(--gold);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(3rem, 7vw, 6.2rem);
    line-height: 0.98;
    color: var(--teal-dark);
    margin: 0;
    letter-spacing: -0.04em;
}

.hero h1 em {
    color: var(--gold);
    font-style: normal;
}

.hero-subtitle {
    margin-top: 1.5rem;
    font-family: 'Playfair Display', serif;
    font-size: 1.35rem;
    color: var(--brown);
}

.hero-description {
    max-width: 680px;
    margin-top: 1rem;
    font-size: 1rem;
    line-height: 1.8;
    color: var(--muted);
}

.hero-orbit {
    position: absolute;
    right: 9%;
    top: 20%;
    width: 260px;
    height: 260px;
    border: 1px solid rgba(55,102,91,0.15);
    border-radius: 50%;
    animation: rotate 20s linear infinite;
}

.hero-orbit::before,
.hero-orbit::after {
    content: "";
    position: absolute;
    border-radius: 50%;
}

.hero-orbit::before {
    width: 22px;
    height: 22px;
    background: var(--gold);
    top: -10px;
    left: 48%;
    box-shadow: 0 0 30px rgba(201,169,110,0.5);
}

.hero-orbit::after {
    width: 15px;
    height: 15px;
    background: var(--teal);
    right: 5px;
    top: 48%;
}

.hero-center {
    position: absolute;
    width: 120px;
    height: 120px;
    border-radius: 50%;
    right: calc(9% + 70px);
    top: calc(20% + 70px);
    background: rgba(255,255,255,0.9);
    border: 1px solid rgba(55,102,91,0.12);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    color: var(--teal-dark);
    box-shadow: 0 15px 50px rgba(55,102,91,0.12);
    animation: float 5s ease-in-out infinite;
    z-index: 2;
}

@keyframes rotate {
    to { transform: rotate(360deg); }
}

@keyframes pulseGlow {
    0%,100% { transform: scale(1); opacity: 0.8; }
    50% { transform: scale(1.12); opacity: 1; }
}

@keyframes appear {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* =========================================================
   TAGLINE STRIP
   ========================================================= */

.tagline-strip {
    text-align: center;
    padding: 1.8rem 1rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--teal);
    font-size: 0.78rem;
    font-weight: 700;
}

.tagline-strip span {
    color: var(--gold);
    margin: 0 0.6rem;
}

/* =========================================================
   SECTION HEADERS
   ========================================================= */

.section-label {
    color: var(--gold);
    font-size: 0.76rem;
    text-transform: uppercase;
    letter-spacing: 0.16em;
    font-weight: 700;
}

.section-title {
    font-family: 'Playfair Display', serif;
    color: var(--teal-dark);
    font-size: 2.7rem;
    margin-top: 0.25rem;
}

.section-text {
    color: var(--muted);
    line-height: 1.7;
    max-width: 720px;
}

/* =========================================================
   FEATURE CARDS
   ========================================================= */

.feature-card {
    padding: 1.7rem;
    min-height: 210px;
    border-radius: 24px;
    background: rgba(255,255,255,0.76);
    border: 1px solid rgba(55,102,91,0.09);
    box-shadow: 0 12px 35px rgba(55,102,91,0.07);
    transition: all 0.3s ease;
    animation: appear 0.7s ease;
}

.feature-card:hover {
    transform: translateY(-7px);
    box-shadow: 0 20px 45px rgba(55,102,91,0.13);
}

.feature-icon {
    font-size: 1.7rem;
    margin-bottom: 1rem;
}

.feature-card h3 {
    font-family: 'Playfair Display', serif;
    color: var(--teal-dark);
    font-size: 1.35rem;
}

.feature-card p {
    color: var(--muted);
    line-height: 1.65;
    font-size: 0.92rem;
}

/* =========================================================
   QUESTIONNAIRE
   ========================================================= */

.question-shell {
    max-width: 950px;
    margin: auto;
    padding: 2.5rem;
    background: rgba(255,255,255,0.78);
    border-radius: 32px;
    border: 1px solid rgba(55,102,91,0.09);
    box-shadow: 0 20px 60px rgba(55,102,91,0.08);
    animation: appear 0.5s ease;
}

.question-number {
    color: var(--gold);
    font-size: 0.78rem;
    letter-spacing: 0.14em;
    font-weight: 700;
    text-transform: uppercase;
}

.question-title {
    font-family: 'Playfair Display', serif;
    color: var(--teal-dark);
    font-size: 2.2rem;
    line-height: 1.2;
    margin: 0.6rem 0 0.7rem;
}

.question-helper {
    color: var(--muted);
    margin-bottom: 1.8rem;
}

.option-card {
    padding: 1.3rem;
    border-radius: 20px;
    background: #FFFDF8;
    border: 1px solid rgba(55,102,91,0.10);
    transition: all 0.25s ease;
}

.option-card:hover {
    transform: translateY(-4px);
    border-color: rgba(201,169,110,0.65);
    box-shadow: 0 12px 30px rgba(55,102,91,0.10);
}

/* =========================================================
   PROGRESS
   ========================================================= */

.progress-track {
    height: 8px;
    background: #E4E8E0;
    border-radius: 99px;
    overflow: hidden;
    margin: 1rem 0 2rem;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--teal), var(--gold));
    border-radius: 99px;
    transition: width 0.5s ease;
}

/* =========================================================
   DASHBOARD
   ========================================================= */

.metric-card {
    padding: 1.5rem;
    border-radius: 22px;
    background: rgba(255,255,255,0.80);
    border: 1px solid rgba(55,102,91,0.08);
    box-shadow: 0 10px 30px rgba(55,102,91,0.06);
    transition: all 0.25s ease;
}

.metric-card:hover {
    transform: translateY(-4px);
}

.metric-label {
    color: var(--muted);
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.metric-value {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    color: var(--teal-dark);
    margin-top: 0.35rem;
}

/* =========================================================
   AYURVEDIC BODY TYPE
   ========================================================= */

.type-card {
    padding: 2rem;
    border-radius: 28px;
    min-height: 260px;
    background: rgba(255,255,255,0.82);
    border: 1px solid rgba(55,102,91,0.09);
    transition: all 0.3s ease;
}

.type-card:hover {
    transform: translateY(-8px) rotate(0.3deg);
    box-shadow: 0 22px 45px rgba(55,102,91,0.12);
}

.type-symbol {
    font-size: 2rem;
}

.type-card h3 {
    font-family: 'Playfair Display', serif;
    color: var(--teal-dark);
    font-size: 1.6rem;
}

/* =========================================================
   CHALLENGE
   ========================================================= */

.challenge-card {
    padding: 3rem;
    border-radius: 34px;
    background:
        linear-gradient(135deg,
        rgba(255,255,255,0.9),
        rgba(235,241,232,0.82));
    border: 1px solid rgba(55,102,91,0.10);
    box-shadow: 0 20px 60px rgba(55,102,91,0.10);
    text-align: center;
    animation: appear 0.6s ease;
}

.challenge-icon {
    font-size: 3rem;
    animation: float 4s ease-in-out infinite;
}

.challenge-card h2 {
    font-family: 'Playfair Display', serif;
    font-size: 2.5rem;
    color: var(--teal-dark);
}

.reward-reveal {
    padding: 1rem;
    margin-top: 1.5rem;
    border-radius: 18px;
    background: rgba(201,169,110,0.13);
    color: var(--brown);
}

/* =========================================================
   EMPTY STATE
   ========================================================= */

.empty-state {
    text-align: center;
    padding: 5rem 2rem;
    border-radius: 30px;
    background: rgba(255,255,255,0.68);
    border: 1px dashed rgba(55,102,91,0.18);
    animation: appear 0.8s ease;
}

.empty-symbol {
    font-size: 3rem;
    animation: float 4s ease-in-out infinite;
}

.empty-state h2 {
    font-family: 'Playfair Display', serif;
    color: var(--teal-dark);
    font-size: 2.2rem;
}

/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    margin-top: 4rem;
    padding-top: 2rem;
    border-top: 1px solid rgba(55,102,91,0.10);
    text-align: center;
    color: var(--muted);
    font-size: 0.8rem;
}

</style>

<div class="bg-orb-one"></div>
<div class="bg-orb-two"></div>
<div class="bg-orb-three"></div>
""", unsafe_allow_html=True)


# =========================================================
# DATA
# =========================================================

questions = [

    {
        "section": "Your foundation",
        "q": "How old are you?",
        "type": "number",
        "key": "age",
        "help": "Your age helps us understand your wellness context."
    },

    {
        "section": "Your foundation",
        "q": "How would you like MYBIO to address you?",
        "type": "choice",
        "key": "sex",
        "options": ["Female", "Male", "Prefer not to say"],
        "help": ""
    },

    {
        "section": "Your foundation",
        "q": "What is your height?",
        "type": "number",
        "key": "height",
        "help": "Enter your height in centimetres."
    },

    {
        "section": "Your foundation",
        "q": "What is your current weight?",
        "type": "number",
        "key": "weight",
        "help": "Enter your current weight in kilograms."
    },

    {
        "section": "Your intention",
        "q": "What would you most like to work towards?",
        "type": "choice",
        "key": "goal",
        "options": [
            "Feel lighter",
            "Maintain my current state",
            "Build fitness",
            "Reduce body fat",
            "Build strength",
            "Improve overall wellbeing"
        ],
        "help": ""
    },

    {
        "section": "Your rhythm",
        "q": "How active is a typical day for you?",
        "type": "choice",
        "key": "activity",
        "options": [
            "Mostly seated",
            "Light movement",
            "Regularly active",
            "Highly active"
        ],
        "help": ""
    },

    {
        "section": "Your natural tendencies",
        "q": "Which description feels closest to your natural build?",
        "type": "dosha",
        "key": "build",
        "options": {
            "Vata": "Naturally light and lean; gaining weight can be difficult.",
            "Pitta": "Moderate build; tends to maintain weight relatively easily.",
            "Kapha": "Solid or fuller build; tends to gain weight more easily."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "How would you describe your appetite?",
        "type": "dosha",
        "key": "appetite",
        "options": {
            "Vata": "Variable — sometimes very hungry, sometimes not.",
            "Pitta": "Strong and fairly predictable.",
            "Kapha": "Moderate or slow; I can comfortably go longer between meals."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "What is your usual digestive experience?",
        "type": "dosha",
        "key": "digestion",
        "options": {
            "Vata": "Can be irregular, with occasional bloating.",
            "Pitta": "Usually strong, sometimes accompanied by acidity.",
            "Kapha": "Generally slower, with occasional heaviness."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "Which environment feels least comfortable?",
        "type": "dosha",
        "key": "weather",
        "options": {
            "Vata": "Cold and windy conditions.",
            "Pitta": "Excessive heat.",
            "Kapha": "Damp, heavy or very cold conditions."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "How does your energy usually behave?",
        "type": "dosha",
        "key": "energy",
        "options": {
            "Vata": "Quick bursts of energy, but inconsistent.",
            "Pitta": "Focused, driven and fairly strong.",
            "Kapha": "Slower to start but good endurance."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "What best describes your sleep?",
        "type": "dosha",
        "key": "sleep_natural",
        "options": {
            "Vata": "Light or sometimes irregular.",
            "Pitta": "Moderate and generally sufficient.",
            "Kapha": "Deep and longer; waking can take effort."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "Which temperament feels most familiar?",
        "type": "dosha",
        "key": "temperament",
        "options": {
            "Vata": "Creative, energetic, curious and sometimes restless.",
            "Pitta": "Focused, ambitious and decisive.",
            "Kapha": "Calm, patient, steady and relaxed."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "How does your weight generally respond?",
        "type": "dosha",
        "key": "weight_response",
        "options": {
            "Vata": "I find gaining weight difficult.",
            "Pitta": "My weight changes fairly moderately.",
            "Kapha": "I gain weight relatively easily and lose it slowly."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "How structured is your daily routine?",
        "type": "dosha",
        "key": "routine",
        "options": {
            "Vata": "Quite unpredictable.",
            "Pitta": "Fairly organised.",
            "Kapha": "Regular, but sometimes inactive."
        }
    },

    {
        "section": "Your health context",
        "q": "Has a healthcare professional diagnosed you with any of these conditions?",
        "type": "choice",
        "key": "condition",
        "options": [
            "None",
            "Type 2 diabetes",
            "PCOS",
            "Hypothyroidism",
            "Cushing's syndrome",
            "Fatty liver",
            "Another metabolic/endocrine condition"
        ],
        "help": "This information is used only as a safety context."
    },

    {
        "section": "Your health context",
        "q": "Do you currently take medication that may influence weight or appetite?",
        "type": "choice",
        "key": "medication",
        "options": ["No", "Yes"],
        "help": "Medication-related decisions should always involve your healthcare professional."
    },

    {
        "section": "Your health context",
        "q": "Do you have any known food allergies or intolerances?",
        "type": "choice",
        "key": "allergy",
        "options": [
            "None",
            "Dairy",
            "Nuts",
            "Gluten",
            "Eggs",
            "Seafood",
            "Other"
        ],
        "help": ""
    },

    {
        "section": "Your health context",
        "q": "Is there another health consideration you want to keep in mind?",
        "type": "choice",
        "key": "other_health",
        "options": ["No", "Yes"],
        "help": ""
    },

    {
        "section": "Your nourishment",
        "q": "Which eating pattern best represents you?",
        "type": "choice",
        "key": "diet",
        "options": ["Vegetarian", "Non-vegetarian", "Eggetarian"],
        "help": ""
    },

    {
        "section": "Your nourishment",
        "q": "How many meals do you usually have in a day?",
        "type": "choice",
        "key": "meals",
        "options": ["1", "2", "3", "4 or more"],
        "help": ""
    },

    {
        "section": "Your nourishment",
        "q": "How often does processed or fast food enter your week?",
        "type": "choice",
        "key": "junk",
        "options": [
            "Rarely",
            "Once or twice",
            "Several times",
            "Almost every day"
        ],
        "help": ""
    },

    {
        "section": "Your nourishment",
        "q": "How often do you have sugary drinks?",
        "type": "choice",
        "key": "sugar",
        "options": [
            "Rarely",
            "Sometimes",
            "Frequently",
            "Daily"
        ],
        "help": ""
    },

    {
        "section": "Your daily rhythm",
        "q": "How much sleep do you usually get?",
        "type": "choice",
        "key": "sleep",
        "options": [
            "Less than 5 hours",
            "5–7 hours",
            "7–9 hours",
            "More than 9 hours"
        ],
        "help": ""
    },

    {
        "section": "Your daily rhythm",
        "q": "How would you describe your current stress?",
        "type": "choice",
        "key": "stress",
        "options": [
            "Low",
            "Moderate",
            "High"
        ],
        "help": ""
    },

    {
        "section": "Your daily rhythm",
        "q": "How much intentional physical activity do you get each day?",
        "type": "number",
        "key": "activity_minutes",
        "help": "Approximate minutes are enough."
    },

    {
        "section": "Your daily rhythm",
        "q": "How much of your day is spent sitting or looking at screens?",
        "type": "choice",
        "key": "screen",
        "options": [
            "Less than 2 hours",
            "2–6 hours",
            "6–8 hours",
            "More than 8 hours"
        ],
        "help": ""
    },

    {
        "section": "Your daily rhythm",
        "q": "How predictable are your meal timings?",
        "type": "choice",
        "key": "meal_timing",
        "options": [
            "Very regular",
            "Mostly regular",
            "Sometimes irregular",
            "Very irregular"
        ],
        "help": ""
    }
]


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def navigate(page):
    st.session_state.page = page
    st.rerun()


def calculate_type():
    scores = {
        "Vata": st.session_state.vata,
        "Pitta": st.session_state.pitta,
        "Kapha": st.session_state.kapha
    }

    ordered = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    if ordered[0][1] == ordered[1][1] == ordered[2][1]:
        return "Balanced"

    if ordered[0][1] == ordered[1][1]:
        return f"{ordered[0][0]}–{ordered[1][0]}"

    return ordered[0][0]


def save_answer(key, value):
    st.session_state.answers[key] = value


def finish_questionnaire():
    answers = st.session_state.answers

    st.session_state.vata = 0
    st.session_state.pitta = 0
    st.session_state.kapha = 0

    dosha_keys = [
        "build",
        "appetite",
        "digestion",
        "weather",
        "energy",
        "sleep_natural",
        "temperament",
        "weight_response",
        "routine"
    ]

    for key in dosha_keys:
        value = answers.get(key)
        if value == "Vata":
            st.session_state.vata += 1
        elif value == "Pitta":
            st.session_state.pitta += 1
        elif value == "Kapha":
            st.session_state.kapha += 1

    st.session_state.ayurvedic_type = calculate_type()
    st.session_state.profile_complete = True
    st.session_state.question_index = 0
    st.session_state.streak = 1
    st.session_state.xp = 100

    navigate("Body")


def bmi_value():
    height = st.session_state.answers.get("height")
    weight = st.session_state.answers.get("weight")

    if height and weight and height > 0:
        return weight / ((height / 100) ** 2)

    return None


# =========================================================
# NAVIGATION
# =========================================================

st.markdown("""
<div class="nav-wrapper">
    <div>
        <div class="brand">MY<span>BIO</span></div>
        <div class="nav-caption">Your personal wellness journey</div>
    </div>
</div>
""", unsafe_allow_html=True)

nav_items = [
    ("Home", "Home"),
    ("Begin Journey", "Questionnaire"),
    ("My Wellness", "Body"),
    ("Ayurvedic Body Type", "Ayurvedic"),
    ("Today's Challenge", "Challenges"),
    ("My Rhythm", "Streak"),
    ("For You", "Recommendations"),
    ("About", "About")
]

cols = st.columns(len(nav_items))

for col, (label, page) in zip(cols, nav_items):
    with col:
        if st.button(label, key=f"nav_{page}", use_container_width=True):
            navigate(page)


# =========================================================
# HOME
# =========================================================

def home():

    st.markdown("""
    <div class="hero">

        <div class="hero-content">

            <div class="eyebrow">
                ✦ A more mindful way to know yourself
            </div>

            <h1>
                Meet the<br>
                <em>you</em> within.
            </h1>

            <div class="hero-subtitle">
                Ancient wisdom. Modern you. Infinite possibilities.
            </div>

            <p class="hero-description">
                MYBIO brings together your everyday habits, body signals,
                lifestyle rhythms and traditional wellness perspectives
                to create a more meaningful picture of you.
            </p>

        </div>

        <div class="hero-orbit"></div>
        <div class="hero-center">MYBIO</div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tagline-strip">
        ANCIENT WISDOM
        <span>✦</span>
        MODERN YOU
        <span>✦</span>
        INFINITE POSSIBILITIES
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin:1rem 0 2rem;">
        <div class="section-label">YOUR JOURNEY STARTS HERE</div>
        <div class="section-title">Wellness, made personal.</div>
        <p class="section-text" style="margin:auto;">
            Begin with a few thoughtful questions. Discover patterns,
            understand your natural tendencies and build small habits
            that fit your life.
        </p>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(3)

    features = [
        (
            "◌",
            "Know Yourself",
            "Explore the patterns behind your everyday energy, sleep,
            nourishment and lifestyle."
        ),
        (
            "✦",
            "Discover Your Balance",
            "Explore your Ayurvedic body type through a simple,
            interactive experience."
        ),
        (
            "↗",
            "Grow One Step at a Time",
            "Turn awareness into small, meaningful actions that
            become part of your rhythm."
        )
    ]

    for col, (icon, title, text) in zip(cols, features):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon">{icon}</div>
                <h3>{title}</h3>
                <p>{text}</p>
            </div>
            """, unsafe_allow_html=True)

    st.write("")

    if st.session_state.profile_complete:
        st.markdown(
            '<div class="primary-button">',
            unsafe_allow_html=True
        )

        if st.button(
            "Continue my journey  →",
            use_container_width=True,
            key="home_continue"
        ):
            navigate("Body")

        st.markdown("</div>", unsafe_allow_html=True)

    else:
        st.markdown(
            '<div class="primary-button">',
            unsafe_allow_html=True
        )

        if st.button(
            "Begin your journey  →",
            use_container_width=True,
            key="home_begin"
        ):
            navigate("Questionnaire")

        st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# QUESTIONNAIRE
# =========================================================

def questionnaire():

    index = st.session_state.question_index
    total = len(questions)
    question = questions[index]

    progress = index / total * 100

    st.markdown("""
    <div style="margin-bottom:2rem;">
        <div class="section-label">TWINFIT · YOUR FIRST STEP</div>
        <div class="section-title">Let's begin with you.</div>
        <p class="section-text">
            There are no right or wrong answers. Choose what feels
            most naturally true for you.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="progress-track">
        <div class="progress-fill" style="width:{progress}%;"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="text-align:right; color:#718078; font-size:0.8rem;">
        {index + 1:02d} / {total:02d}
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="question-shell">', unsafe_allow_html=True)

    st.markdown(
        f'<div class="question-number">{question["section"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="question-title">{question["q"]}</div>',
        unsafe_allow_html=True
    )

    if question.get("help"):
        st.markdown(
            f'<div class="question-helper">{question["help"]}</div>',
            unsafe_allow_html=True
        )

    current = st.session_state.answers.get(question["key"])

    # NUMBER QUESTION
    if question["type"] == "number":

        value = st.number_input(
            " ",
            min_value=1.0,
            max_value=250.0 if question["key"] == "weight" else 250.0,
            value=float(current) if current else 1.0,
            step=1.0,
            key=f"input_{question['key']}"
        )

        if st.button(
            "Continue  →",
            use_container_width=True,
            key=f"continue_{question['key']}"
        ):

            save_answer(question["key"], value)

            if index < total - 1:
                st.session_state.question_index += 1
                st.rerun()
            else:
                finish_questionnaire()

    # DOSHA QUESTION
    elif question["type"] == "dosha":

        options = list(question["options"].items())

        for start in range(0, len(options), 3):

            row = options[start:start + 3]
            cols = st.columns(len(row))

            for col, (dosha, description) in zip(cols, row):

                with col:

                    selected = current == dosha

                    st.markdown(f"""
                    <div class="option-card">
                        <div style="
                            font-family:'Playfair Display',serif;
                            color:#244D45;
                            font-size:1.25rem;
                            font-weight:600;
                            margin-bottom:0.5rem;">
                            {dosha}
                        </div>
                        <div style="
                            color:#718078;
                            font-size:0.87rem;
                            line-height:1.55;">
                            {description}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    if st.button(
                        "Selected ✓" if selected else "Choose",
                        key=f"{question['key']}_{dosha}",
                        use_container_width=True
                    ):
                        save_answer(question["key"], dosha)
                        st.rerun()

    # NORMAL CHOICE
    else:

        options = question["options"]

        for start in range(0, len(options), 2):

            row = options[start:start + 2]
            cols = st.columns(len(row))

            for col, option in zip(cols, row):

                with col:

                    selected = current == option

                    st.markdown(f"""
                    <div class="option-card">
                        <div style="
                            color:#25352F;
                            font-size:0.98rem;
                            font-weight:600;">
                            {option}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    if st.button(
                        "Selected ✓" if selected else "Choose",
                        key=f"{question['key']}_{option}",
                        use_container_width=True
                    ):
                        save_answer(question["key"], option)
                        st.rerun()

        if current:
            if st.button(
                "Continue  →",
                use_container_width=True,
                key=f"next_{question['key']}"
            ):

                if index < total - 1:
                    st.session_state.question_index += 1
                    st.rerun()
                else:
                    finish_questionnaire()

    st.markdown("</div>", unsafe_allow_html=True)

    if index > 0:

        if st.button(
            "← Previous",
            key="previous_question"
        ):
            st.session_state.question_index -= 1
            st.rerun()


# =========================================================
# WELLNESS DASHBOARD
# =========================================================

def body():

    if not st.session_state.profile_complete:

        st.markdown("""
        <div class="empty-state">
            <div class="empty-symbol">✦</div>
            <h2>Your wellness picture is waiting.</h2>
            <p>
                Complete your first journey to begin discovering
                your personal patterns.
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Start my journey →", use_container_width=True):
            navigate("Questionnaire")

        return

    bmi = bmi_value()

    st.markdown("""
    <div class="section-label">YOUR WELLNESS SPACE</div>
    <div class="section-title">A picture of where you are.</div>
    <p class="section-text">
        Your journey is not about perfection. It is about noticing
        patterns and making better choices, one day at a time.
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    cols = st.columns(4)

    metrics = [
        ("Current rhythm", f"{st.session_state.streak} day"),
        ("Journey points", f"{st.session_state.xp} XP"),
        ("Ayurvedic body type", st.session_state.ayurvedic_type),
        ("BMI", f"{bmi:.1f}" if bmi else "—")
    ]

    for col, (label, value) in zip(cols, metrics):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="feature-card">
        <div class="section-label">TODAY</div>
        <h3>A gentle place to start</h3>
        <p>
            You have already taken the first step by understanding
            yourself. Now choose one small action that feels realistic
            for today.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("See today's challenge →", use_container_width=True):
        navigate("Challenges")


# =========================================================
# AYURVEDIC BODY TYPE
# =========================================================

def ayurvedic():

    if not st.session_state.profile_complete:

        st.markdown("""
        <div class="empty-state">
            <div class="empty-symbol">◌</div>
            <h2>Your natural balance is yet to unfold.</h2>
            <p>
                Complete the MYBIO journey first and this space
                will become part of your wellness story.
            </p>
        </div>
        """, unsafe_allow_html=True)

        return

    st.markdown("""
    <div class="section-label">ANCIENT PERSPECTIVE</div>
    <div class="section-title">Your Ayurvedic Body Type</div>
    <p class="section-text">
        Ayurveda describes different natural patterns of constitution
        through three fundamental tendencies. Your responses provide
        an introductory, non-diagnostic interpretation.
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    types = [
        (
            "Vata",
            "◌",
            "Movement & adaptability",
            "Often associated with lightness, creativity, variability and movement."
        ),
        (
            "Pitta",
            "☀",
            "Transformation & focus",
            "Often associated with intensity, focus, warmth and purposeful action."
        ),
        (
            "Kapha",
            "◒",
            "Stability & grounding",
            "Often associated with steadiness, endurance, calmness and grounding."
        )
    ]

    cols = st.columns(3)

    for col, (name, icon, subtitle, text) in zip(cols, types):

        with col:

            highlight = ""

            if name in st.session_state.ayurvedic_type:
                highlight = "border:2px solid rgba(201,169,110,0.65);"

            st.markdown(f"""
            <div class="type-card" style="{highlight}">
                <div class="type-symbol">{icon}</div>
                <h3>{name}</h3>
                <div style="
                    color:#C9A96E;
                    font-weight:700;
                    font-size:0.8rem;
                    text-transform:uppercase;
                    letter-spacing:0.08em;">
                    {subtitle}
                </div>
                <p style="
                    color:#718078;
                    line-height:1.65;
                    margin-top:1rem;">
                    {text}
                </p>
            </div>
            """, unsafe_allow_html=True)

    st.write("")

    st.markdown(f"""
    <div class="challenge-card">
        <div class="challenge-icon">✦</div>
        <div class="section-label">YOUR RESULT</div>
        <h2>{st.session_state.ayurvedic_type}</h2>
        <p style="color:#718078;">
            Your responses show this as the strongest pattern in
            this introductory wellness assessment.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.caption(
        "This is an educational wellness interpretation, not a medical diagnosis."
    )


# =========================================================
# CHALLENGES
# =========================================================

challenges_data = [
    {
        "title": "The Hydration Pause",
        "icon": "◌",
        "task": "Take a mindful water break and have one full glass of water.",
        "reward": "Hydration Hero",
        "xp": 20
    },
    {
        "title": "The Movement Minute",
        "icon": "↗",
        "task": "Take a 10-minute walk or gentle movement break today.",
        "reward": "Move With Intention",
        "xp": 25
    },
    {
        "title": "The Mindful Plate",
        "icon": "◉",
        "task": "For one meal today, pause before eating and notice your hunger.",
        "reward": "Mindful Nourisher",
        "xp": 25
    },
    {
        "title": "The Evening Reset",
        "icon": "☾",
        "task": "Put your screen away for 20 minutes before bedtime.",
        "reward": "Evening Guardian",
        "xp": 30
    }
]


def challenges():

    if not st.session_state.profile_complete:

        st.markdown("""
        <div class="empty-state">
            <div class="empty-symbol">✦</div>
            <h2>Your first challenge is waiting.</h2>
            <p>
                Begin your MYBIO journey first. Your daily actions
                will appear here as you move forward.
            </p>
        </div>
        """, unsafe_allow_html=True)

        return

    completed = st.session_state.completed_challenges

    remaining = [
        i for i in range(len(challenges_data))
        if i not in completed
    ]

    if not remaining:

        st.markdown("""
        <div class="empty-state">
            <div class="empty-symbol">✦</div>
            <h2>You made it through.</h2>
            <p>
                Your next chapter is waiting. Keep showing up
                for yourself.
            </p>
        </div>
        """, unsafe_allow_html=True)

        return

    current_index = remaining[0]
    challenge = challenges_data[current_index]

    st.markdown("""
    <div class="section-label">ONE SMALL STEP</div>
    <div class="section-title">Today's Challenge</div>
    <p class="section-text">
        You don't need to change everything today.
        Start with one meaningful action.
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown(f"""
    <div class="challenge-card">
        <div class="challenge-icon">{challenge["icon"]}</div>

        <div class="section-label">
            CHALLENGE {len(completed) + 1}
        </div>

        <h2>{challenge["title"]}</h2>

        <p style="
            max-width:620px;
            margin:1rem auto;
            color:#718078;
            line-height:1.8;">
            {challenge["task"]}
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if current_index not in st.session_state.completed_challenges:

        if not st.session_state.started:

            if st.button(
                "Start this challenge  →",
                use_container_width=True
            ):
                st.session_state.started = True
                st.rerun()

        else:

            st.markdown("""
            <div style="
                text-align:center;
                color:#37665B;
                margin:1rem;">
                ✦ Challenge in progress
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                "I completed it ✓",
                use_container_width=True
            ):

                st.session_state.completed_challenges.append(current_index)
                st.session_state.xp += challenge["xp"]
                st.session_state.streak += 1
                st.session_state.started = False

                st.markdown(f"""
                <div class="reward-reveal">
                    ✦ You earned <b>{challenge["xp"]} XP</b><br>
                    Achievement unlocked: <b>{challenge["reward"]}</b>
                </div>
                """, unsafe_allow_html=True)

                st.rerun()


# =========================================================
# STREAK
# =========================================================

def streak():

    if not st.session_state.profile_complete:

        st.markdown("""
        <div class="empty-state">
            <div class="empty-symbol">✧</div>
            <h2>Your rhythm hasn't begun yet.</h2>
            <p>
                Complete your first wellness journey and start
                building your own rhythm, one day at a time.
            </p>
        </div>
        """, unsafe_allow_html=True)

        return

    current = st.session_state.streak

    st.markdown("""
    <div class="section-label">YOUR RHYTHM</div>
    <div class="section-title">Consistency has its own magic.</div>
    <p class="section-text">
        A streak is not about being perfect. It is simply a reminder
        that small actions become powerful when they are repeated.
    </p>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown(f"""
    <div class="challenge-card">
        <div class="challenge-icon">✦</div>

        <div class="section-label">CURRENT RHYTHM</div>

        <h2>{current} day{'s' if current != 1 else ''}</h2>

        <p style="color:#718078;">
            Keep going. Your next small step matters.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    cols = st.columns(7)

    days = ["M", "T", "W", "T", "F", "S", "S"]

    for i, (col, day) in enumerate(zip(cols, days)):

        active = i < min(current, 7)

        with col:

            st.markdown(f"""
            <div style="
                text-align:center;
                padding:1rem 0.2rem;
                border-radius:18px;
                background:{'#37665B' if active else '#FFFFFF'};
                color:{'white' if active else '#718078'};
                border:1px solid rgba(55,102,91,0.10);
                box-shadow:0 7px 20px rgba(55,102,91,0.06);">
                <div style="font-size:0.75rem;">{day}</div>
                <div style="font-size:1.2rem;margin-top:0.3rem;">
                    {'✦' if active else '·'}
                </div>
            </div>
            """, unsafe_allow_html=True)


# =========================================================
# RECOMMENDATIONS
# =========================================================

def recommendations():

    st.markdown("""
    <div class="section-label">A LITTLE SOMETHING FOR YOU</div>
    <div class="section-title">Your wellness notes.</div>
    <p class="section-text">
        A few gentle ideas based on the patterns you shared.
        Nothing here is about perfection.
    </p>
    """, unsafe_allow_html=True)

    answers = st.session_state.answers

    recommendations_list = []

    if answers.get("sleep") in ["Less than 5 hours", "5–7 hours"]:
        recommendations_list.append(
            (
                "☾",
                "Give rest a little more room",
                "Try protecting a consistent bedtime and creating a quieter "
                "wind-down period before sleep."
            )
        )

    if answers.get("activity") in ["Mostly seated", "Light movement"]:
        recommendations_list.append(
            (
                "↗",
                "Bring movement into the ordinary",
                "A short walk, stretch or movement break can be easier to "
                "maintain than waiting for a perfect workout."
            )
        )

    if answers.get("junk") in ["Several times", "Almost every day"]:
        recommendations_list.append(
            (
                "◉",
                "Make one meal feel different",
                "Instead of changing everything, begin with one balanced "
                "meal that leaves you feeling nourished."
            )
        )

    if answers.get("meal_timing") in ["Sometimes irregular", "Very irregular"]:
        recommendations_list.append(
            (
                "◷",
                "Create a little rhythm",
                "More predictable meal timings may make your day feel "
                "less scattered."
            )
        )

    if not recommendations_list:
        recommendations_list.append(
            (
                "✦",
                "Keep what is already working",
                "Your responses suggest several positive habits. "
                "Focus on consistency rather than constantly adding more."
            )
        )

    for icon, title, text in recommendations_list:

        st.markdown(f"""
        <div class="feature-card" style="margin-bottom:1rem;">
            <div class="feature-icon">{icon}</div>
            <h3>{title}</h3>
            <p>{text}</p>
        </div>
        """, unsafe_allow_html=True)

    st.caption(
        "MYBIO provides general wellness information and does not replace "
        "professional medical or nutritional advice."
    )


# =========================================================
# ABOUT
# =========================================================

def about():

    st.markdown("""
    <div class="section-label">THE IDEA BEHIND MYBIO</div>

    <div class="section-title">
        Wellness begins with awareness.
    </div>

    <p class="section-text">
        MYBIO is designed around a simple idea:
        understanding yourself can be the first step towards
        making better everyday choices.
    </p>

    <br>

    <div class="feature-card">
        <div class="feature-icon">✦</div>

        <h3>
            Ancient perspectives. Contemporary experience.
        </h3>

        <p>
            MYBIO brings together lifestyle reflection, body measurements,
            everyday habits and an introductory Ayurvedic perspective
            in one personal wellness experience.
        </p>
    </div>

    <br>

    <div class="feature-card">
        <div class="feature-icon">◌</div>

        <h3>
            Designed around you.
        </h3>

        <p>
            Instead of presenting endless information, MYBIO focuses
            on turning personal responses into a journey that feels
            simple, visual and actionable.
        </p>
    </div>

    <br>

    <div class="feature-card">
        <div class="feature-icon">∞</div>

        <h3>
            A journey, not a judgement.
        </h3>

        <p>
            Your wellness is constantly changing. MYBIO is designed
            to encourage curiosity, consistency and small improvements
            rather than perfection.
        </p>
    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ROUTING
# =========================================================

page = st.session_state.page

if page == "Home":
    home()

elif page == "Questionnaire":
    questionnaire()

elif page == "Body":
    body()

elif page == "Ayurvedic":
    ayurvedic()

elif page == "Challenges":
    challenges()

elif page == "Streak":
    streak()

elif page == "Recommendations":
    recommendations()

elif page == "About":
    about()


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    <b>MYBIO</b> · Ancient wisdom. Modern you. Infinite possibilities.
    <br><br>
    A wellness exploration experience — designed for awareness,
    reflection and better everyday choices.
</div>
""", unsafe_allow_html=True)
