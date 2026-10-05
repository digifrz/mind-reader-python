import streamlit as st
import time

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Mind Reader 2.0",
    page_icon="🧠",
    layout="centered"
)

# ============================================================
# CUSTOM DESIGN
# ============================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at top,
            #25254a 0%,
            #10101c 45%,
            #050509 100%
        );
    color: white;
}

.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: 900;
    letter-spacing: 3px;
    margin-top: 10px;
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    color: #b8b8c8;
    font-size: 18px;
    margin-bottom: 35px;
}

.card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 20px;
    padding: 28px;
    margin: 18px 0;
}

.mode-title {
    font-size: 25px;
    font-weight: 800;
    margin-bottom: 12px;
}

.big-result {
    text-align: center;
    font-size: 64px;
    font-weight: 900;
    padding: 20px;
}

.center {
    text-align: center;
}

.small-text {
    color: #bdbdcc;
    font-size: 15px;
}

.footer {
    text-align: center;
    color: #77778a;
    font-size: 13px;
    margin-top: 50px;
    padding-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🧠 MIND READER 2.0</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Mathematical Tricks That Feel Like Magic</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🧠 Mind Reader")

st.sidebar.markdown(
    "Choose your experience:"
)

mode = st.sidebar.radio(
    "Select Mode",
    [
        "🔮 Guaranteed Prediction",
        "🎴 Number Prediction",
        "🧩 Mathematical Magic",
        "🕵️ Secret Challenge",
        "📖 Reveal the Secret"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "This project uses mathematics and Python "
    "to create mind-reading illusions."
)


# ============================================================
# MODE 1 — GUARANTEED PREDICTION
# ============================================================

if mode == "🔮 Guaranteed Prediction":

    st.markdown("""
    <div class="card">

    <div class="mode-title">
    🔮 MODE 1 — GUARANTEED PREDICTION
    </div>

    <p>
    Think of <b>any number</b>.
    Keep it secret.
    </p>

    <p>Then follow these steps:</p>

    <ol>
        <li>Multiply your number by <b>2</b>.</li>
        <li>Add <b>10</b>.</li>
        <li>Divide the result by <b>2</b>.</li>
        <li>Subtract your original number.</li>
    </ol>

    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "🔮 Reveal My Prediction",
        use_container_width=True
    ):

        with st.spinner("Reading your mathematical thoughts..."):
            time.sleep(1.5)

        st.markdown("""
        <div class="card">

        <div class="center">
        <div class="small-text">
        🧠 MY PREDICTION
        </div>

        <div class="big-result">
        5
        </div>

        <div class="small-text">
        Your final answer is always 5!
        </div>
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.success(
            "The secret isn't mind reading. It's mathematics! 🧠✨"
        )

        with st.expander("🧮 Reveal the mathematics"):

            st.write(
                "Let your original number be x."
            )

            st.latex(
                r"\frac{2x + 10}{2} - x = x + 5 - x = 5"
            )

            st.write(
                "The x cancels out, leaving 5."
            )


# ============================================================
# MODE 2 — NUMBER PREDICTION
# ============================================================

elif mode == "🎴 Number Prediction":

    st.markdown("""
    <div class="card">

    <div class="mode-title">
    🎴 MODE 2 — NUMBER PREDICTION
    </div>

    <p>
    Choose a whole number from <b>1 to 31</b>.
    </p>

    <p>
    Don't tell me your number.
    I'll try to reconstruct it from your answers.
    🤫
    </p>

    </div>
    """, unsafe_allow_html=True)

    selected_cards = []

    for bit in range(5):

        value = 1 << bit

        numbers = [
            number
            for number in range(1, 32)
            if number & value
        ]

        selected = st.checkbox(
            f"🎴 Card {value} — My number is on this card",
            key=f"card_{value}"
        )

        if selected:
            selected_cards.append(value)

        with st.expander(f"View Card {value}"):

            st.write(
                ", ".join(map(str, numbers))
            )

    if st.button(
        "🧠 Predict My Number",
        use_container_width=True
    ):

        prediction = sum(selected_cards)

        if 1 <= prediction <= 31:

            st.markdown("""
            <div class="card">

            <div class="center">

            <div class="small-text">
            🔮 I PREDICT YOUR NUMBER IS
            </div>

            <div class="big-result">
            """ + str(prediction) + """
            </div>

            </div>

            </div>
            """, unsafe_allow_html=True)

            st.success(
                "The prediction is based on binary numbers! 🎯"
            )

            with st.expander("🧮 How did this work?"):

                st.write(
                    "Each card represents a power of 2:"
                )

                st.write(
                    "1, 2, 4, 8 and 16."
                )

                st.write(
                    "Adding the values of the cards containing "
                    "your number reconstructs the original number."
                )

                st.latex(
                    r"Number = 1b_1 + 2b_2 + 4b_3 + 8b_4 + 16b_5"
                )

        else:

            st.warning(
                "Please select the cards containing your secret number."
            )


# ============================================================
# MODE 3 — MATHEMATICAL MAGIC
# ============================================================

elif mode == "🧩 Mathematical Magic":

    st.markdown("""
    <div class="card">

    <div class="mode-title">
    🧩 MODE 3 — MATHEMATICAL MAGIC
    </div>

    <p>
    Choose one of the mathematical tricks.
    </p>

    </div>
    """, unsafe_allow_html=True)

    trick = st.selectbox(
        "Choose a trick",
        [
            "Answer is always 4",
            "Digit sum becomes 9"
        ]
    )

    if trick == "Answer is always 4":

        st.markdown("""
        <div class="card">

        Think of any number.

        <br><br>

        1️⃣ Multiply it by 3.

        <br>

        2️⃣ Add 12.

        <br>

        3️⃣ Divide by 3.

        <br>

        4️⃣ Subtract your original number.

        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "✨ Reveal the Answer",
            use_container_width=True
        ):

            st.markdown(
                '<div class="big-result">4</div>',
                unsafe_allow_html=True
            )

            with st.expander("🧮 Mathematical explanation"):

                st.latex(
                    r"\frac{3x + 12}{3} - x = x + 4 - x = 4"
                )

    else:

        st.markdown("""
        <div class="card">

        Choose a whole number from <b>1 to 9</b>.

        <br><br>

        Multiply it by 9.

        <br>

        Then add the digits of your result.
        </div>
        """, unsafe_allow_html=True)

        number = st.number_input(
            "Choose your secret number",
            min_value=1,
            max_value=9,
            value=7,
            step=1
        )

        if st.button(
            "✨ Perform the Magic",
            use_container_width=True
        ):

            result = number * 9

            digit_sum = sum(
                int(digit)
                for digit in str(result)
            )

            st.markdown(
                f'<div class="big-result">{digit_sum}</div>',
                unsafe_allow_html=True
            )

            st.info(
                f"{number} × 9 = {result} → "
                f"digit sum = {digit_sum}"
            )


# ============================================================
# MODE 4 — SECRET CHALLENGE
# ============================================================

elif mode == "🕵️ Secret Challenge":

    st.markdown("""
    <div class="card">

    <div class="mode-title">
    🕵️ MODE 4 — SECRET CHALLENGE
    </div>

    <p>
    Challenge your classmates!
    </p>

    <p>
    Give them this sequence:
    </p>

    <ol>
        <li>Think of any number.</li>
        <li>Multiply it by 2.</li>
        <li>Add 10.</li>
        <li>Divide by 2.</li>
        <li>Subtract the original number.</li>
    </ol>

    <p>
    Now ask them:
    </p>

    <h3>
    🤔 What will the answer be?
    </h3>

    </div>
    """, unsafe_allow_html=True)

    guess = st.number_input(
        "What do you think the answer will be?",
        value=0,
        step=1
    )

    if st.button(
        "🎯 Check My Guess",
        use_container_width=True
    ):

        if guess == 5:
            st.success(
                "Correct! 🎉 You solved the mathematical illusion."
            )
        else:
            st.error(
                "Not quite! Try thinking algebraically."
            )

    with st.expander("💡 Give me a hint"):

        st.write(
            "Call your starting number x."
        )

        st.write(
            "Track what happens to x after every step."
        )


# ============================================================
# MODE 5 — REVEAL THE SECRET
# ============================================================

elif mode == "📖 Reveal the Secret":

    st.markdown("""
    <div class="card">

    <div class="mode-title">
    📖 MODE 5 — REVEAL THE SECRET
    </div>

    <p>
    The tricks feel like mind reading,
    but they are actually based on mathematics.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.subheader("🔮 Guaranteed Prediction")

    st.latex(
        r"\frac{2x + 10}{2} - x = x + 5 - x = 5"
    )

    st.write(
        "The unknown number x cancels itself."
    )

    st.subheader("🧩 Mathematical Magic — Answer 4")

    st.latex(
        r"\frac{3x + 12}{3} - x = x + 4 - x = 4"
    )

    st.subheader("🎯 Mathematical Magic — Answer 9")

    st.write(
        "Multiples of 9 have a special digit-sum property."
    )

    st.write(
        "For example:"
    )

    st.latex(
        r"9 \times 7 = 63"
    )

    st.latex(
        r"6 + 3 = 9"
    )

    st.subheader("🎴 Number Prediction")

    st.write(
        "The cards represent powers of 2:"
    )

    st.code(
        "1, 2, 4, 8, 16"
    )

    st.write(
        "These are the place values used in binary representation."
    )

    st.info(
        "There is no real mind reading involved. "
        "The magic comes from patterns in mathematics."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

🧠 Mind Reader 2.0
<br>
A Python Mathematical Illusion Project

</div>
""", unsafe_allow_html=True)