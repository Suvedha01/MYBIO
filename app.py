import streamlit as st
from datetime import date, timedelta


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="MYBIO",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# GLOBAL CSS
# HTML IS USED ONLY FOR STYLING — NEVER FOR PAGE CONTENT
# ============================================================

st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap'
    );

    /* ======================================================
       BASE
       ====================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 12% 18%,
                rgba(143, 170, 147, 0.22),
                transparent 24%
            ),
            radial-gradient(
                circle at 88% 18%,
                rgba(220, 176, 146, 0.18),
                transparent 25%
            ),
            radial-gradient(
                circle at 70% 85%,
                rgba(168, 157, 192, 0.14),
                transparent 25%
            ),
            #E9E1D5;
        color: #29342E;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.8rem !important;
        padding-bottom: 4rem !important;
    }

    html,
    body,
    [class*="css"] {
        font-family: "DM Sans", sans-serif;
    }

    /* ======================================================
       HEADINGS
       ====================================================== */

    h1,
    h2,
    h3 {
        font-family: "Playfair Display", Georgia, serif !important;
        color: #26332C !important;
    }

    h1 {
        font-size: clamp(3.2rem, 7vw, 6.5rem) !important;
        line-height: 0.98 !important;
        letter-spacing: -3px !important;
        margin-top: 0 !important;
        margin-bottom: 1rem !important;
    }

    h2 {
        font-size: clamp(2rem, 4vw, 3.3rem) !important;
        line-height: 1.08 !important;
    }

    h3 {
        font-size: 1.5rem !important;
    }

    p {
        color: #536057;
        font-size: 1rem;
        line-height: 1.65;
    }

    /* ======================================================
       BUTTONS
       ====================================================== */

    .stButton > button {
        min-height: 48px;
        border-radius: 999px;
        border: 1px solid rgba(63, 82, 68, 0.13);
        background: rgba(255, 252, 246, 0.86);
        color: #344239;
        font-weight: 700;
        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease,
            background 0.25s ease;
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 14px 30px rgba(52, 67, 56, 0.14);
        background: #FFFDF8;
    }

    button[kind="primary"] {
        background: #526B59 !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 12px 30px rgba(61, 82, 66, 0.22);
    }

    button[kind="primary"]:hover {
        background: #405646 !important;
        color: white !important;
        transform: translateY(-4px) scale(1.01);
        box-shadow: 0 18px 35px rgba(61, 82, 66, 0.27);
    }

    /* ======================================================
       CARDS
       ====================================================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 252, 246, 0.72);
        border: 1px solid rgba(76, 96, 81, 0.12);
        border-radius: 26px;
        padding: 1.15rem;
        transition:
            transform 0.3s ease,
            box-shadow 0.3s ease;
        animation: appear 0.55s ease both;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-6px);
        box-shadow: 0 20px 45px rgba(60, 70, 62, 0.12);
    }

    /* ======================================================
       METRICS
       ====================================================== */

    [data-testid="stMetric"] {
        background: rgba(255, 252, 246, 0.68);
        border: 1px solid rgba(76, 96, 81, 0.10);
        border-radius: 20px;
        padding: 1rem;
        animation: appear 0.6s ease both;
    }

    [data-testid="stMetricValue"] {
        color: #526B59;
    }

    /* ======================================================
       PROGRESS
       ====================================================== */

    .stProgress > div > div > div > div {
        background: #526B59;
    }

    /* ======================================================
       INPUTS
       ====================================================== */

    div[data-baseweb="select"] > div {
        border-radius: 14px;
        background: rgba(255, 252, 246, 0.9);
    }

    input {
        border-radius: 14px !important;
    }

    /* ======================================================
       ALERTS
       ====================================================== */

    [data-testid="stAlert"] {
        border-radius: 18px;
    }

    /* ======================================================
       ANIMATIONS
       ====================================================== */

    @keyframes appear {
        from {
            opacity: 0;
            transform: translateY(18px);
        }

        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes floatOne {
        0%, 100% {
            transform: translateY(0px) rotate(0deg);
        }

        50% {
            transform: translateY(-15px) rotate(4deg);
        }
    }

    @keyframes floatTwo {
        0%, 100% {
            transform: translateY(0px);
        }

        50% {
            transform: translateY(12px);
        }
    }

    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
            opacity: 0.75;
        }

        50% {
            transform: scale(1.08);
            opacity: 1;
        }
    }

    @keyframes spinSlow {
        from {
            transform: rotate(0deg);
        }

        to {
            transform: rotate(360deg);
        }
    }

    /* ======================================================
       MOBILE
       ====================================================== */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }

        h1 {
            font-size: 3.4rem !important;
            letter-spacing: -1.5px !important;
        }

        h2 {
            font-size: 2.2rem !important;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "page": "Home",
    "answers": {},
    "question_index": 0,
    "profile_complete": False,
    "body_type": "",
    "vata": 0,
    "pitta": 0,
    "kapha": 0,
    "xp": 0,
    "streak": 0,
    "completion_dates": [],
    "completed_challenges": [],
    "badges": [],
    "active_challenge": None,
    "last_reward": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# DATA
# ============================================================

NAVIGATION = [
    "Home",
    "Journey",
    "My Wellness",
    "Body Type",
    "Today’s Challenge",
    "My Rhythm",
    "For You",
    "About",
]


QUESTIONS = [
    {
        "key": "goal",
        "question": "What do you want more of?",
        "options": [
            "⚡ Energy",
            "🌙 Better sleep",
            "🧘 Calm",
            "🥗 Nourishment",
            "🏃 Movement",
            "🌿 Balance",
        ],
    },
    {
        "key": "activity",
        "question": "How active is your usual day?",
        "options": [
            "🪑 Mostly sitting",
            "🚶 Lightly active",
            "🏃 Quite active",
            "🔥 Very active",
        ],
    },
    {
        "key": "build",
        "question": "Which feels most like you?",
        "options": [
            "🌬️ Lean & light",
            "🔥 Medium & athletic",
            "🌱 Broad & solid",
        ],
    },
    {
        "key": "appetite",
        "question": "How does your appetite behave?",
        "options": [
            "〰️ Changes often",
            "🔥 Strong & regular",
            "🌿 Steady & moderate",
        ],
    },
    {
        "key": "energy",
        "question": "How does your energy move?",
        "options": [
            "⚡ In bursts",
            "🔥 Strong & focused",
            "🌊 Calm & steady",
        ],
    },
    {
        "key": "sleep",
        "question": "How much do you usually sleep?",
        "options": [
            "🌙 Under 6 hours",
            "🌙 6–7 hours",
            "🌙 7–8 hours",
            "🌙 Over 8 hours",
        ],
    },
    {
        "key": "stress",
        "question": "How has your mind felt lately?",
        "options": [
            "🌿 Calm",
            "🙂 A little busy",
            "😵 Stressed",
            "🌪️ Overwhelmed",
        ],
    },
    {
        "key": "meals",
        "question": "How regular are your meals?",
        "options": [
            "〰️ Unpredictable",
            "🥣 Somewhat irregular",
            "🍽️ Mostly regular",
            "🌿 Very consistent",
        ],
    },
    {
        "key": "routine",
        "question": "How does your routine feel?",
        "options": [
            "🌬️ Flexible",
            "📋 Structured",
            "🌱 Consistent",
        ],
    },
]


BODY_TYPES = {
    "Vata": {
        "emoji": "🌬️",
        "short": "Dynamic • Creative • Adaptable",
        "description": (
            "Traditionally associated with movement, creativity "
            "and change."
        ),
        "support": (
            "Regularity, grounding routines and intentional pauses."
        ),
    },
    "Pitta": {
        "emoji": "🔥",
        "short": "Focused • Driven • Energetic",
        "description": (
            "Traditionally associated with focus, intensity "
            "and purposeful action."
        ),
        "support": (
            "Balanced routines, cooling pauses and time to slow down."
        ),
    },
    "Kapha": {
        "emoji": "🌱",
        "short": "Steady • Calm • Grounded",
        "description": (
            "Traditionally associated with steadiness, stability "
            "and grounded energy."
        ),
        "support": (
            "Fresh movement, variety and energising routines."
        ),
    },
}


CHALLENGES = [
    {
        "id": "water",
        "emoji": "💧",
        "title": "Hydration Pause",
        "description": (
            "Drink one full glass of water slowly and mindfully."
        ),
        "why": (
            "A tiny pause can help you reconnect with your body's needs."
        ),
        "xp": 20,
        "badge": "Hydration Hero",
        "badge_emoji": "💧",
    },
    {
        "id": "movement",
        "emoji": "🌿",
        "title": "Movement Spark",
        "description": (
            "Give yourself 10 minutes of movement today."
        ),
        "why": (
            "Small bursts of movement can become easier everyday habits."
        ),
        "xp": 25,
        "badge": "Movement Spark",
        "badge_emoji": "🏃",
    },
    {
        "id": "meal",
        "emoji": "🥗",
        "title": "Mindful Meal",
        "description": (
            "Have one meal without your phone or another screen."
        ),
        "why": (
            "Less distraction can make an ordinary meal more intentional."
        ),
        "xp": 25,
        "badge": "Mindful Nourisher",
        "badge_emoji": "🥗",
    },
    {
        "id": "evening",
        "emoji": "🌙",
        "title": "Evening Reset",
        "description": (
            "Spend 20 screen-free minutes before bed."
        ),
        "why": (
            "A gentle transition can help create a calmer evening rhythm."
        ),
        "xp": 30,
        "badge": "Evening Guardian",
        "badge_emoji": "🌙",
    },
]


# ============================================================
# FUNCTIONS
# ============================================================

def go_to(page):
    st.session_state.page = page
    st.rerun()


def calculate_body_type():

    answers = st.session_state.answers

    vata = 0
    pitta = 0
    kapha = 0

    if "Lean" in answers.get("build", ""):
        vata += 2
    elif "Medium" in answers.get("build", ""):
        pitta += 2
    elif "Broad" in answers.get("build", ""):
        kapha += 2

    if "Changes" in answers.get("appetite", ""):
        vata += 2
    elif "Strong" in answers.get("appetite", ""):
        pitta += 2
    elif "Steady" in answers.get("appetite", ""):
        kapha += 2

    if "bursts" in answers.get("energy", "").lower():
        vata += 2
    elif "Strong" in answers.get("energy", ""):
        pitta += 2
    elif "Calm" in answers.get("energy", ""):
        kapha += 2

    if "Flexible" in answers.get("routine", ""):
        vata += 2
    elif "Structured" in answers.get("routine", ""):
        pitta += 2
    elif "Consistent" in answers.get("routine", ""):
        kapha += 2

    if "Mostly" in answers.get("activity", ""):
        vata += 1
    elif "Very" in answers.get("activity", ""):
        pitta += 1
    else:
        kapha += 1

    scores = {
        "Vata": vata,
        "Pitta": pitta,
        "Kapha": kapha,
    }

    dominant = max(scores, key=scores.get)

    st.session_state.vata = vata
    st.session_state.pitta = pitta
    st.session_state.kapha = kapha
    st.session_state.body_type = dominant
    st.session_state.profile_complete = True


def reset_journey():

    st.session_state.answers = {}
    st.session_state.question_index = 0
    st.session_state.profile_complete = False
    st.session_state.body_type = ""
    st.session_state.vata = 0
    st.session_state.pitta = 0
    st.session_state.kapha = 0


def next_challenge():

    completed = st.session_state.completed_challenges

    for challenge in CHALLENGES:
        if challenge["id"] not in completed:
            return challenge

    return None


def calculate_streak():

    dates = sorted(
        set(st.session_state.completion_dates),
        reverse=True,
    )

    if not dates:
        return 0

    today = date.today()

    if date.fromisoformat(dates[0]) != today:
        return 0

    streak = 1
    expected = today - timedelta(days=1)

    for item in dates[1:]:

        current = date.fromisoformat(item)

        if current == expected:
            streak += 1
            expected -= timedelta(days=1)
        else:
            break

    return streak


def complete_challenge(challenge):

    today = str(date.today())

    if challenge["id"] not in st.session_state.completed_challenges:
        st.session_state.completed_challenges.append(
            challenge["id"]
        )

    if today not in st.session_state.completion_dates:
        st.session_state.completion_dates.append(today)

        st.session_state.xp += challenge["xp"]

    st.session_state.streak = calculate_streak()

    if challenge["badge"] not in st.session_state.badges:
        st.session_state.badges.append(
            challenge["badge"]
        )

    st.session_state.last_reward = challenge
    st.session_state.active_challenge = None


# ============================================================
# NAVIGATION BAR
# ============================================================

def render_navigation():

    brand, *items = st.columns(
        [1.45] + [1] * len(NAVIGATION)
    )

    with brand:

        if st.button(
            "🌿 MYBIO",
            key="brand",
            use_container_width=True,
        ):
            go_to("Home")

    for index, item in enumerate(NAVIGATION):

        with items[index]:

            if st.button(
                item,
                key=f"nav_{index}",
                use_container_width=True,
            ):
                go_to(item)

    st.divider()


# ============================================================
# HOME
# ============================================================

def render_home():

    # --------------------------------------------------------
    # HERO
    # --------------------------------------------------------

    left, right = st.columns(
        [1.15, 0.85],
        gap="large",
    )

    with left:

        st.write("")
        st.write("")

        st.caption("🌿  YOUR RHYTHM · YOUR JOURNEY")

        st.title("Meet the\nyou within.")

        st.markdown(
            "**ANCIENT WISDOM · MODERN YOU · INFINITE POSSIBILITIES**"
        )

        st.write("")

        if st.button(
            "Begin your journey  →",
            type="primary",
            key="hero_begin",
        ):
            go_to("Journey")

        st.write("")

        st.caption(
            "Reflect. Understand. Grow."
        )

    with right:

        with st.container(border=True):

            st.markdown("## 🌿")

            st.markdown("### Find your rhythm.")

            st.write("")

            visual_one, visual_two = st.columns(2)

            with visual_one:

                st.markdown("## 🪷")
                st.caption("REFLECT")

            with visual_two:

                st.markdown("## 🌙")
                st.caption("RESET")

            st.write("")

            st.markdown("## ✨")

            st.caption(
                "A small journey toward a more intentional you."
            )

    st.write("")
    st.write("")
    st.divider()

    # --------------------------------------------------------
    # THREE STEPS
    # --------------------------------------------------------

    st.caption("THE MYBIO EXPERIENCE")

    st.header("Three steps. One journey.")

    st.write("")

    first, second, third = st.columns(
        3,
        gap="medium",
    )

    with first:

        with st.container(border=True):

            st.markdown("## 🧭")

            st.caption("01")

            st.subheader("Discover")

            st.write(
                "Reveal your everyday patterns."
            )

    with second:

        with st.container(border=True):

            st.markdown("## 🌿")

            st.caption("02")

            st.subheader("Understand")

            st.write(
                "Explore your traditional body-type pattern."
            )

    with third:

        with st.container(border=True):

            st.markdown("## 🎯")

            st.caption("03")

            st.subheader("Act")

            st.write(
                "Turn insight into tiny actions."
            )

    st.write("")
    st.write("")
    st.divider()

    # --------------------------------------------------------
    # PHILOSOPHY
    # --------------------------------------------------------

    left, right = st.columns(
        [0.8, 1.2],
        gap="large",
    )

    with left:

        st.markdown("## 🌱")

        st.caption("A DIFFERENT APPROACH")

    with right:

        st.header("Small shifts.")

        st.header("Deeper balance.")

        st.write(
            "No drastic transformations. "
            "Just meaningful moments, one at a time."
        )

    st.write("")
    st.write("")
    st.divider()

    # --------------------------------------------------------
    # FINAL CTA
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("## 🪷")

        st.header("Ready to meet yourself differently?")

        if st.button(
            "Start MYBIO  →",
            type="primary",
            key="home_final",
        ):
            go_to("Journey")


# ============================================================
# JOURNEY
# ============================================================

def render_journey():

    st.caption("🧭 MYBIO JOURNEY")

    if st.session_state.profile_complete:

        body = st.session_state.body_type
        info = BODY_TYPES[body]

        st.title("Your journey is complete.")

        st.write("Your rhythm has started to take shape.")

        st.write("")

        with st.container(border=True):

            st.markdown(
                f"## {info['emoji']}  {body}"
            )

            st.caption(info["short"])

            st.write(info["description"])

        st.write("")

        one, two = st.columns(2)

        with one:

            if st.button(
                "Explore my wellness →",
                type="primary",
                key="journey_wellness",
            ):
                go_to("My Wellness")

        with two:

            if st.button(
                "View my body type →",
                key="journey_body",
            ):
                go_to("Body Type")

        st.write("")

        if st.button(
            "Start again",
            key="journey_restart",
        ):
            reset_journey()
            st.rerun()

        return

    # --------------------------------------------------------
    # QUESTION
    # --------------------------------------------------------

    current = st.session_state.question_index
    total = len(QUESTIONS)

    st.progress(
        current / total
    )

    st.caption(
        f"QUESTION {current + 1}  /  {total}"
    )

    question = QUESTIONS[current]

    st.title(question["question"])

    st.caption(
        "Choose what feels most like you."
    )

    st.write("")

    options = question["options"]

    columns = st.columns(
        2,
        gap="medium",
    )

    for index, option in enumerate(options):

        with columns[index % 2]:

            if st.button(
                option,
                key=f"question_{current}_{index}",
                use_container_width=True,
            ):

                st.session_state.answers[
                    question["key"]
                ] = option

                if current < total - 1:

                    st.session_state.question_index += 1

                else:

                    calculate_body_type()

                st.rerun()

    st.write("")

    if current > 0:

        if st.button(
            "← Previous",
            key="previous_question",
        ):
            st.session_state.question_index -= 1
            st.rerun()


# ============================================================
# MY WELLNESS
# ============================================================

def render_wellness():

    st.caption("🌿 MY WELLNESS")

    if not st.session_state.profile_complete:

        st.title("Your wellness story starts here.")

        st.write(
            "Complete your Journey to unlock your profile."
        )

        if st.button(
            "Begin Journey →",
            type="primary",
            key="wellness_begin",
        ):
            go_to("Journey")

        return

    body = st.session_state.body_type
    info = BODY_TYPES[body]

    st.title("Your wellness snapshot.")

    st.caption(
        "A simple reflection of your MYBIO journey."
    )

    st.write("")

    one, two, three = st.columns(3)

    with one:
        st.metric(
            "XP",
            st.session_state.xp,
        )

    with two:
        st.metric(
            "STREAK",
            f"{st.session_state.streak} days",
        )

    with three:
        st.metric(
            "BADGES",
            len(st.session_state.badges),
        )

    st.write("")

    with st.container(border=True):

        st.markdown(
            f"## {info['emoji']}  {body}"
        )

        st.caption(info["short"])

        st.write(info["description"])

    st.write("")

    left, right = st.columns(2)

    with left:

        with st.container(border=True):

            st.subheader("🎯 Your focus")

            st.write(
                st.session_state.answers.get(
                    "goal",
                    "🌿 Balance",
                )
            )

    with right:

        with st.container(border=True):

            st.subheader("✨ Next")

            st.write(
                "Explore your pattern or take today's challenge."
            )

            if st.button(
                "Today's Challenge →",
                type="primary",
                key="wellness_challenge",
            ):
                go_to("Today’s Challenge")


# ============================================================
# BODY TYPE
# ============================================================

def render_body_type():

    st.caption("🌿 YOUR PATTERN")

    if not st.session_state.profile_complete:

        st.title("Your pattern is waiting.")

        st.write(
            "Complete the Journey to discover your "
            "Ayurvedic body-type interpretation."
        )

        if st.button(
            "Start Journey →",
            type="primary",
            key="bodytype_start",
        ):
            go_to("Journey")

        return

    body = st.session_state.body_type
    info = BODY_TYPES[body]

    st.title(
        f"{info['emoji']} {body}"
    )

    st.caption(
        "YOUR AYURVEDIC BODY-TYPE PATTERN"
    )

    st.write(
        "An educational interpretation inspired by "
        "traditional Ayurvedic concepts."
    )

    st.write("")

    with st.container(border=True):

        st.subheader(info["short"])

        st.write(info["description"])

        st.write("")

        st.markdown(
            "**What may support your balance**"
        )

        st.write(info["support"])

    st.write("")
    st.divider()

    st.subheader("Explore the three patterns")

    cards = st.columns(3)

    for index, (name, data) in enumerate(
        BODY_TYPES.items()
    ):

        with cards[index]:

            with st.container(border=True):

                st.markdown(
                    f"## {data['emoji']}"
                )

                st.subheader(name)

                st.caption(data["short"])

                if name == body:
                    st.success("YOUR PATTERN")


# ============================================================
# TODAY'S CHALLENGE
# ============================================================

def render_challenge():

    st.caption("🎯 TODAY'S CHALLENGE")

    # --------------------------------------------------------
    # REWARD
    # --------------------------------------------------------

    if st.session_state.last_reward:

        reward = st.session_state.last_reward

        st.title("You did it. ✨")

        st.caption("A SMALL WIN IS STILL A WIN.")

        st.write("")

        with st.container(border=True):

            st.markdown(
                f"## {reward['badge_emoji']}"
            )

            st.caption("BADGE UNLOCKED")

            st.header(
                reward["badge"]
            )

            st.metric(
                "XP EARNED",
                f"+{reward['xp']}",
            )

        st.balloons()

        st.write("")

        if st.button(
            "Continue →",
            type="primary",
            key="reward_continue",
        ):

            st.session_state.last_reward = None
            go_to("My Rhythm")

        return

    challenge = next_challenge()

    # --------------------------------------------------------
    # COMPLETE
    # --------------------------------------------------------

    if challenge is None:

        st.title("You've done them all. 🏆")

        st.write(
            "Your challenge collection is complete."
        )

        if st.button(
            "See my rhythm →",
            type="primary",
            key="all_challenges",
        ):
            go_to("My Rhythm")

        return

    # --------------------------------------------------------
    # CHALLENGE CARD
    # --------------------------------------------------------

    st.title(
        f"{challenge['emoji']} {challenge['title']}"
    )

    st.caption(
        "ONE SMALL ACTION FOR TODAY"
    )

    st.write("")

    with st.container(border=True):

        st.header(
            challenge["description"]
        )

        st.write("")

        st.info(
            f"💡 {challenge['why']}"
        )

        st.write("")

        if (
            st.session_state.active_challenge
            != challenge["id"]
        ):

            if st.button(
                "I'm ready  →",
                type="primary",
                key="challenge_start",
            ):

                st.session_state.active_challenge = (
                    challenge["id"]
                )

                st.rerun()

        else:

            st.success(
                "Challenge active. Take your moment."
            )

            if st.button(
                "I completed it  ✓",
                type="primary",
                key="challenge_complete",
            ):

                complete_challenge(challenge)

                st.rerun()


# ============================================================
# MY RHYTHM
# ============================================================

def render_rhythm():

    st.caption("🔥 MY RHYTHM")

    st.title("Your rhythm is growing.")

    one, two, three = st.columns(3)

    with one:
        st.metric(
            "🔥 STREAK",
            st.session_state.streak,
        )

    with two:
        st.metric(
            "✨ XP",
            st.session_state.xp,
        )

    with three:
        st.metric(
            "🏆 BADGES",
            len(st.session_state.badges),
        )

    st.write("")
    st.divider()

    st.subheader("Your week")

    days = [
        date.today() - timedelta(days=x)
        for x in range(6, -1, -1)
    ]

    columns = st.columns(7)

    for index, day in enumerate(days):

        with columns[index]:

            completed = str(day) in (
                st.session_state.completion_dates
            )

            st.caption(
                day.strftime("%a")
            )

            if completed:
                st.success("✓")
            else:
                st.info("·")

            st.caption(
                day.strftime("%d")
            )

    st.write("")
    st.divider()

    st.subheader("Your badges")

    if not st.session_state.badges:

        with st.container(border=True):

            st.markdown("## 🏅")

            st.subheader(
                "Your first badge is waiting."
            )

            if st.button(
                "Take today's challenge →",
                type="primary",
                key="empty_badges",
            ):
                go_to("Today’s Challenge")

    else:

        count = len(st.session_state.badges)

        columns = st.columns(
            min(count, 4)
        )

        for index, badge in enumerate(
            st.session_state.badges
        ):

            emoji = "🏅"

            for challenge in CHALLENGES:

                if challenge["badge"] == badge:
                    emoji = challenge["badge_emoji"]

            with columns[index % len(columns)]:

                with st.container(border=True):

                    st.markdown(
                        f"## {emoji}"
                    )

                    st.subheader(badge)

                    st.caption("UNLOCKED")


# ============================================================
# FOR YOU
# ============================================================

def render_for_you():

    st.caption("✨ FOR YOU")

    if not st.session_state.profile_complete:

        st.title("This space will become yours.")

        st.write(
            "Complete your Journey to unlock "
            "personalised suggestions."
        )

        if st.button(
            "Begin Journey →",
            type="primary",
            key="foryou_start",
        ):
            go_to("Journey")

        return

    body = st.session_state.body_type

    st.title("A little something for you.")

    st.caption(
        f"Based on your {body} pattern."
    )

    st.write("")

    recommendations = [
        (
            "🌿",
            "Create an anchor",
            "Choose one tiny habit and repeat it around the same time."
        ),
        (
            "💧",
            "Pause",
            "Use ordinary moments as reminders to check in with yourself."
        ),
        (
            "🌙",
            "Protect your evening",
            "Create a small transition between your day and bedtime."
        ),
        (
            "🧘",
            "Notice first",
            "Observe your rhythm before deciding what needs to change."
        ),
    ]

    left, right = st.columns(2)

    for index, item in enumerate(
        recommendations
    ):

        emoji, title, description = item

        target = left if index % 2 == 0 else right

        with target:

            with st.container(border=True):

                st.markdown(
                    f"## {emoji}"
                )

                st.subheader(title)

                st.write(description)

    st.write("")

    if st.button(
        "Try today's challenge →",
        type="primary",
        key="foryou_challenge",
    ):
        go_to("Today’s Challenge")


# ============================================================
# ABOUT
# ============================================================

def render_about():

    st.caption("🌿 ABOUT MYBIO")

    st.title("Ancient wisdom.")

    st.title("Modern you.")

    st.write(
        "MYBIO brings reflection, traditional wellness concepts "
        "and everyday action into one interactive experience."
    )

    st.write("")
    st.divider()

    one, two, three = st.columns(3)

    with one:

        with st.container(border=True):

            st.markdown("## 🧭")

            st.subheader("Reflect")

            st.write(
                "Pause and notice your everyday patterns."
            )

    with two:

        with st.container(border=True):

            st.markdown("## 🌿")

            st.subheader("Understand")

            st.write(
                "Explore traditional wellness ideas."
            )

    with three:

        with st.container(border=True):

            st.markdown("## 🎯")

            st.subheader("Experiment")

            st.write(
                "Try small actions that fit your rhythm."
            )

    st.write("")
    st.divider()

    st.header("A note on wellness")

    st.info(
        "MYBIO is an educational wellness experience. "
        "Its Ayurvedic body-type interpretation is based on "
        "traditional concepts and is not a medical diagnosis "
        "or a substitute for professional medical advice."
    )

    st.write("")
    st.write("")

    st.markdown(
        "**ANCIENT WISDOM · MODERN YOU · INFINITE POSSIBILITIES**"
    )


# ============================================================
# PAGE ROUTER
# ============================================================

render_navigation()

current_page = st.session_state.page

if current_page == "Home":
    render_home()

elif current_page == "Journey":
    render_journey()

elif current_page == "My Wellness":
    render_wellness()

elif current_page == "Body Type":
    render_body_type()

elif current_page == "Today’s Challenge":
    render_challenge()

elif current_page == "My Rhythm":
    render_rhythm()

elif current_page == "For You":
    render_for_you()

elif current_page == "About":
    render_about()


# ============================================================
# FOOTER
# ============================================================

st.write("")
st.write("")

st.caption(
    "MYBIO  ·  YOUR RHYTHM · YOUR JOURNEY"
)
