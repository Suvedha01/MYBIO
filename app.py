import streamlit as st
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

DEFAULTS = {
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
    "completed_challenges": [],
    "started": False,
    "last_completed": None
}

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');


/* =========================================================
   COLOR SYSTEM
   ========================================================= */

:root {
    --ivory: #FBF8F1;
    --cream: #F4EFE5;
    --white: #FFFFFF;

    --sage: #A9B9A2;
    --sage-soft: #DDE6D7;

    --peach: #E8B99A;
    --peach-soft: #F5DED0;

    --gold: #C9A66B;
    --gold-soft: #EBD9B6;

    --olive: #65745D;

    --ink: #29332E;
    --ink-soft: #56625B;

    --line: rgba(41, 51, 46, 0.10);
}


/* =========================================================
   BASE
   ========================================================= */

html,
body,
[class*="css"] {
    font-family: "DM Sans", sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 8% 8%,
            rgba(232,185,154,0.18),
            transparent 25%
        ),
        radial-gradient(
            circle at 92% 12%,
            rgba(169,185,162,0.18),
            transparent 28%
        ),
        radial-gradient(
            circle at 80% 85%,
            rgba(201,166,107,0.10),
            transparent 25%
        ),
        linear-gradient(
            135deg,
            #FBF8F1 0%,
            #FFFDF9 48%,
            #F1F4EC 100%
        );

    color: var(--ink);
    min-height: 100vh;
}

.block-container {
    max-width: 1380px;
    padding-top: 1.2rem;
    padding-bottom: 4rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}


/* =========================================================
   BACKGROUND MOTION
   ========================================================= */

.motion-orb {
    position: fixed;
    border-radius: 50%;
    pointer-events: none;
    z-index: 0;
}

.orb-1 {
    width: 260px;
    height: 260px;
    left: -100px;
    top: 18%;
    background: rgba(232,185,154,0.13);
    filter: blur(5px);
    animation: drift1 12s ease-in-out infinite alternate;
}

.orb-2 {
    width: 230px;
    height: 230px;
    right: -90px;
    bottom: 15%;
    background: rgba(169,185,162,0.16);
    filter: blur(5px);
    animation: drift2 15s ease-in-out infinite alternate;
}

.orb-3 {
    width: 90px;
    height: 90px;
    right: 18%;
    top: 40%;
    background: rgba(201,166,107,0.10);
    animation: floating 6s ease-in-out infinite;
}

@keyframes drift1 {
    from {
        transform: translate(0,0);
    }
    to {
        transform: translate(45px,55px);
    }
}

@keyframes drift2 {
    from {
        transform: translate(0,0);
    }
    to {
        transform: translate(-40px,-45px);
    }
}

@keyframes floating {
    0%,100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-20px);
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

@keyframes softPulse {
    0%,100% {
        transform: scale(1);
        opacity: 0.75;
    }
    50% {
        transform: scale(1.08);
        opacity: 1;
    }
}

@keyframes spin {
    to {
        transform: rotate(360deg);
    }
}


/* =========================================================
   BRAND
   ========================================================= */

.brand-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
    position: relative;
    z-index: 5;
}

.brand {
    font-family: "Playfair Display", serif;
    font-size: 1.75rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    color: var(--ink);
}

.brand span {
    color: var(--peach);
}

.brand-caption {
    color: var(--ink-soft);
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}


/* =========================================================
   NAVIGATION
   ========================================================= */

div.stButton > button {
    border-radius: 15px !important;
    border: 1px solid rgba(41,51,46,0.09) !important;
    background: rgba(255,255,255,0.62) !important;
    color: var(--ink) !important;

    font-weight: 600 !important;

    min-height: 43px !important;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        background 0.25s ease,
        border-color 0.25s ease !important;

    box-shadow:
        0 6px 20px rgba(41,51,46,0.045) !important;
}

div.stButton > button:hover {
    transform: translateY(-3px) !important;

    background: #FFFFFF !important;

    border-color: rgba(232,185,154,0.55) !important;

    box-shadow:
        0 12px 28px rgba(41,51,46,0.09) !important;
}

div.stButton > button:active {
    transform: translateY(0) !important;
}


/* Primary buttons */

.primary-btn div.stButton > button {
    background:
        linear-gradient(
            135deg,
            #687A61,
            #829579
        ) !important;

    color: white !important;

    border: none !important;

    box-shadow:
        0 12px 28px rgba(101,116,93,0.22) !important;
}

.primary-btn div.stButton > button:hover {
    background:
        linear-gradient(
            135deg,
            #596A53,
            #74866D
        ) !important;

    color: white !important;
}


/* =========================================================
   HERO
   ========================================================= */

.hero {
    position: relative;
    overflow: hidden;

    min-height: 555px;

    padding: 4.5rem 5rem;

    border-radius: 42px;

    background:
        linear-gradient(
            120deg,
            rgba(255,255,255,0.94),
            rgba(249,240,229,0.80)
        );

    border: 1px solid rgba(41,51,46,0.07);

    box-shadow:
        0 28px 80px rgba(72,75,65,0.10);

    animation: fadeUp 0.8s ease;
}

.hero-content {
    position: relative;
    z-index: 4;

    max-width: 720px;
}

.eyebrow {
    display: inline-block;

    padding: 0.55rem 0.9rem;

    border-radius: 100px;

    background: rgba(232,185,154,0.15);

    color: #9C684D;

    font-size: 0.72rem;
    font-weight: 700;

    letter-spacing: 0.15em;

    text-transform: uppercase;
}

.hero h1 {
    font-family: "Playfair Display", serif;

    font-size: clamp(
        3.5rem,
        7vw,
        6.4rem
    );

    line-height: 0.96;

    margin: 1.3rem 0 0;

    letter-spacing: -0.055em;

    color: var(--ink);
}

.hero h1 em {
    font-style: normal;
    color: var(--peach);
}

.hero-subtitle {
    margin-top: 1.5rem;

    font-family: "Playfair Display", serif;

    font-size: 1.42rem;

    color: var(--olive);
}

.hero-description {
    max-width: 630px;

    margin-top: 1.1rem;

    color: var(--ink-soft);

    line-height: 1.8;

    font-size: 1rem;
}


/* =========================================================
   HERO ORBIT
   ========================================================= */

.hero-visual {
    position: absolute;

    right: 7%;
    top: 18%;

    width: 330px;
    height: 330px;

    display: flex;
    align-items: center;
    justify-content: center;
}

.orbit {
    position: absolute;

    width: 285px;
    height: 285px;

    border: 1px solid rgba(101,116,93,0.20);

    border-radius: 50%;

    animation: spin 22s linear infinite;
}

.orbit::before {
    content: "";

    position: absolute;

    width: 20px;
    height: 20px;

    top: -10px;
    left: 50%;

    border-radius: 50%;

    background: var(--peach);

    box-shadow:
        0 0 28px rgba(232,185,154,0.65);
}

.orbit::after {
    content: "";

    position: absolute;

    width: 13px;
    height: 13px;

    right: -6px;
    top: 50%;

    border-radius: 50%;

    background: var(--gold);
}

.hero-core {
    width: 145px;
    height: 145px;

    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    background:
        linear-gradient(
            145deg,
            #FFFFFF,
            #F3E9DB
        );

    border: 1px solid rgba(201,166,107,0.30);

    box-shadow:
        0 20px 55px rgba(72,75,65,0.13);

    font-family: "Playfair Display", serif;

    font-size: 1.7rem;

    color: var(--olive);

    animation: softPulse 5s ease-in-out infinite;
}


/* =========================================================
   TAGLINE
   ========================================================= */

.tagline {
    text-align: center;

    margin: 2rem 0 3rem;

    font-size: 0.78rem;

    font-weight: 700;

    letter-spacing: 0.18em;

    color: var(--olive);
}

.tagline span {
    color: var(--peach);

    margin: 0 0.7rem;
}


/* =========================================================
   SECTION HEADINGS
   ========================================================= */

.section-label {
    color: #A57A59;

    font-size: 0.72rem;

    font-weight: 700;

    letter-spacing: 0.16em;

    text-transform: uppercase;
}

.section-title {
    font-family: "Playfair Display", serif;

    color: var(--ink);

    font-size: clamp(
        2.3rem,
        4vw,
        3.4rem
    );

    line-height: 1.05;

    margin-top: 0.35rem;

    letter-spacing: -0.025em;
}

.section-text {
    color: var(--ink-soft);

    max-width: 720px;

    line-height: 1.75;
}


/* =========================================================
   HOME FEATURE CARDS
   ========================================================= */

.feature-grid {
    margin-top: 2rem;
}

.feature-card {
    position: relative;

    min-height: 245px;

    padding: 2rem;

    border-radius: 28px;

    background:
        rgba(255,255,255,0.76);

    border:
        1px solid rgba(41,51,46,0.08);

    box-shadow:
        0 12px 35px rgba(41,51,46,0.055);

    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease;

    animation: fadeUp 0.7s ease;
}

.feature-card:hover {
    transform: translateY(-8px);

    box-shadow:
        0 24px 50px rgba(41,51,46,0.10);
}

.feature-number {
    font-family: "Playfair Display", serif;

    font-size: 3rem;

    color: var(--peach-soft);

    line-height: 1;
}

.feature-icon {
    font-size: 1.8rem;

    margin-top: 0.4rem;
}

.feature-card h3 {
    font-family: "Playfair Display", serif;

    color: var(--ink);

    font-size: 1.45rem;

    margin-top: 0.8rem;
}

.feature-card p {
    color: var(--ink-soft);

    font-size: 0.92rem;

    line-height: 1.7;
}


/* =========================================================
   JOURNEY INTRO
   ========================================================= */

.journey-banner {
    margin: 2rem 0;

    padding: 1.5rem 1.8rem;

    border-radius: 25px;

    background:
        linear-gradient(
            110deg,
            rgba(221,230,215,0.65),
            rgba(245,222,208,0.45)
        );

    border: 1px solid rgba(41,51,46,0.06);

    animation: fadeUp 0.7s ease;
}


/* =========================================================
   QUESTIONNAIRE
   ========================================================= */

.question-wrapper {
    max-width: 980px;

    margin: 2rem auto 0;

    animation: fadeUp 0.55s ease;
}

.question-header {
    text-align: center;

    margin-bottom: 1.8rem;
}

.question-card {
    padding: 3rem;

    border-radius: 36px;

    background:
        rgba(255,255,255,0.84);

    border:
        1px solid rgba(41,51,46,0.08);

    box-shadow:
        0 25px 70px rgba(41,51,46,0.085);
}

.question-count {
    color: #A57A59;

    font-size: 0.74rem;

    font-weight: 700;

    letter-spacing: 0.15em;

    text-transform: uppercase;
}

.question-title {
    font-family: "Playfair Display", serif;

    color: var(--ink);

    font-size: 2.35rem;

    line-height: 1.15;

    margin-top: 0.6rem;
}

.question-help {
    color: var(--ink-soft);

    line-height: 1.7;

    margin-bottom: 1.7rem;
}


/* Progress */

.progress-background {
    height: 8px;

    background: #EAE8DF;

    border-radius: 100px;

    overflow: hidden;

    margin: 0.8rem 0 2rem;
}

.progress-value {
    height: 100%;

    border-radius: 100px;

    background:
        linear-gradient(
            90deg,
            #9CAF91,
            #E3B28F
        );

    transition: width 0.5s ease;
}


/* =========================================================
   CHOICE CARDS
   ========================================================= */

.choice-title {
    color: var(--ink);

    font-weight: 600;

    margin-bottom: 0.4rem;
}

.choice-description {
    color: var(--ink-soft);

    font-size: 0.86rem;

    line-height: 1.55;
}


/* =========================================================
   NUMBER INPUT
   ========================================================= */

div[data-testid="stNumberInput"] input {
    background: #FFFDF9 !important;

    border: 1px solid rgba(41,51,46,0.12) !important;

    border-radius: 17px !important;

    color: var(--ink) !important;

    min-height: 54px !important;

    font-size: 1rem !important;
}

div[data-testid="stNumberInput"] input:focus {
    border-color: var(--peach) !important;

    box-shadow:
        0 0 0 3px rgba(232,185,154,0.13) !important;
}


/* =========================================================
   WELLNESS DASHBOARD
   ========================================================= */

.metric-card {
    padding: 1.5rem;

    min-height: 150px;

    border-radius: 25px;

    background:
        rgba(255,255,255,0.78);

    border:
        1px solid rgba(41,51,46,0.08);

    box-shadow:
        0 12px 32px rgba(41,51,46,0.05);

    transition: transform 0.25s ease;
}

.metric-card:hover {
    transform: translateY(-5px);
}

.metric-icon {
    font-size: 1.3rem;
}

.metric-label {
    margin-top: 0.65rem;

    color: var(--ink-soft);

    font-size: 0.72rem;

    font-weight: 700;

    letter-spacing: 0.09em;

    text-transform: uppercase;
}

.metric-value {
    margin-top: 0.25rem;

    font-family: "Playfair Display", serif;

    color: var(--ink);

    font-size: 1.7rem;
}


/* =========================================================
   BODY TYPE
   ========================================================= */

.type-card {
    min-height: 285px;

    padding: 2rem;

    border-radius: 30px;

    background:
        rgba(255,255,255,0.80);

    border:
        1px solid rgba(41,51,46,0.08);

    box-shadow:
        0 15px 38px rgba(41,51,46,0.055);

    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease;
}

.type-card:hover {
    transform: translateY(-8px);

    box-shadow:
        0 25px 55px rgba(41,51,46,0.10);
}

.type-icon {
    font-size: 2rem;
}

.type-card h3 {
    font-family: "Playfair Display", serif;

    color: var(--ink);

    font-size: 1.65rem;
}

.type-subtitle {
    color: #A57A59;

    font-size: 0.72rem;

    font-weight: 700;

    letter-spacing: 0.10em;

    text-transform: uppercase;
}

.type-card p {
    color: var(--ink-soft);

    line-height: 1.7;
}


/* =========================================================
   RESULT
   ========================================================= */

.result-card {
    position: relative;

    overflow: hidden;

    text-align: center;

    margin-top: 2rem;

    padding: 3.2rem;

    border-radius: 36px;

    background:
        linear-gradient(
            135deg,
            rgba(221,230,215,0.72),
            rgba(245,222,208,0.60)
        );

    border: 1px solid rgba(41,51,46,0.07);

    box-shadow:
        0 22px 60px rgba(41,51,46,0.08);
}

.result-card::after {
    content: "";

    position: absolute;

    width: 250px;
    height: 250px;

    border-radius: 50%;

    right: -100px;
    top: -100px;

    background: rgba(255,255,255,0.35);
}

.result-card h2 {
    position: relative;
    z-index: 2;

    font-family: "Playfair Display", serif;

    font-size: 3rem;

    color: var(--ink);
}


/* =========================================================
   CHALLENGE
   ========================================================= */

.challenge-shell {
    max-width: 900px;

    margin: 2rem auto;

    animation: fadeUp 0.6s ease;
}

.challenge-card {
    position: relative;

    overflow: hidden;

    text-align: center;

    padding: 3.5rem 2.5rem;

    border-radius: 38px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.90),
            rgba(249,239,228,0.78)
        );

    border: 1px solid rgba(41,51,46,0.08);

    box-shadow:
        0 25px 75px rgba(41,51,46,0.10);
}

.challenge-number {
    color: #A57A59;

    font-size: 0.72rem;

    font-weight: 700;

    letter-spacing: 0.16em;

    text-transform: uppercase;
}

.challenge-icon {
    width: 85px;
    height: 85px;

    margin: 0 auto 1.2rem;

    border-radius: 50%;

    display: flex;
    align-items: center;
    justify-content: center;

    background:
        linear-gradient(
            145deg,
            #EED4C4,
            #E4EBD9
        );

    font-size: 2rem;

    animation: floating 4s ease-in-out infinite;
}

.challenge-card h2 {
    font-family: "Playfair Display", serif;

    color: var(--ink);

    font-size: 2.7rem;
}

.challenge-task {
    max-width: 620px;

    margin: 1rem auto;

    color: var(--ink-soft);

    line-height: 1.8;

    font-size: 1rem;
}


/* =========================================================
   REWARD REVEAL
   ========================================================= */

.reward-card {
    text-align: center;

    padding: 2.2rem;

    margin-top: 1.5rem;

    border-radius: 30px;

    background:
        linear-gradient(
            135deg,
            #F7EBD7,
            #E5ECDD
        );

    border: 1px solid rgba(201,166,107,0.25);

    animation: fadeUp 0.6s ease;
}

.badge {
    display: inline-flex;

    align-items: center;
    justify-content: center;

    width: 92px;
    height: 92px;

    border-radius: 50%;

    background: #FFFFFF;

    border: 3px solid var(--gold);

    font-size: 2.2rem;

    box-shadow:
        0 12px 35px rgba(201,166,107,0.18);
}

.reward-card h3 {
    font-family: "Playfair Display", serif;

    color: var(--ink);

    font-size: 1.7rem;
}


/* =========================================================
   STREAK
   ========================================================= */

.streak-hero {
    text-align: center;

    padding: 3rem;

    border-radius: 36px;

    background:
        linear-gradient(
            135deg,
            rgba(221,230,215,0.72),
            rgba(255,255,255,0.75)
        );

    border: 1px solid rgba(41,51,46,0.07);

    box-shadow:
        0 20px 60px rgba(41,51,46,0.07);
}

.streak-number {
    font-family: "Playfair Display", serif;

    font-size: 5rem;

    color: var(--ink);

    line-height: 1;
}

.streak-word {
    color: #A57A59;

    text-transform: uppercase;

    font-size: 0.75rem;

    font-weight: 700;

    letter-spacing: 0.18em;
}

.day-box {
    text-align: center;

    padding: 1rem 0.4rem;

    border-radius: 19px;

    border: 1px solid rgba(41,51,46,0.08);

    background: rgba(255,255,255,0.72);

    transition: transform 0.25s ease;
}

.day-box:hover {
    transform: translateY(-4px);
}

.day-active {
    background:
        linear-gradient(
            145deg,
            #879A7C,
            #AAB99F
        );

    color: white;

    border: none;
}

.day-letter {
    font-size: 0.72rem;

    font-weight: 700;
}


/* =========================================================
   BADGES
   ========================================================= */

.badges-title {
    font-family: "Playfair Display", serif;

    color: var(--ink);

    font-size: 2rem;
}

.badge-small {
    text-align: center;

    padding: 1.3rem 0.7rem;

    border-radius: 22px;

    background: rgba(255,255,255,0.75);

    border: 1px solid rgba(41,51,46,0.08);

    min-height: 145px;
}

.badge-small-icon {
    font-size: 2rem;
}

.badge-small-name {
    margin-top: 0.6rem;

    color: var(--ink);

    font-size: 0.82rem;

    font-weight: 700;
}

.badge-locked {
    opacity: 0.35;
    filter: grayscale(1);
}


/* =========================================================
   RECOMMENDATIONS
   ========================================================= */

.recommendation {
    padding: 1.8rem;

    margin-bottom: 1rem;

    border-radius: 26px;

    background:
        rgba(255,255,255,0.78);

    border: 1px solid rgba(41,51,46,0.08);

    box-shadow:
        0 10px 28px rgba(41,51,46,0.045);

    transition: transform 0.25s ease;
}

.recommendation:hover {
    transform: translateX(5px);
}

.recommendation-icon {
    font-size: 1.6rem;
}

.recommendation h3 {
    font-family: "Playfair Display", serif;

    color: var(--ink);

    font-size: 1.35rem;
}

.recommendation p {
    color: var(--ink-soft);

    line-height: 1.7;
}


/* =========================================================
   EMPTY STATES
   ========================================================= */

.empty-state {
    max-width: 850px;

    margin: 4rem auto;

    padding: 4rem 2rem;

    text-align: center;

    border-radius: 38px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.82),
            rgba(244,239,229,0.72)
        );

    border: 1px dashed rgba(101,116,93,0.22);

    box-shadow:
        0 18px 50px rgba(41,51,46,0.06);

    animation: fadeUp 0.7s ease;
}

.empty-icon {
    font-size: 3rem;

    animation: floating 4s ease-in-out infinite;
}

.empty-state h2 {
    font-family: "Playfair Display", serif;

    color: var(--ink);

    font-size: 2.4rem;
}

.empty-state p {
    max-width: 560px;

    margin: auto;

    color: var(--ink-soft);

    line-height: 1.8;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    margin-top: 5rem;

    padding-top: 2rem;

    border-top:
        1px solid rgba(41,51,46,0.08);

    text-align: center;

    color: #7A837D;

    font-size: 0.78rem;

    line-height: 1.8;
}


/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 900px) {

    .hero {
        padding: 3rem 2rem;
        min-height: 650px;
    }

    .hero-visual {
        opacity: 0.35;
        right: 50%;
        transform: translateX(50%);
        top: 55%;
    }

    .hero h1 {
        font-size: 4rem;
    }

    .question-card {
        padding: 2rem 1.3rem;
    }

    .question-title {
        font-size: 1.9rem;
    }
}

</style>

<div class="motion-orb orb-1"></div>
<div class="motion-orb orb-2"></div>
<div class="motion-orb orb-3"></div>
""",
    unsafe_allow_html=True
)


# =========================================================
# QUESTION DATA
# =========================================================

questions = [

    {
        "section": "A little about you",
        "q": "How old are you?",
        "type": "number",
        "key": "age",
        "help": "This helps place your answers in the right wellness context.",
        "unit": "years"
    },

    {
        "section": "A little about you",
        "q": "How would you like MYBIO to address you?",
        "type": "choice",
        "key": "sex",
        "options": [
            "Female",
            "Male",
            "Prefer not to say"
        ]
    },

    {
        "section": "A little about you",
        "q": "How tall are you?",
        "type": "number",
        "key": "height",
        "help": "Enter your height in centimetres.",
        "unit": "cm"
    },

    {
        "section": "A little about you",
        "q": "What is your current weight?",
        "type": "number",
        "key": "weight",
        "help": "An approximate value is perfectly fine.",
        "unit": "kg"
    },

    {
        "section": "What matters to you",
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
        ]
    },

    {
        "section": "Your everyday rhythm",
        "q": "What does a normal day look like for movement?",
        "type": "choice",
        "key": "activity",
        "options": [
            "Mostly seated",
            "Light movement",
            "Regularly active",
            "Highly active"
        ]
    },

    {
        "section": "Your natural tendencies",
        "q": "Which description feels closest to your natural build?",
        "type": "dosha",
        "key": "build",
        "options": {
            "Vata": "Naturally light or lean, with a tendency to find gaining weight difficult.",
            "Pitta": "Moderate build, with a tendency to maintain weight relatively easily.",
            "Kapha": "Solid or fuller build, with a tendency to gain weight more easily."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "How does your appetite usually behave?",
        "type": "dosha",
        "key": "appetite",
        "options": {
            "Vata": "It can change from day to day.",
            "Pitta": "It is usually strong and fairly predictable.",
            "Kapha": "It is generally moderate, and I can go longer between meals."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "Which sounds closest to your digestion?",
        "type": "dosha",
        "key": "digestion",
        "options": {
            "Vata": "Sometimes irregular, with occasional bloating.",
            "Pitta": "Usually strong, sometimes with acidity.",
            "Kapha": "Generally slower, sometimes with a feeling of heaviness."
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
        "q": "How does your energy usually move through the day?",
        "type": "dosha",
        "key": "energy",
        "options": {
            "Vata": "Quick bursts of energy, but not always consistent.",
            "Pitta": "Focused, driven and fairly strong.",
            "Kapha": "Slower to begin, but steady once I get going."
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
            "Kapha": "Deep and longer, and waking can take effort."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "Which temperament feels most familiar?",
        "type": "dosha",
        "key": "temperament",
        "options": {
            "Vata": "Creative, curious, energetic and sometimes restless.",
            "Pitta": "Focused, ambitious and decisive.",
            "Kapha": "Calm, patient, steady and relaxed."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "How does your weight usually respond?",
        "type": "dosha",
        "key": "weight_response",
        "options": {
            "Vata": "I generally find gaining weight difficult.",
            "Pitta": "My weight tends to change moderately.",
            "Kapha": "I tend to gain weight relatively easily."
        }
    },

    {
        "section": "Your natural tendencies",
        "q": "How structured is your daily routine?",
        "type": "dosha",
        "key": "routine",
        "options": {
            "Vata": "It can be quite unpredictable.",
            "Pitta": "It is fairly organised.",
            "Kapha": "It is regular, although I can sometimes be inactive."
        }
    },

    {
        "section": "Your wellness context",
        "q": "Has a healthcare professional diagnosed you with any of these?",
        "type": "choice",
        "key": "condition",
        "options": [
            "None",
            "Type 2 diabetes",
            "PCOS",
            "Hypothyroidism",
            "Cushing's syndrome",
            "Fatty liver",
            "Another metabolic or endocrine condition"
        ],
        "help": "This is only considered as wellness and safety context."
    },

    {
        "section": "Your wellness context",
        "q": "Do you currently take medication that may influence weight or appetite?",
        "type": "choice",
        "key": "medication",
        "options": [
            "No",
            "Yes"
        ],
        "help": "Medication-related decisions should always involve a healthcare professional."
    },

    {
        "section": "Your nourishment",
        "q": "Which eating pattern best represents you?",
        "type": "choice",
        "key": "diet",
        "options": [
            "Vegetarian",
            "Non-vegetarian",
            "Eggetarian"
        ]
    },

    {
        "section": "Your nourishment",
        "q": "How many meals do you usually have?",
        "type": "choice",
        "key": "meals",
        "options": [
            "1",
            "2",
            "3",
            "4 or more"
        ]
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
        ]
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
        ]
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
        ]
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
        ]
    },

    {
        "section": "Your daily rhythm",
        "q": "How much intentional movement do you usually get?",
        "type": "number",
        "key": "activity_minutes",
        "help": "Approximate minutes per day are enough.",
        "unit": "minutes"
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
        ]
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
        ]
    }
]


# =========================================================
# CHALLENGE DATA
# =========================================================

challenges_data = [

    {
        "title": "The Hydration Pause",
        "icon": "💧",
        "task": "Take a quiet pause and have one full glass of water. No rush. Just notice the moment.",
        "reward": "Hydration Hero",
        "badge": "💧",
        "xp": 20
    },

    {
        "title": "The Movement Minute",
        "icon": "🌿",
        "task": "Give yourself ten minutes of movement today — a walk, a stretch or anything that gets you moving.",
        "reward": "Move With Intention",
        "badge": "🌿",
        "xp": 25
    },

    {
        "title": "The Mindful Plate",
        "icon": "🥣",
        "task": "During one meal today, slow down for a moment and notice your hunger, your food and how you feel while eating.",
        "reward": "Mindful Nourisher",
        "badge": "🥣",
        "xp": 25
    },

    {
        "title": "The Evening Reset",
        "icon": "🌙",
        "task": "Give your mind twenty screen-free minutes before bedtime and let the day become a little quieter.",
        "reward": "Evening Guardian",
        "badge": "🌙",
        "xp": 30
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

    ordered = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    if ordered[0][1] == ordered[1][1] == ordered[2][1]:
        return "Balanced"

    if ordered[0][1] == ordered[1][1]:
        return f"{ordered[0][0]}–{ordered[1][0]}"

    return ordered[0][0]


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


def completed_badges():

    completed = st.session_state.completed_challenges

    return [
        challenges_data[i]
        for i in completed
        if i < len(challenges_data)
    ]


# =========================================================
# BRAND HEADER
# =========================================================

st.markdown(
    """
<div class="brand-row">

    <div>
        <div class="brand">MY<span>BIO</span></div>

        <div class="brand-caption">
            Your personal wellness journey
        </div>
    </div>

</div>
""",
    unsafe_allow_html=True
)


# =========================================================
# NAVIGATION
# =========================================================

nav_items = [
    ("Home", "Home"),
    ("Begin Journey", "Questionnaire"),
    ("My Wellness", "Body"),
    ("Body Type", "Ayurvedic"),
    ("Today's Challenge", "Challenges"),
    ("My Rhythm", "Streak"),
    ("For You", "Recommendations"),
    ("About", "About")
]

nav_cols = st.columns(len(nav_items))

for col, (label, page) in zip(nav_cols, nav_items):

    with col:

        if st.button(
            label,
            key=f"nav_{page}",
            use_container_width=True
        ):
            navigate(page)


st.markdown("<br>", unsafe_allow_html=True)


# =========================================================
# HOME
# =========================================================

def home():

    st.markdown(
        """
<div class="hero">

    <div class="hero-content">

        <div class="eyebrow">
            ✦ A different way to know yourself
        </div>

        <h1>
            Meet the<br>
            <em>you</em> within.
        </h1>

        <div class="hero-subtitle">
            Ancient wisdom. Modern you. Infinite possibilities.
        </div>

        <p class="hero-description">
            MYBIO is a space to pause, reflect and understand the
            patterns that make your everyday life uniquely yours.
            Discover your wellness story, explore an Ayurvedic
            perspective and take small steps that feel right for you.
        </p>

    </div>


    <div class="hero-visual">

        <div class="orbit"></div>

        <div class="hero-core">
            MYBIO
        </div>

    </div>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="tagline">

    ANCIENT WISDOM
    <span>✦</span>
    MODERN YOU
    <span>✦</span>
    INFINITE POSSIBILITIES

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div style="text-align:center;">

    <div class="section-label">
        YOUR STORY STARTS HERE
    </div>

    <div class="section-title">
        Wellness should feel personal.
    </div>

    <p class="section-text" style="margin:auto;">
        Not another list of things you should do.
        Not another place telling you to be perfect.
        Just a space to understand yourself a little better —
        and begin from there.
    </p>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    cols = st.columns(3)

    features = [

        (
            "01",
            "◌",
            "Discover Yourself",
            "Reflect on your everyday habits, energy, nourishment,
            movement and natural tendencies."
        ),

        (
            "02",
            "✦",
            "Find Your Balance",
            "Explore your Ayurvedic Body Type through a simple,
            visual and personal experience."
        ),

        (
            "03",
            "∞",
            "Grow Gently",
            "Turn awareness into small actions that can actually
            fit into your everyday life."
        )
    ]

    for col, (number, icon, title, text) in zip(cols, features):

        with col:

            st.markdown(
                f"""
<div class="feature-card">

    <div class="feature-number">
        {number}
    </div>

    <div class="feature-icon">
        {icon}
    </div>

    <h3>
        {title}
    </h3>

    <p>
        {text}
    </p>

</div>
""",
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="journey-banner">

    <div class="section-label">
        ONE STEP IS ENOUGH
    </div>

    <div style="
        font-family:'Playfair Display',serif;
        font-size:1.5rem;
        color:#29332E;
        margin-top:0.3rem;">
        You don't have to change your whole life today.
        You only have to begin.
    </div>

</div>
""",
        unsafe_allow_html=True
    )

    if st.session_state.profile_complete:

        st.markdown(
            '<div class="primary-btn">',
            unsafe_allow_html=True
        )

        if st.button(
            "Continue my journey  →",
            key="home_continue",
            use_container_width=True
        ):
            navigate("Body")

        st.markdown("</div>", unsafe_allow_html=True)

    else:

        st.markdown(
            '<div class="primary-btn">',
            unsafe_allow_html=True
        )

        if st.button(
            "Begin your MYBIO journey  →",
            key="home_begin",
            use_container_width=True
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

    progress = ((index) / total) * 100

    st.markdown(
        """
<div class="question-header">

    <div class="section-label">
        YOUR MYBIO JOURNEY
    </div>

    <div class="section-title">
        Let's start with you.
    </div>

    <p class="section-text" style="margin:auto;">
        There are no perfect answers here.
        Choose what feels most naturally true.
    </p>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
<div class="progress-background">

    <div class="progress-value"
         style="width:{progress}%;"></div>

</div>

<div style="
    text-align:right;
    color:#7A837D;
    font-size:0.75rem;
    margin-bottom:1rem;">
    {index + 1:02d} / {total:02d}
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="question-wrapper"><div class="question-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
<div class="question-count">
    {question["section"]}
</div>

<div class="question-title">
    {question["q"]}
</div>
""",
        unsafe_allow_html=True
    )

    if question.get("help"):

        st.markdown(
            f"""
<div class="question-help">
    {question["help"]}
</div>
""",
            unsafe_allow_html=True
        )

    current = st.session_state.answers.get(
        question["key"]
    )


    # -----------------------------------------------------
    # NUMBER
    # -----------------------------------------------------

    if question["type"] == "number":

        value = st.number_input(
            question.get("unit", ""),
            min_value=1.0,
            max_value=250.0,
            value=float(current) if current else 1.0,
            step=1.0,
            key=f"number_{question['key']}"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            '<div class="primary-btn">',
            unsafe_allow_html=True
        )

        if st.button(
            "Continue  →",
            key=f"continue_{question['key']}",
            use_container_width=True
        ):

            st.session_state.answers[
                question["key"]
            ] = value

            if index < total - 1:

                st.session_state.question_index += 1

                st.rerun()

            else:

                finish_questionnaire()

        st.markdown("</div>", unsafe_allow_html=True)


    # -----------------------------------------------------
    # DOSHA / BODY TYPE
    # -----------------------------------------------------

    elif question["type"] == "dosha":

        options = list(
            question["options"].items()
        )

        cols = st.columns(3)

        for col, (name, description) in zip(
            cols,
            options
        ):

            with col:

                selected = current == name

                if selected:

                    border = (
                        "2px solid #C9A66B;"
                        "background:#F8F1E6;"
                    )

                    button_text = "Chosen ✓"

                else:

                    border = (
                        "1px solid rgba(41,51,46,0.09);"
                    )

                    button_text = "Choose this"

                st.markdown(
                    f"""
<div style="
    min-height:190px;
    padding:1.5rem;
    border-radius:24px;
    border:{border};
    box-shadow:0 8px 25px rgba(41,51,46,0.05);
    margin-bottom:0.8rem;">

    <div style="
        font-family:'Playfair Display',serif;
        color:#29332E;
        font-size:1.4rem;
        font-weight:600;">
        {name}
    </div>

    <div style="
        color:#56625B;
        font-size:0.86rem;
        line-height:1.6;
        margin-top:0.6rem;">
        {description}
    </div>

</div>
""",
                    unsafe_allow_html=True
                )

                if st.button(
                    button_text,
                    key=f"{question['key']}_{name}",
                    use_container_width=True
                ):

                    st.session_state.answers[
                        question["key"]
                    ] = name

                    st.rerun()

        if current:

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(
                '<div class="primary-btn">',
                unsafe_allow_html=True
            )

            if st.button(
                "Continue  →",
                key=f"next_{question['key']}",
                use_container_width=True
            ):

                if index < total - 1:

                    st.session_state.question_index += 1

                    st.rerun()

                else:

                    finish_questionnaire()

            st.markdown("</div>", unsafe_allow_html=True)


    # -----------------------------------------------------
    # NORMAL CHOICE
    # -----------------------------------------------------

    else:

        options = question["options"]

        for start in range(
            0,
            len(options),
            2
        ):

            row = options[
                start:start + 2
            ]

            cols = st.columns(2)

            for col, option in zip(
                cols,
                row
            ):

                with col:

                    selected = current == option

                    if selected:

                        st.markdown(
                            f"""
<div style="
    padding:1.15rem 1.3rem;
    border-radius:20px;
    background:#F8F1E6;
    border:2px solid #C9A66B;
    margin-bottom:0.4rem;">

    <div class="choice-title">
        {option}
    </div>

    <div style="
        color:#A57A59;
        font-size:0.72rem;
        font-weight:700;
        margin-top:0.25rem;">
        SELECTED ✓
    </div>

</div>
""",
                            unsafe_allow_html=True
                        )

                    else:

                        st.markdown(
                            f"""
<div style="
    padding:1.15rem 1.3rem;
    border-radius:20px;
    background:rgba(255,255,255,0.65);
    border:1px solid rgba(41,51,46,0.08);
    margin-bottom:0.4rem;">

    <div class="choice-title">
        {option}
    </div>

</div>
""",
                            unsafe_allow_html=True
                        )

                    if st.button(
                        "Selected ✓"
                        if selected
                        else "Choose",
                        key=f"{question['key']}_{option}",
                        use_container_width=True
                    ):

                        st.session_state.answers[
                            question["key"]
                        ] = option

                        st.rerun()

        if current:

            st.markdown("<br>", unsafe_allow_html=True)

            st.markdown(
                '<div class="primary-btn">',
                unsafe_allow_html=True
            )

            if st.button(
                "Continue  →",
                key=f"next_{question['key']}",
                use_container_width=True
            ):

                if index < total - 1:

                    st.session_state.question_index += 1

                    st.rerun()

                else:

                    finish_questionnaire()

            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        "</div></div>",
        unsafe_allow_html=True
    )

    if index > 0:

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "← Go back",
            key="previous_question"
        ):

            st.session_state.question_index -= 1

            st.rerun()


# =========================================================
# WELLNESS DASHBOARD
# =========================================================

def body():

    if not st.session_state.profile_complete:

        st.markdown(
            """
<div class="empty-state">

    <div class="empty-icon">
        ✦
    </div>

    <div class="section-label">
        YOUR SPACE IS WAITING
    </div>

    <h2>
        Something beautiful begins with knowing yourself.
    </h2>

    <p>
        Complete your first MYBIO journey and this space
        will begin reflecting your personal wellness story.
    </p>

</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="primary-btn">',
            unsafe_allow_html=True
        )

        if st.button(
            "Begin my journey  →",
            use_container_width=True
        ):
            navigate("Questionnaire")

        st.markdown("</div>", unsafe_allow_html=True)

        return

    bmi = bmi_value()

    st.markdown(
        """
<div class="section-label">
    YOUR WELLNESS SPACE
</div>

<div class="section-title">
    A picture of where you are.
</div>

<p class="section-text">
    Your journey isn't about becoming someone else.
    It is about noticing yourself — and choosing what
    deserves your attention today.
</p>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    metrics = [

        (
            "✦",
            "Current rhythm",
            f"{st.session_state.streak} day"
        ),

        (
            "◌",
            "Journey points",
            f"{st.session_state.xp} XP"
        ),

        (
            "☀",
            "Ayurvedic Body Type",
            st.session_state.ayurvedic_type
        ),

        (
            "∞",
            "BMI",
            f"{bmi:.1f}" if bmi else "—"
        )
    ]

    cols = st.columns(4)

    for col, (icon, label, value) in zip(
        cols,
        metrics
    ):

        with col:

            st.markdown(
                f"""
<div class="metric-card">

    <div class="metric-icon">
        {icon}
    </div>

    <div class="metric-label">
        {label}
    </div>

    <div class="metric-value">
        {value}
    </div>

</div>
""",
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="journey-banner">

    <div class="section-label">
        TODAY'S THOUGHT
    </div>

    <div style="
        font-family:'Playfair Display',serif;
        font-size:1.45rem;
        color:#29332E;
        margin-top:0.4rem;">
        Small choices are still choices.
        You don't need a perfect day to make a meaningful one.
    </div>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="primary-btn">',
        unsafe_allow_html=True
    )

    if st.button(
        "See today's challenge  →",
        use_container_width=True
    ):
        navigate("Challenges")

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# AYURVEDIC BODY TYPE
# =========================================================

def ayurvedic():

    if not st.session_state.profile_complete:

        st.markdown(
            """
<div class="empty-state">

    <div class="empty-icon">
        ◌
    </div>

    <div class="section-label">
        SOMETHING IS UNFOLDING
    </div>

    <h2>
        Your natural wellness pattern is waiting.
    </h2>

    <p>
        Complete your MYBIO journey first.
        Then come back here to explore your Ayurvedic Body Type.
    </p>

</div>
""",
            unsafe_allow_html=True
        )

        return

    st.markdown(
        """
<div class="section-label">
    ANCIENT PERSPECTIVE
</div>

<div class="section-title">
    Your Ayurvedic Body Type
</div>

<p class="section-text">
    Ayurveda describes three broad tendencies associated with
    movement, transformation and stability. Your result is an
    introductory wellness interpretation based on your responses.
</p>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    types = [

        (
            "Vata",
            "◌",
            "Movement & adaptability",
            "Often associated with lightness, creativity,
            variability and movement."
        ),

        (
            "Pitta",
            "☀",
            "Transformation & focus",
            "Often associated with intensity, focus,
            warmth and purposeful action."
        ),

        (
            "Kapha",
            "◒",
            "Stability & grounding",
            "Often associated with steadiness,
            endurance, calmness and grounding."
        )
    ]

    cols = st.columns(3)

    for col, (
        name,
        icon,
        subtitle,
        description
    ) in zip(cols, types):

        with col:

            if name in st.session_state.ayurvedic_type:

                border = (
                    "2px solid #C9A66B;"
                    "background:#FAF4E9;"
                )

            else:

                border = (
                    "1px solid rgba(41,51,46,0.08);"
                )

            st.markdown(
                f"""
<div class="type-card"
     style="border:{border};">

    <div class="type-icon">
        {icon}
    </div>

    <h3>
        {name}
    </h3>

    <div class="type-subtitle">
        {subtitle}
    </div>

    <p>
        {description}
    </p>

</div>
""",
                unsafe_allow_html=True
            )

    st.markdown(
        f"""
<div class="result-card">

    <div class="section-label">
        YOUR RESULT
    </div>

    <h2>
        {st.session_state.ayurvedic_type}
    </h2>

    <p style="
        position:relative;
        z-index:2;
        color:#56625B;
        max-width:600px;
        margin:auto;
        line-height:1.8;">
        This is the pattern that appeared most strongly
        across your responses in this introductory experience.
    </p>

</div>
""",
        unsafe_allow_html=True
    )

    st.caption(
        "MYBIO provides an educational wellness interpretation "
        "and does not replace medical diagnosis or professional care."
    )


# =========================================================
# CHALLENGES
# =========================================================

def challenges():

    if not st.session_state.profile_complete:

        st.markdown(
            """
<div class="empty-state">

    <div class="empty-icon">
        ✦
    </div>

    <div class="section-label">
        YOUR NEXT STEP
    </div>

    <h2>
        Your first little challenge is waiting.
    </h2>

    <p>
        Begin your MYBIO journey first.
        Once you are ready, one small action will appear here —
        never a hundred things at once.
    </p>

</div>
""",
            unsafe_allow_html=True
        )

        return

    completed = st.session_state.completed_challenges

    remaining = [
        i
        for i in range(len(challenges_data))
        if i not in completed
    ]

    # -----------------------------------------------------
    # ALL CHALLENGES COMPLETE
    # -----------------------------------------------------

    if not remaining:

        st.markdown(
            """
<div class="empty-state">

    <div class="empty-icon">
        ✦
    </div>

    <div class="section-label">
        LOOK HOW FAR YOU'VE COME
    </div>

    <h2>
        You showed up for yourself.
    </h2>

    <p>
        Every small action became part of your rhythm.
        There is nothing left to prove — just more to discover.
    </p>

</div>
""",
            unsafe_allow_html=True
        )

        return

    current_index = remaining[0]

    challenge = challenges_data[
        current_index
    ]

    st.markdown(
        """
<div style="text-align:center;">

    <div class="section-label">
        ONE SMALL STEP
    </div>

    <div class="section-title">
        Today's Challenge
    </div>

    <p class="section-text" style="margin:auto;">
        You don't need to change everything.
        Just do this one thing.
    </p>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        '<div class="challenge-shell">',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
<div class="challenge-card">

    <div class="challenge-icon">
        {challenge["icon"]}
    </div>

    <div class="challenge-number">
        STEP {len(completed) + 1}
    </div>

    <h2>
        {challenge["title"]}
    </h2>

    <div class="challenge-task">
        {challenge["task"]}
    </div>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # -----------------------------------------------------
    # START
    # -----------------------------------------------------

    if not st.session_state.started:

        st.markdown(
            '<div class="primary-btn">',
            unsafe_allow_html=True
        )

        if st.button(
            "Start this challenge  →",
            key=f"start_{current_index}",
            use_container_width=True
        ):

            st.session_state.started = True

            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # -----------------------------------------------------
    # IN PROGRESS
    # -----------------------------------------------------

    else:

        st.markdown(
            """
<div style="
    text-align:center;
    padding:1rem;
    color:#65745D;
    font-weight:600;">
    ✦ Take your time. Come back when you've done it.
</div>
""",
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="primary-btn">',
            unsafe_allow_html=True
        )

        if st.button(
            "I completed it  ✓",
            key=f"complete_{current_index}",
            use_container_width=True
        ):

            st.session_state.completed_challenges.append(
                current_index
            )

            st.session_state.xp += challenge["xp"]

            st.session_state.streak += 1

            st.session_state.started = False

            st.session_state.last_completed = current_index

            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # -----------------------------------------------------
    # REWARD ONLY AFTER COMPLETION
    # -----------------------------------------------------

    if (
        st.session_state.last_completed
        is not None
        and st.session_state.last_completed
        == current_index
    ):

        st.markdown(
            f"""
<div class="reward-card">

    <div class="badge">
        {challenge["badge"]}
    </div>

    <h3>
        {challenge["reward"]}
    </h3>

    <p style="color:#56625B;">
        +{challenge["xp"]} XP
    </p>

</div>
""",
            unsafe_allow_html=True
        )


# =========================================================
# STREAK / RHYTHM
# =========================================================

def streak():

    if not st.session_state.profile_complete:

        st.markdown(
            """
<div class="empty-state">

    <div class="empty-icon">
        ✧
    </div>

    <div class="section-label">
        YOUR RHYTHM WILL COME
    </div>

    <h2>
        Nothing to count yet.
    </h2>

    <p>
        Begin your journey first.
        Your rhythm will grow naturally from the small things
        you choose to do.
    </p>

</div>
""",
            unsafe_allow_html=True
        )

        return

    current = st.session_state.streak

    st.markdown(
        """
<div style="text-align:center;">

    <div class="section-label">
        YOUR RHYTHM
    </div>

    <div class="section-title">
        Consistency has its own magic.
    </div>

    <p class="section-text" style="margin:auto;">
        A streak isn't about perfection.
        It is simply a reminder that you kept showing up.
    </p>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        f"""
<div class="streak-hero">

    <div class="streak-number">
        {current}
    </div>

    <div class="streak-word">
        day rhythm
    </div>

    <p style="
        color:#56625B;
        margin-top:1rem;">
        Keep going. Your next small step matters.
    </p>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    cols = st.columns(7)

    days = [
        "M",
        "T",
        "W",
        "T",
        "F",
        "S",
        "S"
    ]

    for i, (col, day) in enumerate(
        zip(cols, days)
    ):

        active = i < min(current, 7)

        with col:

            class_name = (
                "day-box day-active"
                if active
                else "day-box"
            )

            symbol = "✦" if active else "·"

            st.markdown(
                f"""
<div class="{class_name}">

    <div class="day-letter">
        {day}
    </div>

    <div style="
        font-size:1.2rem;
        margin-top:0.35rem;">
        {symbol}
    </div>

</div>
""",
                unsafe_allow_html=True
            )

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        """
<div class="badges-title">
    Your badges
</div>

<p style="color:#56625B;">
    Every badge marks something you chose to do for yourself.
</p>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    badges = completed_badges()

    badge_cols = st.columns(4)

    for i, challenge in enumerate(
        challenges_data
    ):

        unlocked = i < len(
            st.session_state.completed_challenges
        )

        with badge_cols[i]:

            class_name = (
                "badge-small"
                if unlocked
                else "badge-small badge-locked"
            )

            icon = (
                challenge["badge"]
                if unlocked
                else "?"
            )

            st.markdown(
                f"""
<div class="{class_name}">

    <div class="badge-small-icon">
        {icon}
    </div>

    <div class="badge-small-name">
        {challenge["reward"]}
    </div>

</div>
""",
                unsafe_allow_html=True
            )


# =========================================================
# RECOMMENDATIONS
# =========================================================

def recommendations():

    if not st.session_state.profile_complete:

        st.markdown(
            """
<div class="empty-state">

    <div class="empty-icon">
        ♡
    </div>

    <div class="section-label">
        SOMETHING MADE FOR YOU
    </div>

    <h2>
        Your space will become personal.
    </h2>

    <p>
        Complete your journey first.
        Then come back for a few thoughtful ideas shaped around
        the answers you shared.
    </p>

</div>
""",
            unsafe_allow_html=True
        )

        return

    answers = st.session_state.answers

    recommendations_list = []

    if answers.get("sleep") in [
        "Less than 5 hours",
        "5–7 hours"
    ]:

        recommendations_list.append(
            (
                "☾",
                "Give rest a little more room",
                "Try creating a consistent wind-down period
                before sleep rather than waiting until you
                are completely exhausted."
            )
        )

    if answers.get("activity") in [
        "Mostly seated",
        "Light movement"
    ]:

        recommendations_list.append(
            (
                "↗",
                "Bring movement into ordinary moments",
                "A short walk, gentle stretch or movement break
                can be easier to maintain than waiting for
                the perfect workout."
            )
        )

    if answers.get("junk") in [
        "Several times",
        "Almost every day"
    ]:

        recommendations_list.append(
            (
                "◉",
                "Change one meal, not everything",
                "Start with one meal that feels more balanced
                and nourishing instead of trying to completely
                redesign your eating habits overnight."
            )
        )

    if answers.get("meal_timing") in [
        "Sometimes irregular",
        "Very irregular"
    ]:

        recommendations_list.append(
            (
                "◷",
                "Create a little rhythm",
                "More predictable meal timings may help your
                day feel less scattered."
            )
        )

    if not recommendations_list:

        recommendations_list.append(
            (
                "✦",
                "Keep what is already working",
                "Your responses suggest several positive patterns.
                Focus on consistency rather than constantly
                adding more."
            )
        )

    st.markdown(
        """
<div class="section-label">
    A LITTLE SOMETHING FOR YOU
</div>

<div class="section-title">
    Your wellness notes.
</div>

<p class="section-text">
    A few gentle ideas based on the patterns you shared.
    Take what feels useful and leave what doesn't.
</p>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    for icon, title, text in recommendations_list:

        st.markdown(
            f"""
<div class="recommendation">

    <div class="recommendation-icon">
        {icon}
    </div>

    <h3>
        {title}
    </h3>

    <p>
        {text}
    </p>

</div>
""",
            unsafe_allow_html=True
        )

    st.caption(
        "MYBIO provides general wellness information and does "
        "not replace professional medical or nutritional advice."
    )


# =========================================================
# ABOUT
# =========================================================

def about():

    st.markdown(
        """
<div style="text-align:center;">

    <div class="section-label">
        THE IDEA BEHIND MYBIO
    </div>

    <div class="section-title">
        Wellness begins with awareness.
    </div>

    <p class="section-text" style="margin:auto;">
        MYBIO was imagined around a simple idea:
        understanding yourself can be the beginning of
        better everyday choices.
    </p>

</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    about_cards = [

        (
            "✦",
            "Ancient perspective. Contemporary experience.",
            "MYBIO brings an Ayurvedic perspective together with
            everyday lifestyle reflection in a way that feels
            familiar, visual and personal."
        ),

        (
            "◌",
            "Designed around the individual.",
            "Instead of overwhelming you with endless information,
            MYBIO creates a simple journey where each step
            builds on the last."
        ),

        (
            "∞",
            "A journey, not a judgement.",
            "There is no perfect version of you waiting at the end.
            The goal is awareness, consistency and small changes
            that feel possible."
        )
    ]

    for icon, title, text in about_cards:

        st.markdown(
            f"""
<div class="feature-card"
     style="margin-bottom:1rem;">

    <div class="feature-icon">
        {icon}
    </div>

    <h3>
        {title}
    </h3>

    <p>
        {text}
    </p>

</div>
""",
            unsafe_allow_html=True
        )


# =========================================================
# ROUTER
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

st.markdown(
    """
<div class="footer">

    <b>MYBIO</b>
    <br>

    Ancient Wisdom
    <span style="color:#C9A66B;">✦</span>
    Modern You
    <span style="color:#C9A66B;">✦</span>
    Infinite Possibilities

    <br><br>

    A personal wellness exploration experience —
    created for awareness, reflection and everyday growth.

</div>
""",
    unsafe_allow_html=True
)
