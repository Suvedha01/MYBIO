import streamlit as st
from datetime import date, timedelta


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="MYBIO · Your Rhythm, Your Journey",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# GLOBAL STYLE
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

    /* ---------- APP ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 90% 5%,
                rgba(201, 173, 128, 0.20),
                transparent 25%
            ),
            radial-gradient(
                circle at 5% 35%,
                rgba(126, 157, 134, 0.14),
                transparent 28%
            ),
            #EAE2D6;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* ---------- TYPOGRAPHY ---------- */

    html,
    body,
    [class*="css"] {
        font-family: "DM Sans", sans-serif;
    }

    h1,
    h2,
    h3 {
        font-family: "Playfair Display", Georgia, serif !important;
        color: #26332C !important;
    }

    h1 {
        font-size: 4.2rem !important;
        line-height: 1.03 !important;
        letter-spacing: -2px !important;
    }

    h2 {
        font-size: 2.5rem !important;
        line-height: 1.15 !important;
    }

    h3 {
        font-size: 1.55rem !important;
    }

    p {
        color: #505A53;
        line-height: 1.7;
    }

    /* ---------- NAVIGATION ---------- */

    .stButton > button {
        border-radius: 999px;
        border: 1px solid rgba(72, 91, 76, 0.14);
        background: rgba(255, 253, 248, 0.82);
        color: #344239;
        font-weight: 600;
        transition: all 0.25s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        border-color: rgba(82, 107, 89, 0.35);
        box-shadow: 0 10px 24px rgba(58, 69, 61, 0.12);
        color: #26332C;
    }

    /* ---------- PRIMARY BUTTON ---------- */

    button[kind="primary"] {
        background: #526B59 !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 10px 25px rgba(62, 81, 66, 0.20);
    }

    button[kind="primary"]:hover {
        background: #405646 !important;
        color: white !important;
        transform: translateY(-3px);
    }

    /* ---------- CARDS ---------- */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 253, 248, 0.78);
        border: 1px solid rgba(82, 107, 89, 0.13);
        border-radius: 24px;
        padding: 1rem;
        transition:
            transform 0.3s ease,
            box-shadow 0.3s ease;
    }

    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 18px 38px rgba(57, 69, 61, 0.11);
    }

    /* ---------- METRICS ---------- */

    [data-testid="stMetric"] {
        background: rgba(255, 253, 248, 0.78);
        border: 1px solid rgba(82, 107, 89, 0.12);
        border-radius: 20px;
        padding: 1rem;
        animation: fadeUp 0.6s ease both;
    }

    [data-testid="stMetricValue"] {
        color: #526B59;
    }

    /* ---------- PROGRESS ---------- */

    .stProgress > div > div > div > div {
        background: #526B59;
    }

    /* ---------- ALERTS ---------- */

    [data-testid="stAlert"] {
        border-radius: 18px;
    }

    /* ---------- INPUTS ---------- */

    div[data-baseweb="select"] > div {
        border-radius: 14px;
        background: rgba(255, 253, 248, 0.9);
    }

    input {
        border-radius: 14px !important;
    }

    /* ---------- ANIMATIONS ---------- */

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(14px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes float {
        0%, 100% {
            transform: translateY(0px);
        }

        50% {
            transform: translateY(-9px);
        }
    }

    /* ---------- MOBILE ---------- */

    @media (max-width: 768px) {

        h1 {
            font-size: 3rem !important;
        }

        h2 {
            font-size: 2rem !important;
        }

        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

DEFAULTS = {
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

for key, value in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# DATA
# ============================================================

NAV_ITEMS = [
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
        "title": "What would you like to improve right now?",
        "options": [
            "⚡ More energy",
            "🌙 Better sleep",
            "🧘 More calm",
            "🥗 Better nourishment",
            "🏃 More movement",
            "🌿 Overall balance",
        ],
    },
    {
        "key": "activity",
        "title": "How does movement usually fit into your day?",
        "options": [
            "🪑 Mostly sitting",
            "🚶 Lightly active",
            "🏃 Quite active",
            "🔥 Very active",
        ],
    },
    {
        "key": "build",
        "title": "Which description feels closest to you?",
        "options": [
            "🌬️ Lean and light",
            "🔥 Medium and athletic",
            "🌱 Broad and solid",
        ],
    },
    {
        "key": "appetite",
        "title": "How would you describe your appetite?",
        "options": [
            "〰️ It changes a lot",
            "🔥 Strong and regular",
            "🌿 Steady and moderate",
        ],
    },
    {
        "key": "energy",
        "title": "How does your energy usually feel?",
        "options": [
            "⚡ Bursts of energy",
            "🔥 Strong and focused",
            "🌊 Calm and steady",
        ],
    },
    {
        "key": "sleep",
        "title": "How much do you usually sleep?",
        "options": [
            "🌙 Less than 6 hours",
            "🌙 6–7 hours",
            "🌙 7–8 hours",
            "🌙 More than 8 hours",
        ],
    },
    {
        "key": "stress",
        "title": "How has your stress level felt lately?",
        "options": [
            "🌿 Mostly calm",
            "🙂 A little busy",
            "😵 Quite stressful",
            "🌪️ Very overwhelming",
        ],
    },
    {
        "key": "meals",
        "title": "How regular are your meals?",
        "options": [
            "〰️ Quite unpredictable",
            "🥣 Somewhat irregular",
            "🍽️ Mostly regular",
            "🌿 Very consistent",
        ],
    },
    {
        "key": "routine",
        "title": "How does your daily routine feel?",
        "options": [
            "🌬️ Flexible",
            "📋 Structured",
            "🌱 Very consistent",
        ],
    },
]


CHALLENGES = [
    {
        "id": "water",
        "emoji": "💧",
        "title": "Hydration Pause",
        "description": "Take a quiet moment to drink a full glass of water mindfully.",
        "why": "A simple pause can help you reconnect with what your body needs.",
        "xp": 20,
        "badge": "Hydration Hero",
        "badge_emoji": "💧",
    },
    {
        "id": "movement",
        "emoji": "🌿",
        "title": "Movement Spark",
        "description": "Take 10 minutes today for any movement that feels good.",
        "why": "Small amounts of movement can be easier to build into everyday life.",
        "xp": 25,
        "badge": "Movement Spark",
        "badge_emoji": "🏃",
    },
    {
        "id": "meal",
        "emoji": "🥗",
        "title": "Mindful Meal",
        "description": "Have one meal today without a screen. Slow down and notice each bite.",
        "why": "Removing distractions can make an everyday meal feel more intentional.",
        "xp": 25,
        "badge": "Mindful Nourisher",
        "badge_emoji": "🥗",
    },
    {
        "id": "evening",
        "emoji": "🌙",
        "title": "Evening Reset",
        "description": "Spend 20 screen-free minutes before bed.",
        "why": "Creating a calmer transition into the evening can support a more intentional bedtime routine.",
        "xp": 30,
        "badge": "Evening Guardian",
        "badge_emoji": "🌙",
    },
]


BODY_TYPES = {
    "Vata": {
        "emoji": "🌬️",
        "title": "Vata",
        "description": "Often associated with movement, creativity, adaptability and change.",
        "strength": "Creative • Curious • Dynamic",
        "balance": "Regular routines, grounding habits and intentional pauses.",
    },
    "Pitta": {
        "emoji": "🔥",
        "title": "Pitta",
        "description": "Often associated with focus, intensity, transformation and purposeful action.",
        "strength": "Focused • Driven • Energetic",
        "balance": "Cooling pauses, balanced routines and space to slow down.",
    },
    "Kapha": {
        "emoji": "🌱",
        "title": "Kapha",
        "description": "Often associated with steadiness, stability, patience and grounded energy.",
        "strength": "Steady • Calm • Grounded",
        "balance": "Fresh movement, variety and energising routines.",
    },
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def navigate(page):
    st.session_state.page = page
    st.rerun()


def reset_journey():
    st.session_state.answers = {}
    st.session_state.question_index = 0
    st.session_state.profile_complete = False
    st.session_state.body_type = ""
    st.session_state.vata = 0
    st.session_state.pitta = 0
    st.session_state.kapha = 0
    st.session_state.active_challenge = None
    st.session_state.last_reward = None


def calculate_body_type():
    answers = st.session_state.answers

    vata = 0
    pitta = 0
    kapha = 0

    build = answers.get("build", "")
    appetite = answers.get("appetite", "")
    energy = answers.get("energy", "")
    routine = answers.get("routine", "")
    activity = answers.get("activity", "")

    if "Lean" in build:
        vata += 2
    elif "Medium" in build:
        pitta += 2
    else:
        kapha += 2

    if "changes" in appetite:
        vata += 2
    elif "Strong" in appetite:
        pitta += 2
    else:
        kapha += 2

    if "Bursts" in energy:
        vata += 2
    elif "Strong" in energy:
        pitta += 2
    else:
        kapha += 2

    if "Flexible" in routine:
        vata += 2
    elif "Structured" in routine:
        pitta += 1
        kapha += 1
    else:
        kapha += 2

    if "Mostly" in activity:
        vata += 1
    elif "Very" in activity:
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


def get_next_challenge():
    completed = st.session_state.completed_challenges

    for challenge in CHALLENGES:
        if challenge["id"] not in completed:
            return challenge

    return None


def calculate_streak():
    dates = st.session_state.completion_dates

    if not dates:
        return 0

    unique_dates = sorted(set(dates), reverse=True)

    today = date.today()
    latest = date.fromisoformat(unique_dates[0])

    if latest != today:
        return 0

    streak = 1
    expected = today - timedelta(days=1)

    for date_string in unique_dates[1:]:
        current = date.fromisoformat(date_string)

        if current == expected:
            streak += 1
            expected -= timedelta(days=1)
        else:
            break

    return streak


def complete_challenge(challenge):
    today = str(date.today())

    if challenge["id"] not in st.session_state.completed_challenges:
        st.session_state.completed_challenges.append(challenge["id"])

    if today not in st.session_state.completion_dates:
        st.session_state.completion_dates.append(today)

    st.session_state.xp += challenge["xp"]
    st.session_state.streak = calculate_streak()

    if challenge["badge"] not in st.session_state.badges:
        st.session_state.badges.append(challenge["badge"])

    st.session_state.last_reward = challenge
    st.session_state.active_challenge = None


# ============================================================
# NAVIGATION
# ============================================================

def render_navigation():

    left, *nav_columns = st.columns([1.5] + [1] * len(NAV_ITEMS))

    with left:
        if st.button(
            "🌿 MYBIO",
            key="brand_button",
            use_container_width=True,
        ):
            navigate("Home")

    for index, item in enumerate(NAV_ITEMS):
        with nav_columns[index]:
            if st.button(
                item,
                key=f"nav_{item}",
                use_container_width=True,
            ):
                navigate(item)

    st.divider()


# ============================================================
# HOME
# ============================================================

def render_home():

    hero_left, hero_right = st.columns(
        [1.25, 0.75],
        gap="large",
    )

    with hero_left:

        st.caption("🌿  DISCOVER YOUR EVERYDAY RHYTHM")

        st.title("Meet the you within.")

        st.write(
            "A more personal approach to everyday wellness. "
            "Explore your natural patterns, understand your rhythm "
            "and turn tiny moments into meaningful habits."
        )

        st.write("")

        st.markdown(
            "**ANCIENT WISDOM · MODERN YOU · INFINITE POSSIBILITIES**"
        )

        st.write("")

        if st.button(
            "Begin your journey  →",
            type="primary",
            key="home_hero",
        ):
            navigate("Journey")

    with hero_right:

        st.write("")

        with st.container(border=True):
            st.markdown("## 🌿")
            st.markdown("### Your everyday rhythm")

            st.write(
                "Reflect on how you move, rest, eat, think "
                "and experience your day."
            )

            st.write("")

            metric1, metric2 = st.columns(2)

            with metric1:
                st.metric("STEP", "01")

            with metric2:
                st.metric("PATH", "∞")

    st.write("")
    st.write("")
    st.divider()

    # --------------------------------------------------------
    # INTRO
    # --------------------------------------------------------

    st.header("Wellness starts with awareness.")

    st.write(
        "MYBIO is designed around one simple idea: understanding "
        "your patterns can make everyday choices feel more intentional."
    )

    st.write("")

    discover, understand, action = st.columns(3, gap="medium")

    with discover:
        with st.container(border=True):
            st.subheader("🧭 Discover")
            st.write(
                "Answer a handful of thoughtful questions "
                "about your everyday rhythm."
            )
            st.caption("01  ·  REFLECT")

    with understand:
        with st.container(border=True):
            st.subheader("🌿 Understand")
            st.write(
                "Explore an educational Ayurvedic body-type "
                "interpretation based on your responses."
            )
            st.caption("02  ·  LEARN")

    with action:
        with st.container(border=True):
            st.subheader("🎯 Take action")
            st.write(
                "Turn awareness into small challenges that "
                "fit naturally into your day."
            )
            st.caption("03  ·  GROW")

    st.write("")
    st.write("")
    st.divider()

    # --------------------------------------------------------
    # PHILOSOPHY
    # --------------------------------------------------------

    philosophy_left, philosophy_right = st.columns(
        [0.6, 1.4],
        gap="large",
    )

    with philosophy_left:
        st.markdown("## 🌱")
        st.caption("THE MYBIO PHILOSOPHY")

    with philosophy_right:
        st.header("Small shifts. Deeper balance.")

        st.write(
            "You don't need to transform your entire life overnight. "
            "Sometimes the smallest intentional choice is where "
            "everything begins."
        )

        st.write("")

        one, two, three = st.columns(3)

        with one:
            st.metric("REFLECT", "01")

        with two:
            st.metric("UNDERSTAND", "02")

        with three:
            st.metric("GROW", "03")

    st.write("")
    st.write("")
    st.divider()

    # --------------------------------------------------------
    # FINAL CTA
    # --------------------------------------------------------

    with st.container(border=True):
        st.header("Your journey starts here.")

        st.write(
            "A few questions. A little reflection. "
            "A clearer picture of your everyday rhythm."
        )

        if st.button(
            "Start MYBIO  →",
            type="primary",
            key="home_bottom",
        ):
            navigate("Journey")


# ============================================================
# JOURNEY
# ============================================================

def render_journey():

    st.caption("🌿 YOUR MYBIO JOURNEY")

    if st.session_state.profile_complete:

        st.title("Your journey is complete.")

        st.write(
            "Your responses have created your personal wellness profile."
        )

        st.write("")

        left, right = st.columns(2)

        with left:
            with st.container(border=True):
                st.subheader("🌿 Your pattern")
                body = st.session_state.body_type
                st.markdown(
                    f"### {BODY_TYPES[body]['emoji']} {body}"
                )
                st.write(BODY_TYPES[body]["description"])

        with right:
            with st.container(border=True):
                st.subheader("🎯 What's next?")
                st.write(
                    "Explore your Body Type, check your recommendations "
                    "and try today's challenge."
                )

                if st.button(
                    "Explore my wellness →",
                    type="primary",
                    key="journey_complete_next",
                ):
                    navigate("My Wellness")

        st.write("")

        if st.button(
            "Restart journey",
            key="restart_journey",
        ):
            reset_journey()
            st.rerun()

        return

    current = st.session_state.question_index
    total = len(QUESTIONS)

    progress = current / total

    st.progress(progress)

    st.caption(f"QUESTION {current + 1} OF {total}")

    question = QUESTIONS[current]

    st.header(question["title"])

    st.write("")

    options = question["options"]

    columns = st.columns(2, gap="medium")

    for index, option in enumerate(options):

        with columns[index % 2]:

            if st.button(
                option,
                key=f"answer_{question['key']}_{index}",
                use_container_width=True,
            ):
                st.session_state.answers[question["key"]] = option

                if current < total - 1:
                    st.session_state.question_index += 1
                    st.rerun()
                else:
                    calculate_body_type()
                    st.rerun()

    st.write("")

    if current > 0:

        if st.button(
            "← Previous",
            key="journey_previous",
        ):
            st.session_state.question_index -= 1
            st.rerun()

    st.write("")

    st.caption(
        "There are no right or wrong answers. "
        "Choose what feels most like you."
    )


# ============================================================
# MY WELLNESS
# ============================================================

def render_wellness():

    st.caption("🌿 YOUR WELLNESS")

    if not st.session_state.profile_complete:

        st.title("Your story is waiting to unfold.")

        st.write(
            "Complete your MYBIO journey to see your personal "
            "wellness profile here."
        )

        st.write("")

        with st.container(border=True):
            st.markdown("## 🧭")
            st.subheader("Start with reflection")

            st.write(
                "Your profile begins with a few simple questions "
                "about your everyday rhythm."
            )

            if st.button(
                "Begin Journey →",
                type="primary",
                key="wellness_start",
            ):
                navigate("Journey")

        return

    body = st.session_state.body_type
    information = BODY_TYPES[body]

    st.title("Your wellness snapshot.")

    st.write(
        "A simple reflection of the patterns you shared "
        "during your journey."
    )

    st.write("")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("XP", st.session_state.xp)

    with m2:
        st.metric("STREAK", f"{st.session_state.streak} days")

    with m3:
        st.metric(
            "BADGES",
            len(st.session_state.badges),
        )

    st.write("")

    with st.container(border=True):

        left, right = st.columns([0.5, 1.5])

        with left:
            st.markdown(f"## {information['emoji']}")

        with right:
            st.caption("AYURVEDIC BODY-TYPE PATTERN")
            st.header(body)
            st.write(information["description"])
            st.caption(information["strength"])

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):
            st.subheader("🌱 Your direction")

            goal = st.session_state.answers.get(
                "goal",
                "Overall balance",
            )

            st.write(
                f"Your current focus: **{goal}**"
            )

            st.write(
                "Use this as a starting point for small, "
                "consistent choices."
            )

    with col2:

        with st.container(border=True):
            st.subheader("✨ Explore next")

            st.write(
                "Learn more about your body-type pattern "
                "or discover your next challenge."
            )

            if st.button(
                "View Body Type →",
                key="wellness_body",
            ):
                navigate("Body Type")


# ============================================================
# BODY TYPE
# ============================================================

def render_body_type():

    st.caption("🌿 UNDERSTAND YOUR PATTERN")

    if not st.session_state.profile_complete:

        st.title("There is a pattern waiting to emerge.")

        st.write(
            "Complete the Journey first to receive your "
            "Ayurvedic body-type interpretation."
        )

        if st.button(
            "Start Journey →",
            type="primary",
            key="body_start",
        ):
            navigate("Journey")

        return

    body = st.session_state.body_type
    information = BODY_TYPES[body]

    st.title(
        f"{information['emoji']} Your Ayurvedic body-type pattern"
    )

    st.write(
        "This is an educational interpretation inspired by "
        "traditional Ayurvedic concepts. It is not a medical diagnosis."
    )

    st.write("")

    with st.container(border=True):

        st.caption("YOUR DOMINANT PATTERN")

        st.header(body)

        st.write(information["description"])

        st.write("")

        st.subheader("Your natural strengths")

        st.info(information["strength"])

        st.subheader("What may support balance")

        st.write(information["balance"])

    st.write("")
    st.write("")

    st.subheader("The three traditional patterns")

    cards = st.columns(3, gap="medium")

    for index, (name, info) in enumerate(BODY_TYPES.items()):

        with cards[index]:

            with st.container(border=True):

                st.markdown(f"## {info['emoji']}")

                st.subheader(name)

                st.write(info["description"])

                if name == body:
                    st.success("Your current pattern")


# ============================================================
# TODAY'S CHALLENGE
# ============================================================

def render_challenge():

    st.caption("🎯 TODAY'S CHALLENGE")

    # --------------------------------------------------------
    # REWARD STATE
    # --------------------------------------------------------

    if st.session_state.last_reward:

        reward = st.session_state.last_reward

        st.title("You did it. 🌟")

        st.write(
            "One small action completed. That's how a rhythm begins."
        )

        st.write("")

        with st.container(border=True):

            st.markdown(
                f"## {reward['badge_emoji']}"
            )

            st.caption("NEW BADGE UNLOCKED")

            st.header(reward["badge"])

            st.metric(
                "REWARD",
                f"+{reward['xp']} XP",
            )

        st.write("")

        st.balloons()

        if st.button(
            "See my rhythm →",
            type="primary",
            key="reward_rhythm",
        ):
            st.session_state.last_reward = None
            navigate("My Rhythm")

        return

    # --------------------------------------------------------
    # ALL COMPLETE
    # --------------------------------------------------------

    challenge = get_next_challenge()

    if challenge is None:

        st.title("You've completed today's collection. 🌿")

        st.write(
            "You have explored every MYBIO challenge currently available."
        )

        st.write("")

        with st.container(border=True):

            st.markdown("## 🏆")

            st.subheader("Challenge collection complete")

            st.write(
                "Come back to your rhythm and keep building "
                "small, meaningful habits."
            )

        return

    # --------------------------------------------------------
    # CHALLENGE
    # --------------------------------------------------------

    st.title(
        f"{challenge['emoji']} {challenge['title']}"
    )

    st.write(
        "One small action. No pressure. Just a moment for yourself."
    )

    st.write("")

    with st.container(border=True):

        st.caption("YOUR NEXT STEP")

        st.header(challenge["title"])

        st.write(challenge["description"])

        st.write("")

        st.info(
            f"💡 {challenge['why']}"
        )

        st.write("")

        if st.session_state.active_challenge != challenge["id"]:

            if st.button(
                "I'm ready →",
                type="primary",
                key=f"start_{challenge['id']}",
            ):
                st.session_state.active_challenge = challenge["id"]
                st.rerun()

        else:

            st.success(
                "Your challenge is active. Take your moment."
            )

            if st.button(
                "I completed it ✓",
                type="primary",
                key=f"complete_{challenge['id']}",
            ):
                complete_challenge(challenge)
                st.rerun()


# ============================================================
# MY RHYTHM
# ============================================================

def render_rhythm():

    st.caption("🔥 YOUR RHYTHM")

    st.title("Keep your rhythm going.")

    st.write(
        "Every completed challenge becomes part of your journey."
    )

    st.write("")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            "🔥 CURRENT STREAK",
            f"{st.session_state.streak}",
        )

    with m2:
        st.metric(
            "✨ XP",
            st.session_state.xp,
        )

    with m3:
        st.metric(
            "🏆 BADGES",
            len(st.session_state.badges),
        )

    st.write("")
    st.divider()

    # --------------------------------------------------------
    # WEEK
    # --------------------------------------------------------

    st.subheader("Your week")

    days = []

    for offset in range(6, -1, -1):

        current_day = date.today() - timedelta(days=offset)

        days.append(current_day)

    columns = st.columns(7)

    for index, current_day in enumerate(days):

        with columns[index]:

            completed = str(current_day) in (
                st.session_state.completion_dates
            )

            st.markdown(
                f"**{current_day.strftime('%a')}**"
            )

            if completed:
                st.success("✓")
            else:
                st.info("·")

            st.caption(
                current_day.strftime("%d")
            )

    st.write("")
    st.divider()

    # --------------------------------------------------------
    # BADGES
    # --------------------------------------------------------

    st.subheader("Your badge shelf")

    if not st.session_state.badges:

        with st.container(border=True):

            st.markdown("## 🏅")

            st.subheader("Your first badge is waiting.")

            st.write(
                "Complete your first challenge and it will appear here."
            )

            if st.button(
                "Take today's challenge →",
                type="primary",
                key="rhythm_challenge",
            ):
                navigate("Today’s Challenge")

    else:

        badge_columns = st.columns(
            min(4, len(st.session_state.badges))
        )

        for index, badge in enumerate(
            st.session_state.badges
        ):

            with badge_columns[index % len(badge_columns)]:

                with st.container(border=True):

                    badge_emoji = "🏅"

                    for challenge in CHALLENGES:
                        if challenge["badge"] == badge:
                            badge_emoji = challenge["badge_emoji"]

                    st.markdown(f"## {badge_emoji}")

                    st.subheader(badge)

                    st.caption("UNLOCKED")


# ============================================================
# FOR YOU
# ============================================================

def render_for_you():

    st.caption("✨ PERSONAL NOTES")

    if not st.session_state.profile_complete:

        st.title("This space will become yours.")

        st.write(
            "Complete your Journey and MYBIO will use your "
            "responses to shape simple, relevant suggestions."
        )

        if st.button(
            "Begin Journey →",
            type="primary",
            key="for_you_start",
        ):
            navigate("Journey")

        return

    body = st.session_state.body_type
    goal = st.session_state.answers.get(
        "goal",
        "🌿 Overall balance",
    )

    st.title("A few ideas for you.")

    st.write(
        f"Based on your current focus — **{goal}** — "
        f"and your **{body}** pattern."
    )

    st.write("")

    recommendations = [
        (
            "🌿 Create one anchor habit",
            "Choose one small action you can repeat around the same "
            "time each day."
        ),
        (
            "💧 Add intentional pauses",
            "Use ordinary moments such as drinking water or walking "
            "as opportunities to reconnect with yourself."
        ),
        (
            "🌙 Protect your evening",
            "Give yourself a short transition between a busy day "
            "and bedtime."
        ),
        (
            "🧘 Notice before changing",
            "Spend a moment observing your energy and routine "
            "before deciding what needs to change."
        ),
    ]

    cards = st.columns(2, gap="medium")

    for index, (title, description) in enumerate(
        recommendations
    ):

        with cards[index % 2]:

            with st.container(border=True):

                st.subheader(title)

                st.write(description)

    st.write("")
    st.divider()

    with st.container(border=True):

        st.subheader("🎯 Want something more practical?")

        st.write(
            "Try today's challenge and turn one idea into action."
        )

        if st.button(
            "View today's challenge →",
            type="primary",
            key="for_you_challenge",
        ):
            navigate("Today’s Challenge")


# ============================================================
# ABOUT
# ============================================================

def render_about():

    st.caption("🌿 ABOUT MYBIO")

    st.title("Ancient wisdom. Reimagined for everyday life.")

    st.write(
        "MYBIO is an interactive wellness experience designed "
        "to help people reflect on their everyday patterns, "
        "explore traditional wellness concepts and build "
        "small intentional habits."
    )

    st.write("")
    st.divider()

    purpose, journey, philosophy = st.columns(
        3,
        gap="medium",
    )

    with purpose:

        with st.container(border=True):

            st.markdown("## 🌿")

            st.subheader("Our purpose")

            st.write(
                "Make self-reflection feel approachable, "
                "beautiful and engaging."
            )

    with journey:

        with st.container(border=True):

            st.markdown("## 🧭")

            st.subheader("The journey")

            st.write(
                "Reflect → understand → experiment → build "
                "your own rhythm."
            )

    with philosophy:

        with st.container(border=True):

            st.markdown("## ✨")

            st.subheader("The philosophy")

            st.write(
                "Small, consistent actions can create meaningful "
                "changes in everyday life."
            )

    st.write("")
    st.divider()

    st.header("A note on wellness")

    st.info(
        "MYBIO provides educational and reflective wellness content. "
        "Its Ayurvedic body-type interpretation is based on traditional "
        "concepts and is not a medical diagnosis or a substitute for "
        "professional medical advice."
    )

    st.write("")
    st.divider()

    st.markdown(
        "**ANCIENT WISDOM · MODERN YOU · INFINITE POSSIBILITIES**"
    )

    st.caption(
        "MYBIO · YOUR RHYTHM · YOUR JOURNEY"
    )


# ============================================================
# PAGE ROUTER
# ============================================================

render_navigation()

page = st.session_state.page

if page == "Home":
    render_home()

elif page == "Journey":
    render_journey()

elif page == "My Wellness":
    render_wellness()

elif page == "Body Type":
    render_body_type()

elif page == "Today’s Challenge":
    render_challenge()

elif page == "My Rhythm":
    render_rhythm()

elif page == "For You":
    render_for_you()

elif page == "About":
    render_about()


# ============================================================
# FOOTER
# ============================================================

st.write("")
st.write("")

st.caption(
    "MYBIO  ·  YOUR RHYTHM · YOUR JOURNEY  ·  "
    "Ancient wisdom, modern perspective."
)
