import streamlit as st
import time
import math

# ============================================================
# MYBIO — DIGITAL WELLNESS TWIN
# Streamlit application
# ============================================================

st.set_page_config(
    page_title="MYBIO | Your Digital Wellness Twin",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# SESSION STATE
# ============================================================

defaults = {
    "page": "home",
    "profile_complete": False,
    "answers": {},
    "vata": 0,
    "pitta": 0,
    "kapha": 0,
    "prakriti": "",
    "streak": 7,
    "xp": 640,
    "water": 4,
    "steps": 6230,
    "sleep": 7.2,
    "completed_challenges": 3,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

:root {
    --forest: #173f35;
    --deep: #0b2923;
    --sage: #87a98d;
    --mint: #dcebdd;
    --cream: #f6f1e7;
    --gold: #c89b54;
    --terracotta: #b86f52;
    --text: #18332c;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(185, 211, 177, .35), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(220, 193, 143, .22), transparent 24%),
        linear-gradient(135deg, #f7f3e9 0%, #e9f0e4 50%, #f7f2e8 100%);
    color: var(--text);
}

/* Remove Streamlit top padding */
.block-container {
    padding-top: 1rem;
    padding-bottom: 5rem;
    max-width: 1450px;
}

/* =========================================================
   ANIMATIONS
   ========================================================= */

@keyframes float {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-15px) rotate(2deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}

@keyframes floatSlow {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-25px); }
    100% { transform: translateY(0px); }
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(135,169,141,.45); }
    70% { box-shadow: 0 0 0 20px rgba(135,169,141,0); }
    100% { box-shadow: 0 0 0 0 rgba(135,169,141,0); }
}

@keyframes glow {
    0% { opacity: .45; }
    50% { opacity: 1; }
    100% { opacity: .45; }
}

@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate {
    animation: appear .8s ease forwards;
}

.float {
    animation: float 5s ease-in-out infinite;
}

.float-slow {
    animation: floatSlow 7s ease-in-out infinite;
}


/* =========================================================
   HERO
   ========================================================= */

.hero {
    min-height: 570px;
    border-radius: 40px;
    padding: 65px;
    position: relative;
    overflow: hidden;

    background:
        radial-gradient(circle at 80% 20%, rgba(204,169,104,.35), transparent 20%),
        radial-gradient(circle at 15% 80%, rgba(110,151,123,.35), transparent 25%),
        linear-gradient(135deg, #123b32, #1e5043 50%, #315d4c);

    color: white;
    box-shadow: 0 30px 70px rgba(31,63,53,.25);
}

.hero:before {
    content: "";
    position: absolute;
    width: 350px;
    height: 350px;
    border-radius: 50%;
    right: -100px;
    top: -100px;
    background: rgba(220,194,143,.12);
    filter: blur(5px);
}

.hero:after {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    border-radius: 50%;
    left: -100px;
    bottom: -100px;
    background: rgba(155,190,160,.12);
}

.hero-content {
    position: relative;
    z-index: 5;
    max-width: 720px;
}

.logo {
    font-size: 22px;
    letter-spacing: 7px;
    font-weight: 700;
    color: #e7d3a8;
    margin-bottom: 30px;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(50px, 7vw, 90px);
    line-height: .95;
    margin: 0;
    letter-spacing: -3px;
}

.hero h2 {
    font-size: 23px;
    font-weight: 400;
    margin-top: 25px;
    color: #dceadd;
}

.hero-description {
    color: #c9d9d0;
    font-size: 17px;
    line-height: 1.8;
    margin-top: 25px;
}

.hero-orb {
    position: absolute;
    right: 8%;
    top: 20%;
    width: 280px;
    height: 280px;
    border-radius: 50%;

    background:
        radial-gradient(circle at 35% 30%, #e7d6ad, #9ab99c 40%, #416f5b 75%);

    box-shadow:
        inset -30px -35px 70px rgba(0,0,0,.22),
        0 30px 80px rgba(0,0,0,.25);

    animation: floatSlow 6s ease-in-out infinite;
}

.hero-orb:before {
    content: "🧬";
    position: absolute;
    font-size: 95px;
    left: 85px;
    top: 85px;
    filter: drop-shadow(0 8px 12px rgba(0,0,0,.2));
}


/* =========================================================
   SECTION HEADINGS
   ========================================================= */

.section-title {
    font-family: 'Playfair Display', serif;
    font-size: 38px;
    color: var(--forest);
    margin-top: 45px;
}

.section-subtitle {
    color: #64766d;
    font-size: 16px;
    margin-bottom: 25px;
}


/* =========================================================
   GLASS CARDS
   ========================================================= */

.glass-card {
    background: rgba(255,255,255,.55);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,.7);
    border-radius: 28px;
    padding: 28px;
    box-shadow: 0 15px 45px rgba(40,72,60,.10);
    transition: all .35s ease;
}

.glass-card:hover {
    transform: translateY(-7px);
    box-shadow: 0 25px 55px rgba(40,72,60,.17);
}

.metric-card {
    background: rgba(255,255,255,.7);
    border-radius: 25px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,.8);
    box-shadow: 0 12px 35px rgba(40,72,60,.10);
    transition: .3s;
}

.metric-card:hover {
    transform: translateY(-5px) scale(1.01);
}

.metric-icon {
    font-size: 30px;
}

.metric-number {
    font-size: 34px;
    font-weight: 700;
    color: var(--forest);
}

.metric-label {
    color: #718077;
    font-size: 14px;
}


/* =========================================================
   DOSHA CARDS
   ========================================================= */

.dosha-card {
    min-height: 210px;
    border-radius: 30px;
    padding: 30px;
    position: relative;
    overflow: hidden;
    transition: .35s;
}

.dosha-card:hover {
    transform: translateY(-10px) rotateX(3deg);
}

.vata {
    background: linear-gradient(145deg,#d9e8d8,#f1e8ce);
}

.pitta {
    background: linear-gradient(145deg,#f1dfbd,#eab99c);
}

.kapha {
    background: linear-gradient(145deg,#d5e4d6,#b9d2ca);
}

.dosha-symbol {
    font-size: 60px;
    animation: float 5s ease-in-out infinite;
}

.dosha-name {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    color: var(--forest);
}

.dosha-description {
    color: #53665d;
}


/* =========================================================
   PROGRESS
   ========================================================= */

.progress-container {
    width: 100%;
    height: 10px;
    background: #d8e0d9;
    border-radius: 20px;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    border-radius: 20px;
    background: linear-gradient(90deg,#315d4c,#c89b54);
}


/* =========================================================
   BADGES
   ========================================================= */

.badge {
    border-radius: 25px;
    padding: 22px;
    text-align: center;
    background: rgba(255,255,255,.65);
    border: 1px solid rgba(255,255,255,.8);
    transition: .3s;
}

.badge:hover {
    transform: translateY(-8px) rotate(2deg);
}

.badge-icon {
    font-size: 45px;
}

.badge-name {
    font-weight: 700;
    margin-top: 10px;
}

.badge-text {
    font-size: 13px;
    color: #718077;
}


/* =========================================================
   NAVIGATION
   ========================================================= */

.navbar {
    background: rgba(255,255,255,.6);
    backdrop-filter: blur(20px);
    border-radius: 22px;
    padding: 12px 18px;
    margin-bottom: 20px;
    border: 1px solid rgba(255,255,255,.8);
}


/* =========================================================
   STREAMLIT BUTTONS
   ========================================================= */

.stButton > button {
    border-radius: 15px !important;
    border: none !important;
    padding: 12px 24px !important;
    font-weight: 600 !important;
    background: linear-gradient(135deg,#214d40,#396956) !important;
    color: white !important;
    transition: all .3s ease !important;
    box-shadow: 0 8px 20px rgba(34,78,64,.18) !important;
}

.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 14px 28px rgba(34,78,64,.25) !important;
}


/* =========================================================
   INPUTS
   ========================================================= */

.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"],
.stMultiSelect div[data-baseweb="select"] {
    border-radius: 14px !important;
}

div[data-testid="stRadio"] label {
    padding: 8px 5px;
}


/* =========================================================
   QUESTION CARD
   ========================================================= */

.question-card {
    background: rgba(255,255,255,.62);
    border-radius: 25px;
    padding: 25px 30px;
    margin: 15px 0;
    border: 1px solid rgba(255,255,255,.8);
    box-shadow: 0 10px 35px rgba(38,70,57,.08);
}

.question-number {
    color: #b3884b;
    font-weight: 700;
    font-size: 14px;
    letter-spacing: 2px;
}

.question-text {
    font-family: 'Playfair Display', serif;
    color: #173f35;
    font-size: 23px;
    margin: 7px 0 15px;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    margin-top: 70px;
    padding: 35px;
    text-align: center;
    border-radius: 30px;
    background: #173f35;
    color: #dcebdd;
}

.footer-title {
    font-family: 'Playfair Display', serif;
    font-size: 27px;
}

.small {
    color: #7a8b82;
    font-size: 12px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVIGATION
# ============================================================

def navigation():

    st.markdown('<div class="navbar">', unsafe_allow_html=True)

    cols = st.columns(8)

    nav_items = [
        ("🌿", "Home"),
        ("📝", "Questionnaire"),
        ("🧬", "Body Twin"),
        ("🪷", "Prakriti"),
        ("🏆", "Challenges"),
        ("🔥", "Streak"),
        ("💡", "Recommendations"),
        ("ℹ️", "About"),
    ]

    for col, (icon, name) in zip(cols, nav_items):
        with col:
            if st.button(
                f"{icon} {name}",
                key=f"nav_{name}",
                use_container_width=True
            ):
                st.session_state.page = (
                    "home" if name == "Home"
                    else name.lower().replace(" ", "_")
                )
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# HOME PAGE
# ============================================================

def home():

    st.markdown("""
    <div class="hero animate">

        <div class="hero-content">

            <div class="logo">MYBIO • DIGITAL WELLNESS TWIN</div>

            <h1>Know your<br>body.</h1>

            <h2>Understand your biology. Build your balance.</h2>

            <p class="hero-description">
                MYBIO creates a personalized digital wellness twin using
                lifestyle information, body measurements, nutrition habits
                and an Ayurvedic Prakriti profile.
            </p>

        </div>

        <div class="hero-orb"></div>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Your body is a system.</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'MYBIO turns everyday health information into a simple, visual '
        'wellness profile.'
        '</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="glass-card float">
            <div style="font-size:45px;">🧬</div>
            <h3>Digital Twin</h3>
            <p>
            Build a dynamic representation of your current wellness profile
            from the information you provide.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="glass-card float-slow">
            <div style="font-size:45px;">🪷</div>
            <h3>Prakriti Insight</h3>
            <p>
            Explore Vata, Pitta and Kapha patterns using the questionnaire
            scoring system.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="glass-card float">
            <div style="font-size:45px;">✨</div>
            <h3>Daily Guidance</h3>
            <p>
            Receive lifestyle-focused suggestions based on your profile,
            habits and selected goals.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    metrics = [
        ("🧬", "Digital Twin", "Ready to build"),
        ("🪷", "Prakriti", "Personalized"),
        ("🔥", "Current streak", f"{st.session_state.streak} days"),
        ("⭐", "Wellness XP", str(st.session_state.xp)),
    ]

    for col, (icon, label, value) in zip([c1,c2,c3,c4], metrics):

        with col:

            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-icon">{icon}</div>
                    <div class="metric-number">{value}</div>
                    <div class="metric-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])

    with col1:
        st.markdown("""
        <div class="glass-card">
            <h2 style="font-family:'Playfair Display';">
            Ready to meet your digital twin?
            </h2>
            <p>
            Start with a short wellness questionnaire. Your answers will
            create the foundation of your MYBIO profile.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        if st.button("✨ Create My Twin", use_container_width=True):

            st.session_state.page = "questionnaire"
            st.rerun()


# ============================================================
# QUESTIONNAIRE
# ============================================================

def questionnaire():

    st.markdown(
        '<div class="section-title">TwinFit — Initial Questionnaire</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Tell MYBIO about your body, habits, lifestyle and Prakriti.'
        '</div>',
        unsafe_allow_html=True
    )

    # -------------------------------
    # SECTION 1
    # -------------------------------

    st.markdown("""
    <div class="glass-card">
    <h2>🌱 Section 1 — Basic Profile</h2>
    <p>Start with a few basic measurements.</p>
    </div>
    """, unsafe_allow_html=True)

    age = st.number_input(
        "1. What is your age?",
        min_value=10,
        max_value=100,
        value=20
    )

    sex = st.radio(
        "2. What is your sex?",
        ["Male", "Female", "Other"],
        horizontal=True
    )

    height = st.number_input(
        "3. Height (cm)",
        min_value=80.0,
        max_value=230.0,
        value=165.0
    )

    weight = st.number_input(
        "4. Current weight (kg)",
        min_value=20.0,
        max_value=250.0,
        value=60.0
    )

    goal = st.selectbox(
        "5. What is your goal?",
        [
            "Lose weight",
            "Maintain weight",
            "Improve fitness",
            "Reduce body fat",
            "Gain/maintain muscle",
            "Improve overall health"
        ]
    )

    activity = st.selectbox(
        "6. What is your usual activity level?",
        [
            "Sedentary",
            "Lightly active",
            "Moderately active",
            "Very active"
        ]
    )

    # -------------------------------
    # SECTION 2
    # -------------------------------

    st.markdown("""
    <div class="glass-card">
    <h2>🪷 Section 2 — Prakriti Questionnaire</h2>
    <p>
    Select the option that best represents your usual or natural pattern.
    </p>
    </div>
    """, unsafe_allow_html=True)

    prakriti_questions = [

        (
            7,
            "How would you describe your natural body build?",
            [
                "A — Thin/light frame, difficult to gain weight",
                "B — Medium build, relatively easy to maintain weight",
                "C — Larger/heavier build, tends to gain weight easily"
            ]
        ),

        (
            8,
            "How is your appetite usually?",
            [
                "A — Irregular; sometimes very hungry, sometimes not",
                "B — Strong and regular; I become hungry quickly",
                "C — Moderate/slow; I can go longer without food"
            ]
        ),

        (
            9,
            "How is your digestion?",
            [
                "A — Irregular/bloating is common",
                "B — Strong digestion; sometimes acidity/heartburn",
                "C — Slow digestion/heaviness after meals"
            ]
        ),

        (
            10,
            "How do you usually respond to weather?",
            [
                "A — I dislike cold/windy weather",
                "B — I dislike excessive heat",
                "C — I tolerate cold but dislike damp/heavy weather"
            ]
        ),

        (
            11,
            "How would you describe your energy?",
            [
                "A — Energetic in bursts but inconsistent",
                "B — Strong and focused",
                "C — Slow to start but good endurance"
            ]
        ),

        (
            12,
            "How is your sleep?",
            [
                "A — Light/irregular",
                "B — Moderate",
                "C — Deep/long; difficult to wake up sometimes"
            ]
        ),

        (
            13,
            "How would you describe your usual temperament?",
            [
                "A — Creative, restless, anxious, easily distracted",
                "B — Focused, ambitious, sometimes irritable",
                "C — Calm, patient, relaxed, sometimes lethargic"
            ]
        ),

        (
            14,
            "How do you generally gain/lose weight?",
            [
                "A — Difficult to gain weight",
                "B — Weight changes moderately",
                "C — Gain weight easily and lose it slowly"
            ]
        ),

        (
            15,
            "How regular is your daily routine?",
            [
                "A — Very irregular",
                "B — Fairly structured",
                "C — Generally regular but can be inactive"
            ]
        )
    ]

    scores = {
        "A": 0,
        "B": 0,
        "C": 0
    }

    for number, question, options in prakriti_questions:

        st.markdown(
            f"""
            <div class="question-card">
                <div class="question-number">
                    QUESTION {number}
                </div>
                <div class="question-text">
                    {question}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        answer = st.radio(
            "",
            options,
            key=f"q{number}",
            label_visibility="collapsed"
        )

        if answer.startswith("A"):
            scores["A"] += 1
        elif answer.startswith("B"):
            scores["B"] += 1
        else:
            scores["C"] += 1

    # -------------------------------
    # SECTION 3
    # -------------------------------

    st.markdown("""
    <div class="glass-card">
    <h2>🩺 Section 3 — Obesity / Health Profile</h2>
    <p>
    Health conditions are treated as safety constraints and should not be
    used by MYBIO to independently prescribe treatment.
    </p>
    </div>
    """, unsafe_allow_html=True)

    conditions = st.multiselect(
        "16. Have you been diagnosed with any of the following?",
        [
            "None",
            "Type 2 diabetes",
            "PCOS",
            "Hypothyroidism",
            "Cushing's syndrome",
            "Fatty liver",
            "Other endocrine/metabolic condition"
        ]
    )

    medications = st.radio(
        "17. Do you currently take medication that may affect weight or appetite?",
        ["No", "Yes"],
        horizontal=True
    )

    medication_info = ""

    if medications == "Yes":
        medication_info = st.text_input(
            "Enter medication / doctor-provided information"
        )

    allergies = st.multiselect(
        "18. Food allergies or intolerances",
        [
            "None",
            "Milk/dairy",
            "Nuts",
            "Gluten",
            "Eggs",
            "Seafood",
            "Other"
        ]
    )

    other_condition = st.radio(
        "19. Any other medical condition we should consider?",
        ["No", "Yes"],
        horizontal=True
    )

    other_condition_text = ""

    if other_condition == "Yes":
        other_condition_text = st.text_input(
            "Please describe"
        )

    # -------------------------------
    # SECTION 4
    # -------------------------------

    st.markdown("""
    <div class="glass-card">
    <h2>🥗 Section 4 — Food & Nutrition</h2>
    </div>
    """, unsafe_allow_html=True)

    diet = st.radio(
        "20. What is your diet preference?",
        ["Vegetarian", "Non-vegetarian", "Eggetarian"],
        horizontal=True
    )

    meals = st.selectbox(
        "21. How many meals do you normally eat?",
        ["1", "2", "3", "4+"]
    )

    junk = st.selectbox(
        "22. How often do you consume processed/junk food?",
        [
            "Rarely",
            "1–2 times/week",
            "3–5 times/week",
            "Daily"
        ]
    )

    sugary = st.selectbox(
        "23. How often do you consume sugary drinks?",
        [
            "Never/rarely",
            "Occasionally",
            "Frequently",
            "Daily"
        ]
    )

    # -------------------------------
    # SECTION 5
    # -------------------------------

    st.markdown("""
    <div class="glass-card">
    <h2>🌙 Section 5 — Lifestyle</h2>
    </div>
    """, unsafe_allow_html=True)

    sleep_duration = st.selectbox(
        "24. Average sleep duration?",
        ["<5 hours", "5–7 hours", "7–9 hours", ">9 hours"]
    )

    stress = st.radio(
        "25. How would you rate your stress?",
        ["1 — Low", "2 — Moderate", "3 — High"],
        horizontal=True
    )

    physical_activity = st.number_input(
        "26. How much physical activity do you get per day? (minutes)",
        min_value=0,
        max_value=600,
        value=30
    )

    sitting = st.selectbox(
        "27. How much time do you spend sitting/screen-based?",
        ["<2 hours", "2–6 hours", "6–8 hours", "8+ hours"]
    )

    meal_regular = st.selectbox(
        "28. How regular are your meal timings?",
        [
            "Very regular",
            "Mostly regular",
            "Sometimes irregular",
            "Very irregular"
        ]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(
        "✨ GENERATE MY DIGITAL TWIN",
        use_container_width=True
    ):

        # ------------------------------------------------
        # DOSHA SCORING
        # ------------------------------------------------

        vata = scores["A"]
        pitta = scores["B"]
        kapha = scores["C"]

        st.session_state.vata = vata
        st.session_state.pitta = pitta
        st.session_state.kapha = kapha

        score_list = [
            ("Vata", vata),
            ("Pitta", pitta),
            ("Kapha", kapha)
        ]

        score_list.sort(key=lambda x: x[1], reverse=True)

        highest = score_list[0][1]

        dominant = [
            name for name, score in score_list
            if score == highest
        ]

        if len(dominant) == 1:
            prakriti = dominant[0]
        elif len(dominant) == 2:
            prakriti = f"{dominant[0]}-{dominant[1]}"
        else:
            prakriti = "Vata-Pitta-Kapha"

        st.session_state.prakriti = prakriti

        # ------------------------------------------------
        # BMI
        # ------------------------------------------------

        bmi = weight / ((height / 100) ** 2)

        st.session_state.answers = {
            "age": age,
            "sex": sex,
            "height": height,
            "weight": weight,
            "goal": goal,
            "activity": activity,
            "conditions": conditions,
            "medications": medications,
            "medication_info": medication_info,
            "allergies": allergies,
            "diet": diet,
            "meals": meals,
            "junk": junk,
            "sugary": sugary,
            "sleep": sleep_duration,
            "stress": stress,
            "physical_activity": physical_activity,
            "sitting": sitting,
            "meal_regular": meal_regular,
            "bmi": bmi
        }

        st.session_state.profile_complete = True
        st.session_state.page = "body_twin"

        st.success("Your MYBIO digital twin has been created!")
        time.sleep(1)
        st.rerun()


# ============================================================
# BODY TWIN
# ============================================================

def body_twin():

    if not st.session_state.profile_complete:

        st.warning("Complete the questionnaire first.")

        if st.button("Go to Questionnaire"):
            st.session_state.page = "questionnaire"
            st.rerun()

        return

    data = st.session_state.answers

    bmi = data["bmi"]

    st.markdown(
        '<div class="section-title">🧬 Your Digital Body Twin</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'A visual snapshot of the information you provided.'
        '</div>',
        unsafe_allow_html=True
    )

    # -------------------------------
    # DIGITAL BODY
    # -------------------------------

    col1, col2 = st.columns([1, 1.5])

    with col1:

        st.markdown("""
        <div class="glass-card" style="text-align:center; min-height:500px;">

            <div style="
                font-size:170px;
                margin-top:40px;
                animation:floatSlow 5s ease-in-out infinite;
                filter:drop-shadow(0 20px 20px rgba(30,60,50,.18));
            ">
                🧘
            </div>

            <h2 style="font-family:'Playfair Display';">
                MYBIO Twin
            </h2>

            <p>
                Your wellness profile is ready.
            </p>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="glass-card">
            <h2 style="font-family:'Playfair Display';">
                Personal Profile
            </h2>
        """, unsafe_allow_html=True)

        m1, m2 = st.columns(2)

        with m1:
            st.metric("Age", f"{data['age']} yrs")
            st.metric("Height", f"{data['height']:.0f} cm")
            st.metric("Weight", f"{data['weight']:.1f} kg")

        with m2:
            st.metric("BMI", f"{bmi:.1f}")
            st.metric("Activity", data["activity"])
            st.metric("Goal", data["goal"])

        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------
    # BODY METRICS
    # -------------------------------

    st.markdown(
        '<div class="section-title">Body Metrics</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    cards = [
        ("⚖️", f"{bmi:.1f}", "BMI"),
        ("💧", f"{st.session_state.water}/8", "Water glasses"),
        ("🚶", f"{st.session_state.steps:,}", "Steps"),
        ("🌙", f"{st.session_state.sleep}", "Sleep hours"),
    ]

    for col, (icon, value, label) in zip(
        [c1,c2,c3,c4],
        cards
    ):

        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-icon">{icon}</div>
                    <div class="metric-number">{value}</div>
                    <div class="metric-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    # -------------------------------
    # DOSHA SNAPSHOT
    # -------------------------------

    st.markdown(
        '<div class="section-title">Prakriti Snapshot</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)

    doshas = [
        ("🌬️", "Vata", st.session_state.vata, "vata"),
        ("🔥", "Pitta", st.session_state.pitta, "pitta"),
        ("🌊", "Kapha", st.session_state.kapha, "kapha")
    ]

    for col, (symbol, name, score, css) in zip(
        [c1,c2,c3],
        doshas
    ):

        with col:

            percentage = score / 9 * 100

            st.markdown(
                f"""
                <div class="dosha-card {css}">

                    <div class="dosha-symbol">{symbol}</div>

                    <div class="dosha-name">
                        {name}
                    </div>

                    <p>{score}/9 responses</p>

                    <div class="progress-container">
                        <div
                            class="progress-fill"
                            style="width:{percentage}%"
                        ></div>
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# PRAKRITI PAGE
# ============================================================

def prakriti_page():

    st.markdown(
        '<div class="section-title">🪷 Your Ayurvedic Body Type</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.profile_complete:

        st.info(
            "Complete the questionnaire to discover your Prakriti profile."
        )

        return

    prakriti = st.session_state.prakriti

    st.markdown(
        f"""
        <div class="hero" style="min-height:320px;padding:45px;">

            <div class="hero-content">

                <div class="logo">YOUR PRAKRITI</div>

                <h1 style="font-size:65px;">
                    {prakriti}
                </h1>

                <h2>
                    Your dominant constitutional pattern
                </h2>

            </div>

            <div class="hero-orb" style="
                width:180px;
                height:180px;
                right:12%;
                top:22%;
            "></div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">The Three Doshas</div>',
        unsafe_allow_html=True
    )

    descriptions = {

        "Vata":
            "Associated traditionally with movement, creativity, variability and lightness.",

        "Pitta":
            "Associated traditionally with transformation, intensity, focus and metabolic activity.",

        "Kapha":
            "Associated traditionally with stability, endurance, calmness and structure."
    }

    c1, c2, c3 = st.columns(3)

    for col, (symbol, name, css) in zip(
        [c1,c2,c3],
        [
            ("🌬️","Vata","vata"),
            ("🔥","Pitta","pitta"),
            ("🌊","Kapha","kapha")
        ]
    ):

        with col:

            st.markdown(
                f"""
                <div class="dosha-card {css}">

                    <div class="dosha-symbol">
                        {symbol}
                    </div>

                    <div class="dosha-name">
                        {name}
                    </div>

                    <div class="dosha-description">
                        {descriptions[name]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<br>", unsafe_allow_html=True)

    st.warning(
        "Prakriti is presented here as a traditional wellness framework "
        "and should not be treated as a medical diagnosis."
    )


# ============================================================
# CHALLENGES
# ============================================================

def challenges():

    st.markdown(
        '<div class="section-title">🏆 Challenges & Rewards</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Small actions. Consistent habits. Real progress.'
        '</div>',
        unsafe_allow_html=True
    )

    challenges_list = [

        ("💧", "Hydration Hero", "Drink 8 glasses of water", 50),

        ("🚶", "Movement Mission", "Complete 7,000 steps", 75),

        ("🥗", "Mindful Plate", "Choose one balanced meal", 60),

        ("🌙", "Sleep Guardian", "Maintain your sleep target", 80),

        ("🧘", "Mindful Minute", "Practice 10 minutes of relaxation", 40),

        ("📵", "Screen Break", "Take three screen breaks today", 50),
    ]

    for icon, title, description, xp in challenges_list:

        col1, col2, col3 = st.columns([1,4,1])

        with col1:
            st.markdown(
                f"""
                <div style="
                font-size:55px;
                text-align:center;
                animation:float 5s ease-in-out infinite;">
                {icon}
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:

            st.markdown(
                f"""
                <div class="glass-card">

                    <h3>{title}</h3>

                    <p>{description}</p>

                    <div class="small">
                        Reward: +{xp} XP
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        with col3:

            if st.button(
                "Complete",
                key=f"challenge_{title}"
            ):

                st.session_state.xp += xp
                st.session_state.completed_challenges += 1

                st.success("+XP")

                time.sleep(.5)
                st.rerun()

    st.markdown(
        '<div class="section-title">🎖️ Your Badges</div>',
        unsafe_allow_html=True
    )

    badges = [
        ("🌱", "First Step", "Started your MYBIO journey"),
        ("🔥", "7 Day Spark", "Maintained a 7-day streak"),
        ("💧", "Hydration Hero", "Completed hydration goal"),
        ("🧬", "Twin Creator", "Created your digital twin"),
        ("🪷", "Prakriti Explorer", "Completed Prakriti profile"),
    ]

    cols = st.columns(5)

    for col, (icon, name, description) in zip(cols, badges):

        with col:

            st.markdown(
                f"""
                <div class="badge">

                    <div class="badge-icon">
                        {icon}
                    </div>

                    <div class="badge-name">
                        {name}
                    </div>

                    <div class="badge-text">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# STREAK
# ============================================================

def streak():

    st.markdown(
        '<div class="section-title">🔥 Your Wellness Streak</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="hero" style="min-height:400px;text-align:center;">

            <div style="position:relative;z-index:5;">

                <div style="font-size:80px;animation:pulse 2s infinite;">
                    🔥
                </div>

                <div style="
                    font-family:'Playfair Display';
                    font-size:90px;
                    margin-top:10px;">
                    {st.session_state.streak}
                </div>

                <div style="
                    font-size:23px;
                    color:#dceadd;">
                    DAY STREAK
                </div>

                <p style="
                    color:#bcd0c5;
                    margin-top:20px;">
                    Consistency is the foundation of your digital twin.
                </p>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Weekly Rhythm</div>',
        unsafe_allow_html=True
    )

    days = ["M","T","W","T","F","S","S"]

    cols = st.columns(7)

    for i, (col, day) in enumerate(zip(cols, days)):

        with col:

            completed = i < 6

            st.markdown(
                f"""
                <div class="glass-card"
                style="text-align:center;">

                    <div style="
                    font-weight:700;
                    color:#173f35;">
                    {day}
                    </div>

                    <div style="
                    font-size:40px;
                    margin-top:10px;">
                    {"🔥" if completed else "○"}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# RECOMMENDATIONS
# ============================================================

def recommendations():

    st.markdown(
        '<div class="section-title">💡 Personalized Recommendations</div>',
        unsafe_allow_html=True
    )

    if not st.session_state.profile_complete:

        st.info(
            "Complete your questionnaire to unlock personalized guidance."
        )

        return

    data = st.session_state.answers

    recommendations_list = []

    # Sleep
    if data["sleep"] in ["<5 hours", "5–7 hours"]:
        recommendations_list.append(
            (
                "🌙",
                "Protect your sleep",
                "Your selected sleep range suggests that improving sleep "
                "duration may be a useful wellness priority."
            )
        )

    # Activity
    if data["physical_activity"] < 30:
        recommendations_list.append(
            (
                "🚶",
                "Add gentle movement",
                "Consider gradually increasing daily physical activity "
                "according to your comfort and fitness level."
            )
        )

    # Junk food
    if data["junk"] in ["3–5 times/week", "Daily"]:
        recommendations_list.append(
            (
                "🥗",
                "Build a balanced plate",
                "Try replacing some highly processed foods with meals "
                "containing vegetables, protein and whole-food carbohydrates."
            )
        )

    # Sugary drinks
    if data["sugary"] in ["Frequently", "Daily"]:
        recommendations_list.append(
            (
                "🥤",
                "Reduce sugary drinks",
                "Gradually replacing sugary beverages with water or "
                "unsweetened options can support healthier daily habits."
            )
        )

    # Meal timing
    if data["meal_regular"] in [
        "Sometimes irregular",
        "Very irregular"
    ]:
        recommendations_list.append(
            (
                "⏰",
                "Create meal consistency",
                "A more consistent meal routine may make daily eating "
                "patterns easier to manage."
            )
        )

    # Default
    if not recommendations_list:

        recommendations_list.append(
            (
                "✨",
                "Keep building consistency",
                "Your current answers do not highlight a major lifestyle "
                "priority. Continue maintaining your healthy habits."
            )
        )

    for icon, title, text in recommendations_list:

        st.markdown(
            f"""
            <div class="glass-card">

                <div style="
                font-size:50px;
                float:left;
                margin-right:20px;">
                {icon}
                </div>

                <h3>{title}</h3>

                <p>{text}</p>

            </div>

            <br>
            """,
            unsafe_allow_html=True
        )

    st.warning(
        "MYBIO provides general wellness information only. It does not "
        "diagnose disease, prescribe medication or replace professional "
        "medical/dietetic advice. Medical conditions and medications should "
        "be reviewed with a qualified healthcare professional."
    )


# ============================================================
# ABOUT
# ============================================================

def about():

    st.markdown(
        '<div class="section-title">🌿 About MYBIO</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="glass-card">

    <h2 style="font-family:'Playfair Display';">
    MYBIO — Digital Wellness Twin
    </h2>

    <p>
    MYBIO is a digital wellness prototype designed to explore how
    personal health information can be transformed into an interactive
    digital representation of an individual's wellness profile.
    </p>

    <p>
    The platform combines basic body measurements, lifestyle information,
    nutrition habits and a traditional Ayurvedic Prakriti questionnaire
    to generate a visualized wellness profile.
    </p>

    <p>
    The objective is not to replace clinical assessment. Instead, MYBIO
    demonstrates how data-driven interfaces can make personal wellness
    information easier to understand, monitor and interact with.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">⚙️ Technology Concept</div>',
        unsafe_allow_html=True
    )

    c1, c2, c3, c4 = st.columns(4)

    technologies = [
        ("🐍", "Python", "Application logic"),
        ("🎈", "Streamlit", "Interactive interface"),
        ("🧠", "AI / ML", "Future personalization"),
        ("🧬", "Bioinformatics", "Biological context"),
    ]

    for col, (icon, title, desc) in zip(
        [c1,c2,c3,c4],
        technologies
    ):

        with col:

            st.markdown(
                f"""
                <div class="metric-card">

                    <div class="metric-icon">
                    {icon}
                    </div>

                    <h3>{title}</h3>

                    <div class="metric-label">
                    {desc}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# FOOTER
# ============================================================

def footer():

    st.markdown("""
    <div class="footer">

        <div class="footer-title">
            MYBIO
        </div>

        <p>
            Your body. Your data. Your digital twin.
        </p>

        <div class="small">
            Digital wellness prototype • Built with Python & Streamlit
        </div>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# APP ROUTER
# ============================================================

navigation()

page = st.session_state.page

if page == "home":
    home()

elif page == "questionnaire":
    questionnaire()

elif page == "body_twin":
    body_twin()

elif page == "prakriti":
    prakriti_page()

elif page == "challenges":
    challenges()

elif page == "streak":
    streak()

elif page == "recommendations":
    recommendations()

elif page == "about":
    about()

else:
    home()

footer()
