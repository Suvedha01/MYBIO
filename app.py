import streamlit as st
from datetime import date


# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="MYBIO | Ancient Wisdom, Modern You",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "page": "Home",
    "answers": {},
    "question_index": 0,
    "profile_complete": False,
    "body_type": None,
    "vata": 0,
    "pitta": 0,
    "kapha": 0,
    "xp": 0,
    "streak": 0,
    "completed_challenges": [],
    "badges": [],
    "active_challenge": False,
    "reward": None,
    "last_completion_date": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# DESIGN SYSTEM
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

:root {
    --bg: #F3EEE6;
    --surface: #FFFDF9;
    --surface-2: #F9F4EC;

    --ink: #272D2A;
    --muted: #6E756F;

    --sage: #91A98D;
    --sage-dark: #526B56;
    --sage-soft: #DCE8D9;

    --coral: #D98F78;
    --coral-soft: #F3D6CA;

    --lavender: #AAA4C7;
    --lavender-soft: #E7E3F0;

    --gold: #C39B57;
    --gold-soft: #F0E0BD;

    --line: #E4DCD0;

    --shadow: 0 20px 55px rgba(70, 63, 52, 0.11);
    --shadow-soft: 0 10px 30px rgba(70, 63, 52, 0.08);
}


/* ----------------------------------------------------------
   BASE
---------------------------------------------------------- */

html, body, [class*="css"] {
    font-family: "DM Sans", sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 8% 12%,
            rgba(217,143,120,0.20),
            transparent 24%
        ),
        radial-gradient(
            circle at 92% 10%,
            rgba(145,169,141,0.27),
            transparent 25%
        ),
        radial-gradient(
            circle at 82% 88%,
            rgba(170,164,199,0.17),
            transparent 27%
        ),
        var(--bg);
    color: var(--ink);
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* ----------------------------------------------------------
   ANIMATIONS
---------------------------------------------------------- */

@keyframes float {
    0%, 100% {
        transform: translateY(0px) rotate(0deg);
    }

    50% {
        transform: translateY(-18px) rotate(4deg);
    }
}

@keyframes floatReverse {
    0%, 100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(15px);
    }
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(24px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes pulse {
    0%, 100% {
        transform: scale(1);
        opacity: 0.8;
    }

    50% {
        transform: scale(1.08);
        opacity: 1;
    }
}

@keyframes glow {
    0%, 100% {
        box-shadow: 0 0 0 rgba(217,143,120,0);
    }

    50% {
        box-shadow: 0 0 35px rgba(217,143,120,0.22);
    }
}

@keyframes shimmer {
    0% {
        background-position: -500px 0;
    }

    100% {
        background-position: 500px 0;
    }
}

@keyframes rotate {
    from {
        transform: rotate(0deg);
    }

    to {
        transform: rotate(360deg);
    }
}


/* ----------------------------------------------------------
   STREAMLIT BUTTONS
---------------------------------------------------------- */

.stButton > button {
    border-radius: 16px !important;
    border: 1px solid var(--line) !important;
    background: rgba(255,255,255,0.86) !important;
    color: var(--ink) !important;
    font-family: "DM Sans", sans-serif !important;
    font-weight: 600 !important;
    min-height: 48px !important;
    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        background 0.25s ease !important;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: var(--shadow-soft) !important;
    border-color: var(--sage) !important;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(
        135deg,
        var(--sage-dark),
        #71896F
    ) !important;

    color: white !important;

    border: none !important;

    box-shadow:
        0 12px 28px rgba(82,107,86,0.25) !important;
}

.stButton > button[kind="primary"]:hover {
    transform: translateY(-4px) !important;

    box-shadow:
        0 18px 38px rgba(82,107,86,0.32) !important;
}


/* ----------------------------------------------------------
   TOP BRAND
---------------------------------------------------------- */

.brand-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1.4rem;
}

.brand-left {
    display: flex;
    align-items: center;
    gap: 13px;
}

.logo-circle {
    width: 48px;
    height: 48px;
    border-radius: 17px;

    background:
        linear-gradient(
            135deg,
            var(--sage),
            var(--coral)
        );

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 25px;

    box-shadow:
        0 12px 28px rgba(82,107,86,0.20);

    animation: float 5s ease-in-out infinite;
}

.logo-text {
    font-weight: 700;
    font-size: 23px;
    letter-spacing: 0.12em;
}

.logo-sub {
    color: var(--muted);
    font-size: 10px;
    letter-spacing: 0.16em;
    margin-top: 2px;
}


/* ----------------------------------------------------------
   NAVIGATION
---------------------------------------------------------- */

.nav-box {
    background: rgba(255,255,255,0.68);
    border: 1px solid rgba(228,220,208,0.85);
    border-radius: 22px;
    padding: 7px;
    backdrop-filter: blur(15px);
    box-shadow: var(--shadow-soft);
    margin-bottom: 2.5rem;
}


/* ----------------------------------------------------------
   HERO
---------------------------------------------------------- */

.hero-card {
    position: relative;
    overflow: hidden;

    min-height: 520px;

    border-radius: 42px;

    padding: 70px 68px;

    background:
        linear-gradient(
            135deg,
            rgba(255,253,249,0.96),
            rgba(245,238,227,0.93)
        );

    border: 1px solid var(--line);

    box-shadow: var(--shadow);

    animation: appear 0.8s ease both;
}

.hero-card::before {
    content: "";

    position: absolute;

    width: 350px;
    height: 350px;

    right: -120px;
    top: -110px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(145,169,141,0.42),
            rgba(145,169,141,0)
        );

    animation: float 7s ease-in-out infinite;
}

.hero-card::after {
    content: "";

    position: absolute;

    width: 260px;
    height: 260px;

    left: -100px;
    bottom: -120px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(217,143,120,0.32),
            rgba(217,143,120,0)
        );

    animation: floatReverse 6s ease-in-out infinite;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 720px;
}

.hero-kicker {
    display: inline-block;

    background: var(--coral-soft);
    color: #8D5B4B;

    border-radius: 50px;

    padding: 10px 18px;

    font-size: 12px;
    font-weight: 700;

    letter-spacing: 0.13em;

    margin-bottom: 25px;
}

.hero-title {
    font-family: "Playfair Display", serif;

    font-size: clamp(52px, 7vw, 88px);

    line-height: 0.98;

    letter-spacing: -0.045em;

    margin: 0;

    color: var(--ink);
}

.hero-title span {
    color: var(--sage-dark);
    font-style: italic;
}

.hero-description {
    font-size: 18px;
    line-height: 1.8;

    max-width: 650px;

    color: var(--muted);

    margin-top: 27px;
}

.hero-tagline {
    margin-top: 27px;

    font-size: 12px;
    font-weight: 700;

    letter-spacing: 0.17em;

    color: var(--gold);
}


/* floating visual */

.hero-visual {
    position: absolute;

    right: 8%;
    bottom: 13%;

    width: 205px;
    height: 205px;

    border-radius: 50%;

    border: 1px solid rgba(82,107,86,0.20);

    z-index: 1;

    animation: rotate 20s linear infinite;
}

.hero-visual::before {
    content: "🌿";

    position: absolute;

    font-size: 55px;

    left: 72px;
    top: 62px;

    animation: pulse 3s ease-in-out infinite;
}

.hero-visual::after {
    content: "✦";

    position: absolute;

    right: -5px;
    top: 24px;

    font-size: 25px;

    color: var(--gold);
}


/* ----------------------------------------------------------
   TITLES
---------------------------------------------------------- */

.page-kicker {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.17em;
    color: var(--gold);
    margin-bottom: 8px;
}

.page-title {
    font-family: "Playfair Display", serif;

    font-size: clamp(38px, 5vw, 58px);

    line-height: 1.08;

    color: var(--ink);

    margin-bottom: 10px;
}

.page-description {
    font-size: 16px;
    line-height: 1.75;
    color: var(--muted);
    max-width: 720px;
}


/* ----------------------------------------------------------
   HOME FEATURE CARDS
---------------------------------------------------------- */

.feature {
    background: rgba(255,255,255,0.86);

    border: 1px solid var(--line);

    border-radius: 27px;

    padding: 30px;

    min-height: 230px;

    box-shadow: var(--shadow-soft);

    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease;

    animation: appear 0.7s ease both;
}

.feature:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow);
}

.feature-icon {
    font-size: 42px;
    margin-bottom: 18px;

    animation: float 4s ease-in-out infinite;
}

.feature h3 {
    font-family: "Playfair Display", serif;
    font-size: 25px;
    margin: 0 0 10px;
}

.feature p {
    color: var(--muted);
    line-height: 1.65;
    font-size: 14px;
}


/* ----------------------------------------------------------
   JOURNEY
---------------------------------------------------------- */

.journey-card {
    background: rgba(255,255,255,0.90);

    border: 1px solid var(--line);

    border-radius: 34px;

    padding: 42px;

    box-shadow: var(--shadow);

    animation: appear 0.5s ease both;
}

.journey-top {
    display: flex;
    justify-content: space-between;
    align-items: center;

    margin-bottom: 18px;
}

.step-text {
    font-size: 12px;
    font-weight: 700;
    color: var(--sage-dark);
    letter-spacing: 0.12em;
}

.xp-text {
    font-size: 12px;
    font-weight: 700;
    color: var(--gold);
}

.progress {
    height: 9px;

    border-radius: 20px;

    background: #E7E0D5;

    overflow: hidden;

    margin-bottom: 38px;
}

.progress-inner {
    height: 100%;

    border-radius: 20px;

    background:
        linear-gradient(
            90deg,
            var(--sage-dark),
            var(--gold),
            var(--coral)
        );

    background-size: 200% 100%;

    animation: shimmer 3s linear infinite;

    transition: width 0.5s ease;
}

.question-kicker {
    color: var(--coral);

    font-size: 12px;
    font-weight: 700;

    letter-spacing: 0.16em;

    margin-bottom: 12px;
}

.question-title {
    font-family: "Playfair Display", serif;

    font-size: clamp(34px, 4vw, 51px);

    line-height: 1.12;

    color: var(--ink);

    margin-bottom: 12px;
}

.question-description {
    color: var(--muted);

    line-height: 1.7;

    font-size: 15px;

    margin-bottom: 27px;
}


/* ----------------------------------------------------------
   ANSWER BUTTONS
---------------------------------------------------------- */

.answer-wrap {
    margin-bottom: 10px;
}

.answer-label {
    font-size: 16px !important;
}


/* ----------------------------------------------------------
   DASHBOARD
---------------------------------------------------------- */

.stat-card {
    background: rgba(255,255,255,0.9);

    border: 1px solid var(--line);

    border-radius: 25px;

    padding: 25px;

    min-height: 155px;

    box-shadow: var(--shadow-soft);

    transition: transform 0.25s ease;
}

.stat-card:hover {
    transform: translateY(-6px);
}

.stat-emoji {
    font-size: 30px;
}

.stat-label {
    color: var(--muted);

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 0.12em;

    margin-top: 13px;
}

.stat-value {
    font-family: "Playfair Display", serif;

    font-size: 33px;

    color: var(--ink);

    margin-top: 4px;
}


/* ----------------------------------------------------------
   BODY TYPE
---------------------------------------------------------- */

.type-card {
    background: rgba(255,255,255,0.88);

    border: 1px solid var(--line);

    border-radius: 29px;

    padding: 30px;

    min-height: 285px;

    box-shadow: var(--shadow-soft);

    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease;
}

.type-card:hover {
    transform: translateY(-8px) rotate(-0.5deg);
    box-shadow: var(--shadow);
}

.type-emoji {
    font-size: 46px;
}

.type-card h3 {
    font-family: "Playfair Display", serif;
    font-size: 27px;
    margin: 15px 0 7px;
}

.type-quality {
    color: var(--gold);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.1em;
}

.type-card p {
    color: var(--muted);
    line-height: 1.7;
    font-size: 14px;
}


/* ----------------------------------------------------------
   RESULT
---------------------------------------------------------- */

.result {
    position: relative;

    overflow: hidden;

    background:
        linear-gradient(
            135deg,
            #E5EFDF,
            #F7DED4,
            #E8E3F0
        );

    border-radius: 34px;

    padding: 48px;

    text-align: center;

    box-shadow: var(--shadow);

    animation: glow 4s ease-in-out infinite;
}

.result-emoji {
    font-size: 58px;
    animation: float 4s ease-in-out infinite;
}

.result-label {
    color: var(--sage-dark);

    font-size: 11px;

    font-weight: 700;

    letter-spacing: 0.16em;

    margin-top: 15px;
}

.result-name {
    font-family: "Playfair Display", serif;

    font-size: 52px;

    color: var(--ink);

    margin: 8px 0 10px;
}

.result-text {
    max-width: 650px;

    margin: auto;

    color: #626B64;

    line-height: 1.75;
}


/* ----------------------------------------------------------
   CHALLENGE
---------------------------------------------------------- */

.challenge {
    background:
        linear-gradient(
            135deg,
            rgba(255,253,249,0.97),
            rgba(246,238,227,0.95)
        );

    border-radius: 35px;

    border: 1px solid var(--line);

    padding: 45px;

    box-shadow: var(--shadow);

    animation: appear 0.6s ease both;
}

.challenge-emoji {
    font-size: 58px;
    animation: float 3.5s ease-in-out infinite;
}

.challenge-number {
    color: var(--coral);

    font-size: 12px;

    font-weight: 700;

    letter-spacing: 0.16em;

    margin-top: 18px;
}

.challenge-title {
    font-family: "Playfair Display", serif;

    font-size: 48px;

    line-height: 1.1;

    margin: 8px 0 14px;
}

.challenge-description {
    color: var(--muted);

    font-size: 17px;

    line-height: 1.8;

    max-width: 720px;
}

.challenge-tip {
    background: var(--sage-soft);

    border-radius: 18px;

    padding: 20px;

    margin-top: 25px;

    color: var(--sage-dark);

    line-height: 1.6;
}


/* ----------------------------------------------------------
   REWARD
---------------------------------------------------------- */

.reward {
    background:
        radial-gradient(
            circle at top right,
            rgba(195,155,87,0.28),
            transparent 35%
        ),
        #FFFDF8;

    border: 1px solid var(--gold-soft);

    border-radius: 35px;

    padding: 50px;

    text-align: center;

    box-shadow: var(--shadow);

    animation: appear 0.8s ease both;
}

.reward-badge {
    width: 100px;
    height: 100px;

    border-radius: 50%;

    background: var(--gold-soft);

    display: flex;

    align-items: center;
    justify-content: center;

    font-size: 52px;

    margin: 0 auto 20px;

    animation:
        pulse 2.2s ease-in-out infinite;
}

.reward h2 {
    font-family: "Playfair Display", serif;

    font-size: 40px;

    margin-bottom: 5px;
}

.reward-xp {
    color: var(--gold);

    font-weight: 700;

    font-size: 18px;
}


/* ----------------------------------------------------------
   STREAK
---------------------------------------------------------- */

.streak {
    background:
        linear-gradient(
            135deg,
            #F6D8CD,
            #F1E1BD
        );

    border-radius: 32px;

    padding: 38px;

    box-shadow: var(--shadow);

    position: relative;

    overflow: hidden;
}

.streak::after {
    content: "🔥";

    position: absolute;

    font-size: 130px;

    right: 45px;
    top: 25px;

    opacity: 0.12;

    animation: float 4s ease-in-out infinite;
}

.streak-label {
    color: #875747;

    font-size: 12px;

    font-weight: 700;

    letter-spacing: 0.16em;
}

.streak-number {
    font-family: "Playfair Display", serif;

    font-size: 78px;

    line-height: 1;

    margin-top: 12px;
}


/* ----------------------------------------------------------
   BADGES
---------------------------------------------------------- */

.badge-card {
    background: white;

    border: 1px solid var(--line);

    border-radius: 23px;

    padding: 25px;

    text-align: center;

    box-shadow: var(--shadow-soft);

    transition: transform 0.25s ease;
}

.badge-card:hover {
    transform: translateY(-7px);
}

.badge-icon {
    font-size: 42px;

    margin-bottom: 12px;
}

.badge-name {
    font-weight: 700;

    font-size: 14px;
}

.badge-status {
    color: var(--muted);

    font-size: 11px;

    margin-top: 5px;
}


/* ----------------------------------------------------------
   RECOMMENDATIONS
---------------------------------------------------------- */

.recommendation {
    background: rgba(255,255,255,0.9);

    border: 1px solid var(--line);

    border-radius: 26px;

    padding: 27px;

    margin-bottom: 14px;

    box-shadow: var(--shadow-soft);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

.recommendation:hover {
    transform: translateX(6px);
    box-shadow: var(--shadow);
}

.rec-icon {
    font-size: 35px;
}

.rec-title {
    font-family: "Playfair Display", serif;

    font-size: 25px;

    margin-top: 8px;
}

.rec-text {
    color: var(--muted);

    line-height: 1.7;

    font-size: 14px;
}


/* ----------------------------------------------------------
   EMPTY STATES
---------------------------------------------------------- */

.empty {
    background: rgba(255,255,255,0.75);

    border: 1px dashed #D5CCBF;

    border-radius: 32px;

    padding: 70px 35px;

    text-align: center;

    animation: appear 0.7s ease both;
}

.empty-icon {
    font-size: 58px;

    animation: float 4s ease-in-out infinite;
}

.empty h2 {
    font-family: "Playfair Display", serif;

    font-size: 37px;

    margin: 17px 0 8px;
}

.empty p {
    color: var(--muted);

    max-width: 560px;

    margin: auto;

    line-height: 1.7;
}


/* ----------------------------------------------------------
   ABOUT
---------------------------------------------------------- */

.about-box {
    background: rgba(255,255,255,0.88);

    border: 1px solid var(--line);

    border-radius: 30px;

    padding: 34px;

    min-height: 260px;

    box-shadow: var(--shadow-soft);
}

.about-icon {
    font-size: 42px;
}

.about-box h3 {
    font-family: "Playfair Display", serif;

    font-size: 27px;

    margin: 15px 0 10px;
}

.about-box p {
    color: var(--muted);

    line-height: 1.75;
}


/* ----------------------------------------------------------
   FOOTER
---------------------------------------------------------- */

.footer {
    margin-top: 80px;

    padding-top: 25px;

    border-top: 1px solid var(--line);

    text-align: center;

    color: var(--muted);

    font-size: 12px;

    line-height: 1.8;
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# DATA
# ============================================================

QUESTIONS = [
    {
        "key": "age",
        "title": "Let's start with you.",
        "description": "Just one small detail to begin your journey.",
        "kind": "number",
        "label": "Your age",
        "min": 13,
        "max": 100,
        "default": 20,
        "unit": "years",
        "group": "ABOUT YOU",
    },
    {
        "key": "goal",
        "title": "What do you want more of?",
        "description": "Choose the area you'd most like to nurture right now.",
        "kind": "choice",
        "options": [
            ("⚡", "More energy"),
            ("🌙", "Better sleep"),
            ("🧘", "More calm"),
            ("🥗", "Better nourishment"),
            ("🏃", "More movement"),
            ("🌱", "Overall balance"),
        ],
        "group": "YOUR INTENTION",
    },
    {
        "key": "activity",
        "title": "How does your day usually move?",
        "description": "Think about an ordinary day.",
        "kind": "choice",
        "options": [
            ("🪑", "Mostly sitting"),
            ("🚶", "Lightly active"),
            ("🏃", "Quite active"),
            ("🔥", "Very active"),
        ],
        "group": "YOUR RHYTHM",
    },
    {
        "key": "build",
        "title": "Which feels closest to your natural build?",
        "description": "There is no right answer — simply choose what feels familiar.",
        "kind": "choice",
        "options": [
            ("🪽", "Lean and light"),
            ("🏹", "Medium and athletic"),
            ("🌳", "Broad and solid"),
        ],
        "group": "YOUR NATURAL PATTERN",
    },
    {
        "key": "appetite",
        "title": "What is your appetite usually like?",
        "description": "Choose the pattern you notice most often.",
        "kind": "choice",
        "options": [
            ("🌬️", "It changes a lot"),
            ("🔥", "Strong and regular"),
            ("🌿", "Steady and moderate"),
        ],
        "group": "YOUR NATURAL PATTERN",
    },
    {
        "key": "energy",
        "title": "How does your energy behave?",
        "description": "Which one sounds most like your everyday experience?",
        "kind": "choice",
        "options": [
            ("⚡", "Comes in bursts"),
            ("☀️", "Strong and focused"),
            ("🌊", "Calm and steady"),
        ],
        "group": "YOUR NATURAL PATTERN",
    },
    {
        "key": "sleep",
        "title": "How much sleep do you usually get?",
        "description": "An approximate number is perfectly fine.",
        "kind": "number",
        "label": "Average sleep",
        "min": 3,
        "max": 14,
        "default": 7,
        "unit": "hours",
        "group": "YOUR DAILY LIFE",
    },
    {
        "key": "stress",
        "title": "How does life feel lately?",
        "description": "Think about your recent everyday experience.",
        "kind": "choice",
        "options": [
            ("🌤️", "Mostly calm"),
            ("🌥️", "A little busy"),
            ("🌧️", "Quite stressful"),
            ("⛈️", "Very overwhelming"),
        ],
        "group": "YOUR DAILY LIFE",
    },
    {
        "key": "movement",
        "title": "How much intentional movement do you get?",
        "description": "Walking, exercise, yoga, sport — it all counts.",
        "kind": "choice",
        "options": [
            ("🌱", "Less than 20 min"),
            ("🚶", "20–40 min"),
            ("🏃", "40–60 min"),
            ("🔥", "More than an hour"),
        ],
        "group": "YOUR DAILY LIFE",
    },
    {
        "key": "meals",
        "title": "How predictable are your meals?",
        "description": "Choose what best matches your normal routine.",
        "kind": "choice",
        "options": [
            ("🎲", "Very unpredictable"),
            ("🕐", "Somewhat irregular"),
            ("🍽️", "Mostly regular"),
            ("✨", "Very consistent"),
        ],
        "group": "YOUR NOURISHMENT",
    },
    {
        "key": "routine",
        "title": "What kind of routine feels best?",
        "description": "Your natural preference matters more than a perfect routine.",
        "kind": "choice",
        "options": [
            ("🦋", "Flexible"),
            ("📋", "Structured"),
            ("🌿", "Consistent"),
        ],
        "group": "YOUR RHYTHM",
    },
    {
        "key": "weather",
        "title": "What surroundings feel most comfortable?",
        "description": "Notice what your body naturally seems to prefer.",
        "kind": "choice",
        "options": [
            ("🔥", "Warm"),
            ("❄️", "Cool"),
            ("🌤️", "Mild"),
        ],
        "group": "YOUR NATURAL PATTERN",
    },
]


# ============================================================
# BODY TYPE INFORMATION
# ============================================================

BODY_TYPES = {
    "Vata": {
        "emoji": "🌬️",
        "quality": "Creative · Dynamic · Light",
        "text": (
            "Your answers show more qualities traditionally associated "
            "with movement, creativity and change. Grounding routines may "
            "feel especially supportive."
        ),
    },
    "Pitta": {
        "emoji": "🔥",
        "quality": "Focused · Energetic · Driven",
        "text": (
            "Your answers show more qualities traditionally associated "
            "with focus, intensity and determination. Space for recovery "
            "and balance may feel especially valuable."
        ),
    },
    "Kapha": {
        "emoji": "🌊",
        "quality": "Steady · Calm · Grounded",
        "text": (
            "Your answers show more qualities traditionally associated "
            "with steadiness, patience and grounded energy. Variety and "
            "regular movement may help maintain momentum."
        ),
    },
}


# ============================================================
# CHALLENGES
# ============================================================

CHALLENGES = [
    {
        "emoji": "💧",
        "title": "The Hydration Pause",
        "description": (
            "Take one quiet moment today to drink a full glass of water "
            "without scrolling, rushing or multitasking."
        ),
        "tip": "Slow down. Take three breaths. Then drink.",
        "badge": "💧",
        "badge_name": "Hydration Hero",
        "xp": 20,
    },
    {
        "emoji": "🌿",
        "title": "The Movement Spark",
        "description": (
            "Give yourself ten minutes of movement today. Walk, stretch, "
            "dance or simply move in a way that feels good."
        ),
        "tip": "You don't need a workout. You just need a beginning.",
        "badge": "🌿",
        "badge_name": "Movement Spark",
        "xp": 25,
    },
    {
        "emoji": "🥗",
        "title": "The Mindful Meal",
        "description": (
            "Choose one meal today and eat it without your main screen. "
            "Notice the taste, texture and pace of your meal."
        ),
        "tip": "One mindful meal is enough for today.",
        "badge": "🥗",
        "badge_name": "Mindful Nourisher",
        "xp": 25,
    },
    {
        "emoji": "🌙",
        "title": "The Evening Reset",
        "description": (
            "Create twenty screen-free minutes before bed and let your "
            "mind gradually shift from doing to resting."
        ),
        "tip": "Dim the lights. Put the phone away. Let the day end.",
        "badge": "🌙",
        "badge_name": "Evening Guardian",
        "xp": 30,
    },
]


# ============================================================
# FUNCTIONS
# ============================================================

def navigate(page):
    st.session_state.page = page
    st.rerun()


def calculate_body_type():

    scores = {
        "Vata": 0,
        "Pitta": 0,
        "Kapha": 0,
    }

    mapping = {
        "build": {
            "Lean and light": "Vata",
            "Medium and athletic": "Pitta",
            "Broad and solid": "Kapha",
        },
        "appetite": {
            "It changes a lot": "Vata",
            "Strong and regular": "Pitta",
            "Steady and moderate": "Kapha",
        },
        "energy": {
            "Comes in bursts": "Vata",
            "Strong and focused": "Pitta",
            "Calm and steady": "Kapha",
        },
        "routine": {
            "Flexible": "Vata",
            "Structured": "Pitta",
            "Consistent": "Kapha",
        },
        "weather": {
            "Warm": "Vata",
            "Cool": "Pitta",
            "Mild": "Kapha",
        },
    }

    for key, choices in mapping.items():

        answer = st.session_state.answers.get(key)

        if answer in choices:
            scores[choices[answer]] += 1

    ordered = sorted(
        scores.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    if ordered[0][1] == 0:
        body_type = "Balanced"

    elif ordered[0][1] == ordered[1][1]:
        body_type = f"{ordered[0][0]}–{ordered[1][0]}"

    else:
        body_type = ordered[0][0]

    st.session_state.vata = scores["Vata"]
    st.session_state.pitta = scores["Pitta"]
    st.session_state.kapha = scores["Kapha"]
    st.session_state.body_type = body_type


def finish_journey():

    calculate_body_type()

    st.session_state.profile_complete = True

    if st.session_state.xp < 100:
        st.session_state.xp = 100

    if st.session_state.streak == 0:
        st.session_state.streak = 1

    navigate("My Wellness")


def complete_challenge(index):

    challenge = CHALLENGES[index]

    if index not in st.session_state.completed_challenges:

        st.session_state.completed_challenges.append(index)

        st.session_state.xp += challenge["xp"]

        today = str(date.today())

        if st.session_state.last_completion_date != today:
            st.session_state.streak += 1
            st.session_state.last_completion_date = today

        if challenge["badge_name"] not in st.session_state.badges:
            st.session_state.badges.append(
                challenge["badge_name"]
            )

        st.session_state.reward = {
            "emoji": challenge["badge"],
            "name": challenge["badge_name"],
            "xp": challenge["xp"],
        }

    st.session_state.active_challenge = False

    st.rerun()


# ============================================================
# BRAND
# ============================================================

st.markdown(
    """
<div class="brand-row">

    <div class="brand-left">

        <div class="logo-circle">
            🌿
        </div>

        <div>
            <div class="logo-text">
                MYBIO
            </div>

            <div class="logo-sub">
                YOUR RHYTHM · YOUR JOURNEY
            </div>
        </div>

    </div>

</div>
""",
    unsafe_allow_html=True,
)


# ============================================================
# NAVIGATION
# ============================================================

pages = [
    ("🏠", "Home"),
    ("✨", "Journey"),
    ("💚", "My Wellness"),
    ("🌿", "Body Type"),
    ("🎯", "Challenge"),
    ("🔥", "My Rhythm"),
    ("💡", "For You"),
    ("ℹ️", "About"),
]

st.markdown('<div class="nav-box">', unsafe_allow_html=True)

nav_columns = st.columns(len(pages))

for column, (emoji, label) in zip(nav_columns, pages):

    with column:

        if st.button(
            f"{emoji}  {label}",
            key=f"nav_{label}",
            use_container_width=True,
            type=(
                "primary"
                if (
                    (label == "Home" and st.session_state.page == "Home")
                    or
                    (label == "Journey" and st.session_state.page == "Begin Journey")
                    or
                    (label == "My Wellness" and st.session_state.page == "My Wellness")
                    or
                    (label == "Body Type" and st.session_state.page == "Body Type")
                    or
                    (label == "Challenge" and st.session_state.page == "Challenge")
                    or
                    (label == "My Rhythm" and st.session_state.page == "My Rhythm")
                    or
                    (label == "For You" and st.session_state.page == "For You")
                    or
                    (label == "About" and st.session_state.page == "About")
                )
                else "secondary"
            ),
        ):
            target = {
                "Home": "Home",
                "Journey": "Begin Journey",
                "My Wellness": "My Wellness",
                "Body Type": "Body Type",
                "Challenge": "Challenge",
                "My Rhythm": "My Rhythm",
                "For You": "For You",
                "About": "About",
            }

            navigate(target[label])

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# HOME
# ============================================================

def home():

    st.markdown(
        """
<div class="hero-card">

    <div class="hero-content">

        <div class="hero-kicker">
            🌿 DISCOVER YOUR EVERYDAY RHYTHM
        </div>

        <div class="hero-title">
            Meet the <span>you</span><br>
            within.
        </div>

        <div class="hero-description">
            A more personal approach to everyday wellness.
            Discover your natural patterns, understand your rhythm
            and turn tiny moments into meaningful habits.
        </div>

        <div class="hero-tagline">
            ANCIENT WISDOM · MODERN YOU · INFINITE POSSIBILITIES
        </div>

    </div>

    <div class="hero-visual"></div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button(
        "✨  Begin My Journey",
        type="primary",
        key="home_start",
    ):
        navigate("Begin Journey")

    st.write("")
    st.write("")

    st.markdown(
        """
<div class="page-kicker">
    WHY MYBIO?
</div>

<div class="page-title">
    Know your rhythm.<br>
    Nurture your everyday.
</div>

<div class="page-description">
    Not a rigid checklist. Not another productivity system.
    MYBIO is a space to pause, notice and take one small step.
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    columns = st.columns(3)

    features = [
        (
            "🧭",
            "Discover",
            "Answer a handful of thoughtful questions and uncover patterns in the way you naturally move through life.",
        ),
        (
            "🌿",
            "Understand",
            "Explore your Ayurvedic body-type pattern through a simple, educational interpretation.",
        ),
        (
            "🎯",
            "Take action",
            "Turn awareness into tiny challenges that feel achievable rather than overwhelming.",
        ),
    ]

    for column, (icon, title, text) in zip(columns, features):

        with column:

            st.markdown(
                f"""
<div class="feature">

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
                unsafe_allow_html=True,
            )

    st.write("")
    st.write("")

    st.markdown(
        """
<div class="result">

    <div class="result-emoji">
        🌱
    </div>

    <div class="result-label">
        THE MYBIO PHILOSOPHY
    </div>

    <div class="result-name">
        Small shifts.<br>
        Deeper balance.
    </div>

    <div class="result-text">
        You don't need to transform your entire life overnight.
        Sometimes the smallest intentional choice is where everything begins.
    </div>

</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# JOURNEY
# ============================================================

def journey():

    index = st.session_state.question_index

    total = len(QUESTIONS)

    question = QUESTIONS[index]

    progress = int(((index + 1) / total) * 100)

    st.markdown(
        """
<div class="page-kicker">
    ✨ YOUR DISCOVERY
</div>

<div class="page-title">
    Let's get to know you.
</div>

<div class="page-description">
    Twelve simple questions. No perfect answers.
    Just choose what feels most like you.
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    st.markdown(
        f"""
<div class="journey-card">

    <div class="journey-top">

        <div class="step-text">
            QUESTION {index + 1} OF {total}
        </div>

        <div class="xp-text">
            ✨ +{index * 5} XP
        </div>

    </div>

    <div class="progress">

        <div
            class="progress-inner"
            style="width:{progress}%"
        ></div>

    </div>

    <div class="question-kicker">
        {question["group"]}
    </div>

    <div class="question-title">
        {question["title"]}
    </div>

    <div class="question-description">
        {question["description"]}
    </div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    current = st.session_state.answers.get(
        question["key"]
    )

    if question["kind"] == "number":

        value = st.number_input(
            question["label"],
            min_value=question["min"],
            max_value=question["max"],
            value=(
                current
                if current is not None
                else question["default"]
            ),
            step=1,
            key=f"number_{question['key']}",
        )

        st.session_state.answers[
            question["key"]
        ] = value

        st.caption(
            f"Measured in {question['unit']}."
        )

    else:

        option_columns = st.columns(2)

        for i, option in enumerate(question["options"]):

            emoji, text = option

            with option_columns[i % 2]:

                selected = current == text

                label = (
                    f"✅ {emoji}  {text}"
                    if selected
                    else f"{emoji}  {text}"
                )

                if st.button(
                    label,
                    key=f"option_{question['key']}_{i}",
                    use_container_width=True,
                    type=(
                        "primary"
                        if selected
                        else "secondary"
                    ),
                ):

                    st.session_state.answers[
                        question["key"]
                    ] = text

                    st.rerun()

    st.write("")
    st.write("")

    selected = st.session_state.answers.get(
        question["key"]
    )

    left, center, right = st.columns(
        [1, 2, 1]
    )

    with left:

        if index > 0:

            if st.button(
                "← Back",
                key=f"back_{index}",
                use_container_width=True,
            ):

                st.session_state.question_index -= 1
                st.rerun()

    with right:

        if selected is not None:

            if index == total - 1:

                button_text = "🌟 Reveal My Result"

            else:

                button_text = "Continue  →"

            if st.button(
                button_text,
                key=f"next_{index}",
                type="primary",
                use_container_width=True,
            ):

                if index == total - 1:

                    finish_journey()

                else:

                    st.session_state.question_index += 1
                    st.rerun()


# ============================================================
# MY WELLNESS
# ============================================================

def wellness():

    if not st.session_state.profile_complete:

        st.markdown(
            """
<div class="page-kicker">
    💚 MY WELLNESS
</div>

<div class="page-title">
    Your space is waiting.
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
<div class="empty">

    <div class="empty-icon">
        🌱
    </div>

    <h2>
        Something beautiful starts with knowing yourself.
    </h2>

    <p>
        Complete your short discovery journey and this space
        will begin to reflect the patterns you've shared.
    </p>

</div>
""",
            unsafe_allow_html=True,
        )

        st.write("")

        if st.button(
            "✨ Start discovering",
            type="primary",
        ):
            navigate("Begin Journey")

        return

    st.markdown(
        """
<div class="page-kicker">
    💚 MY WELLNESS
</div>

<div class="page-title">
    Your personal snapshot.
</div>

<div class="page-description">
    A few signals from your journey — a starting point,
    not a scorecard.
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    values = [
        ("🔥", "STREAK", f"{st.session_state.streak} days"),
        ("✨", "XP", str(st.session_state.xp)),
        ("🌿", "BODY TYPE", st.session_state.body_type),
        ("🎯", "CHALLENGES", str(len(st.session_state.completed_challenges))),
    ]

    columns = st.columns(4)

    for column, (emoji, label, value) in zip(
        columns,
        values,
    ):

        with column:

            st.markdown(
                f"""
<div class="stat-card">

    <div class="stat-emoji">
        {emoji}
    </div>

    <div class="stat-label">
        {label}
    </div>

    <div class="stat-value">
        {value}
    </div>

</div>
""",
                unsafe_allow_html=True,
            )

    st.write("")
    st.write("")

    body = st.session_state.body_type

    if body in BODY_TYPES:

        info = BODY_TYPES[body]

        st.markdown(
            f"""
<div class="result">

    <div class="result-emoji">
        {info["emoji"]}
    </div>

    <div class="result-label">
        YOUR CURRENT BODY-TYPE PATTERN
    </div>

    <div class="result-name">
        {body}
    </div>

    <div class="result-text">
        {info["text"]}
    </div>

</div>
""",
            unsafe_allow_html=True,
        )

    st.write("")
    st.write("")

    if st.button(
        "🎯 Take today's challenge",
        type="primary",
    ):
        navigate("Challenge")


# ============================================================
# BODY TYPE
# ============================================================

def body_type_page():

    if not st.session_state.profile_complete:

        st.markdown(
            """
<div class="page-kicker">
    🌿 BODY TYPE
</div>

<div class="page-title">
    Your pattern is still unfolding.
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            """
<div class="empty">

    <div class="empty-icon">
        🌿
    </div>

    <h2>
        There's something waiting to be discovered.
    </h2>

    <p>
        Complete the MYBIO journey to explore your Ayurvedic body-type pattern.
    </p>

</div>
""",
            unsafe_allow_html=True,
        )

        if st.button(
            "✨ Begin discovery",
            type="primary",
        ):
            navigate("Begin Journey")

        return

    body = st.session_state.body_type

    st.markdown(
        """
<div class="page-kicker">
    🌿 YOUR BODY TYPE
</div>

<div class="page-title">
    A different way to read your rhythm.
</div>

<div class="page-description">
    Ayurvedic traditions describe broad patterns of qualities.
    Your result is intended for reflection and general wellness education,
    not diagnosis.
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    if body in BODY_TYPES:

        info = BODY_TYPES[body]

        st.markdown(
            f"""
<div class="result">

    <div class="result-emoji">
        {info["emoji"]}
    </div>

    <div class="result-label">
        YOUR RESULT
    </div>

    <div class="result-name">
        {body}
    </div>

    <div class="result-text">
        {info["text"]}
    </div>

</div>
""",
            unsafe_allow_html=True,
        )

    st.write("")
    st.write("")

    columns = st.columns(3)

    all_types = [
        ("🌬️", "Vata", "Creative · Dynamic · Light"),
        ("🔥", "Pitta", "Focused · Energetic · Driven"),
        ("🌊", "Kapha", "Steady · Calm · Grounded"),
    ]

    for column, (emoji, name, quality) in zip(
        columns,
        all_types,
    ):

        with column:

            st.markdown(
                f"""
<div class="type-card">

    <div class="type-emoji">
        {emoji}
    </div>

    <h3>
        {name}
    </h3>

    <div class="type-quality">
        {quality}
    </div>

    <p>
        Explore this traditional wellness concept
        as a lens for reflection and self-awareness.
    </p>

</div>
""",
                unsafe_allow_html=True,
            )

    st.write("")

    st.caption(
        "Educational note: Ayurvedic body-type concepts are traditional wellness concepts "
        "and should not replace professional medical advice."
    )


# ============================================================
# CHALLENGE
# ============================================================

def challenge_page():

    st.markdown(
        """
<div class="page-kicker">
    🎯 TODAY'S MOMENT
</div>

<div class="page-title">
    One small move.
</div>

<div class="page-description">
    You don't have to overhaul your life today.
    Just show up for one intentional moment.
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    # Reward screen
    if st.session_state.reward:

        reward = st.session_state.reward

        st.markdown(
            f"""
<div class="reward">

    <div class="reward-badge">
        {reward["emoji"]}
    </div>

    <div class="page-kicker">
        CHALLENGE COMPLETE
    </div>

    <h2>
        {reward["name"]}
    </h2>

    <div class="reward-xp">
        +{reward["xp"]} XP 🎉
    </div>

    <p style="
        color:#6E756F;
        margin-top:15px;
        line-height:1.7;
    ">
        You showed up for yourself today.
        That's worth celebrating.
    </p>

</div>
""",
            unsafe_allow_html=True,
        )

        st.write("")

        columns = st.columns(3)

        with columns[0]:

            st.metric(
                "🔥 Streak",
                f"{st.session_state.streak} days",
            )

        with columns[1]:

            st.metric(
                "✨ XP",
                st.session_state.xp,
            )

        with columns[2]:

            st.metric(
                "🏆 Badges",
                len(st.session_state.badges),
            )

        st.write("")

        if st.button(
            "Continue →",
            type="primary",
        ):

            st.session_state.reward = None
            st.rerun()

        return

    # Find next challenge
    next_challenge = None

    for i, challenge in enumerate(CHALLENGES):

        if i not in st.session_state.completed_challenges:

            next_challenge = i
            break

    if next_challenge is None:

        st.markdown(
            """
<div class="empty">

    <div class="empty-icon">
        🏆
    </div>

    <h2>
        You've completed this collection.
    </h2>

    <p>
        Every challenge you completed is another small reminder
        that consistency is built one moment at a time.
    </p>

</div>
""",
            unsafe_allow_html=True,
        )

        return

    challenge = CHALLENGES[next_challenge]

    st.markdown(
        f"""
<div class="challenge">

    <div class="challenge-emoji">
        {challenge["emoji"]}
    </div>

    <div class="challenge-number">
        CHALLENGE {next_challenge + 1}
    </div>

    <div class="challenge-title">
        {challenge["title"]}
    </div>

    <div class="challenge-description">
        {challenge["description"]}
    </div>

    <div class="challenge-tip">
        💡 {challenge["tip"]}
    </div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    if not st.session_state.active_challenge:

        if st.button(
            "🚀 I'm ready",
            type="primary",
        ):

            st.session_state.active_challenge = True
            st.rerun()

    else:

        st.info(
            "🌿 Take the moment now. There is no timer and no pressure."
        )

        if st.button(
            "✅ I completed it",
            type="primary",
        ):

            complete_challenge(next_challenge)


# ============================================================
# MY RHYTHM
# ============================================================

def rhythm_page():

    st.markdown(
        """
<div class="page-kicker">
    🔥 MY RHYTHM
</div>

<div class="page-title">
    Keep showing up.
</div>

<div class="page-description">
    Your streak isn't about perfection.
    It's simply a visual reminder of the moments you've chosen yourself.
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    st.markdown(
        f"""
<div class="streak">

    <div class="streak-label">
        CURRENT STREAK
    </div>

    <div class="streak-number">
        {st.session_state.streak}
    </div>

    <div style="color:#875747; font-weight:600;">
        {"day" if st.session_state.streak == 1 else "days"} 🔥
    </div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")

    st.markdown(
        """
<div class="page-kicker">
    🗓️ YOUR WEEK
</div>
""",
        unsafe_allow_html=True,
    )

    days = [
        "MON",
        "TUE",
        "WED",
        "THU",
        "FRI",
        "SAT",
        "SUN",
    ]

    columns = st.columns(7)

    active = min(
        st.session_state.streak,
        7,
    )

    for i, (column, day) in enumerate(
        zip(columns, days)
    ):

        is_active = i >= 7 - active

        with column:

            if is_active:

                st.success(
                    f"{day}\n\n🌱"
                )

            else:

                st.info(
                    f"{day}\n\n·"
                )

    st.write("")
    st.write("")

    st.markdown(
        """
<div class="page-kicker">
    🏆 YOUR COLLECTION
</div>

<div class="page-title" style="font-size:38px;">
    Badges earned along the way.
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    if not st.session_state.badges:

        st.markdown(
            """
<div class="empty">

    <div class="empty-icon">
        🎁
    </div>

    <h2>
        Your first badge is waiting.
    </h2>

    <p>
        Complete a challenge and your first badge
        will appear here.
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

        columns = st.columns(
            min(4, len(earned))
        )

        for column, challenge in zip(
            columns,
            earned,
        ):

            with column:

                st.markdown(
                    f"""
<div class="badge-card">

    <div class="badge-icon">
        {challenge["badge"]}
    </div>

    <div class="badge-name">
        {challenge["badge_name"]}
    </div>

    <div class="badge-status">
        Earned ✨
    </div>

</div>
""",
                    unsafe_allow_html=True,
                )


# ============================================================
# FOR YOU
# ============================================================

def recommendations_page():

    st.markdown(
        """
<div class="page-kicker">
    💡 FOR YOU
</div>

<div class="page-title">
    A few gentle nudges.
</div>

<div class="page-description">
    Small ideas based on the rhythm you shared.
    Nothing here is a prescription.
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    if not st.session_state.profile_complete:

        st.markdown(
            """
<div class="empty">

    <div class="empty-icon">
        💌
    </div>

    <h2>
        This space will become yours.
    </h2>

    <p>
        Complete the MYBIO journey first.
        Then your personal suggestions will begin to appear here.
    </p>

</div>
""",
            unsafe_allow_html=True,
        )

        if st.button(
            "✨ Begin my journey",
            type="primary",
        ):
            navigate("Begin Journey")

        return

    answers = st.session_state.answers

    recommendations = []

    sleep = answers.get("sleep")

    if sleep and sleep < 7:

        recommendations.append(
            (
                "🌙",
                "Give sleep a little more room",
                "If possible, experiment with a slightly earlier wind-down rather than trying to change your entire sleep schedule at once.",
            )
        )

    stress = answers.get("stress")

    if stress in [
        "Quite stressful",
        "Very overwhelming",
    ]:

        recommendations.append(
            (
                "🧘",
                "Create a tiny pause",
                "Try adding one two-minute pause during your busiest part of the day. No productivity goal — simply pause.",
            )
        )

    movement = answers.get("movement")

    if movement == "Less than 20 min":

        recommendations.append(
            (
                "🚶",
                "Start with ten minutes",
                "A short walk can be a much easier starting point than waiting for the perfect workout window.",
            )
        )

    meals = answers.get("meals")

    if meals in [
        "Very unpredictable",
        "Somewhat irregular",
    ]:

        recommendations.append(
            (
                "🥗",
                "Anchor one meal",
                "Choose one meal to make more predictable. One stable point can be enough to start building rhythm.",
            )
        )

    if not recommendations:

        recommendations = [
            (
                "🌱",
                "Protect what already works",
                "Notice one habit that already makes your day better and protect it instead of adding another task.",
            ),
            (
                "🧭",
                "Notice before changing",
                "Spend a minute noticing your energy and mood before deciding what needs to change.",
            ),
            (
                "✨",
                "Choose one thing",
                "The most sustainable routine is often the one with fewer things competing for your attention.",
            ),
        ]

    for icon, title, text in recommendations:

        st.markdown(
            f"""
<div class="recommendation">

    <div class="rec-icon">
        {icon}
    </div>

    <div class="rec-title">
        {title}
    </div>

    <div class="rec-text">
        {text}
    </div>

</div>
""",
            unsafe_allow_html=True,
        )

    st.caption(
        "These are general wellness suggestions and are not medical advice."
    )


# ============================================================
# ABOUT
# ============================================================

def about_page():

    st.markdown(
        """
<div class="page-kicker">
    🌿 ABOUT MYBIO
</div>

<div class="page-title">
    Ancient wisdom.<br>
    Modern you.
</div>

<div class="page-description">
    MYBIO is built around a simple idea:
    self-awareness can be the beginning of better everyday choices.
</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")
    st.write("")

    columns = st.columns(2)

    with columns[0]:

        st.markdown(
            """
<div class="about-box">

    <div class="about-icon">
        🧭
    </div>

    <h3>
        A journey, not a checklist.
    </h3>

    <p>
        MYBIO gives you a space to pause and reflect on
        everyday patterns — energy, movement, nourishment,
        sleep and routine — without turning wellness into
        another thing to stress about.
    </p>

</div>
""",
            unsafe_allow_html=True,
        )

    with columns[1]:

        st.markdown(
            """
<div class="about-box">

    <div class="about-icon">
        🌿
    </div>

    <h3>
        Inspired by tradition.
    </h3>

    <p>
        Ayurvedic concepts are presented as traditional
        wellness perspectives for reflection and learning.
        They are not intended to diagnose, prevent or treat
        medical conditions.
    </p>

</div>
""",
            unsafe_allow_html=True,
        )

    st.write("")
    st.write("")

    st.markdown(
        """
<div class="result">

    <div class="result-emoji">
        🌱
    </div>

    <div class="result-label">
        MYBIO
    </div>

    <div class="result-name">
        A little more you,<br>
        every day.
    </div>

    <div class="result-text">
        Start where you are.
        Notice what matters.
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
    home()

elif st.session_state.page == "Begin Journey":
    journey()

elif st.session_state.page == "My Wellness":
    wellness()

elif st.session_state.page == "Body Type":
    body_type_page()

elif st.session_state.page == "Challenge":
    challenge_page()

elif st.session_state.page == "My Rhythm":
    rhythm_page()

elif st.session_state.page == "For You":
    recommendations_page()

elif st.session_state.page == "About":
    about_page()


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="footer">
    🌿 MYBIO
    <br>
    ANCIENT WISDOM · MODERN YOU · INFINITE POSSIBILITIES
    <br>
    <br>
    Small shifts · mindful moments · your own rhythm
</div>
""",
    unsafe_allow_html=True,
)
