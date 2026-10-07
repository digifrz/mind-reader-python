import streamlit as st

# -----------------------------
# PAGE SETUP
# -----------------------------

st.set_page_config(
    page_title="Mind Reader 2.0",
    page_icon="🧠"
)

# -----------------------------
# SESSION STATE
# -----------------------------

if "mode" not in st.session_state:
    st.session_state.mode = "menu"

if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False

if "number_result" not in st.session_state:
    st.session_state.number_result = None

if "math_done" not in st.session_state:
    st.session_state.math_done = False


# -----------------------------
# TITLE
# -----------------------------

st.title("🧠 Mind Reader 2.0")
st.write("### Can I really read your mind?")
st.write("---")


# -----------------------------
# MAIN MENU
# -----------------------------

if st.session_state.mode == "menu":

    st.subheader("🎮 Choose a Mind-Reading Trick")

    if st.button("🔮 Guaranteed Prediction", use_container_width=True):
        st.session_state.mode = "prediction"
        st.rerun()

    if st.button("🔢 Number Mind Reader", use_container_width=True):
        st.session_state.mode = "number"
        st.rerun()

    if st.button("🎩 Mathematical Magic", use_container_width=True):
        st.session_state.mode = "magic"
        st.rerun()

    if st.button("🕵️ Secret Challenge", use_container_width=True):
        st.session_state.mode = "challenge"
        st.rerun()

    if st.button("🧠 Reveal the Secret", use_container_width=True):
        st.session_state.mode = "secret"
        st.rerun()


# ==================================================
# 1. GUARANTEED PREDICTION
# ==================================================

elif st.session_state.mode == "prediction":

    st.header("🔮 Guaranteed Prediction")

    st.write(
        "Think of any number in your mind. "
        "Don't tell me what it is!"
    )

    st.write("Now follow these steps:")

    st.write("1️⃣ Multiply your number by **2**")
    st.write("2️⃣ Add **10**")
    st.write("3️⃣ Divide the result by **2**")
    st.write("4️⃣ Subtract your original number")

    st.write("---")

    if st.button("🧠 Read My Mind", use_container_width=True):

        st.session_state.prediction_done = True

    if st.session_state.prediction_done:

        st.success("🔮 I can see the answer!")

        st.subheader("✨ Your final number is...")

        st.title("5")

        st.write(
            "😱 No matter what number you started with, "
            "the answer is always 5!"
        )

    if st.button("⬅️ Back to Menu"):
        st.session_state.mode = "menu"
        st.session_state.prediction_done = False
        st.rerun()


# ==================================================
# 2. NUMBER MIND READER
# ==================================================

elif st.session_state.mode == "number":

    st.header("🔢 Number Mind Reader")

    st.write(
        "Think of a whole number between **1 and 31**."
    )

    st.write(
        "I will show you five cards. "
        "Tell me whether your number appears on each card."
    )

    cards = [
        [1, 3, 5, 7, 9, 11, 13, 15,
         17, 19, 21, 23, 25, 27, 29, 31],

        [2, 3, 6, 7, 10, 11, 14, 15,
         18, 19, 22, 23, 26, 27, 30, 31],

        [4, 5, 6, 7, 12, 13, 14, 15,
         20, 21, 22, 23, 28, 29, 30, 31],

        [8, 9, 10, 11, 12, 13, 14, 15,
         24, 25, 26, 27, 28, 29, 30, 31],

        [16, 17, 18, 19, 20, 21, 22, 23,
         24, 25, 26, 27, 28, 29, 30, 31]
    ]

    values = [1, 2, 4, 8, 16]

    answers = []

    for i in range(5):

        st.write("---")

        st.subheader(f"🃏 Card {i + 1}")

        st.write(
            " ".join(str(number) for number in cards[i])
        )

        answer = st.radio(
            f"Is your number on Card {i + 1}?",
            ["Yes", "No"],
            key=f"card_{i}"
        )

        answers.append(answer)

    if st.button("🧠 Reveal My Number", use_container_width=True):

        result = 0

        for i in range(5):

            if answers[i] == "Yes":
                result += values[i]

        if result == 0:

            st.error(
                "Please make sure you selected the correct "
                "answers for your number."
            )

        else:

            st.session_state.number_result = result

    if st.session_state.number_result is not None:

        st.success("🔮 I have read your mind!")

        st.subheader("You were thinking of...")

        st.title(
            str(st.session_state.number_result)
        )

    if st.button("⬅️ Back to Menu"):

        st.session_state.mode = "menu"
        st.session_state.number_result = None

        st.rerun()


# ==================================================
# 3. MATHEMATICAL MAGIC
# ==================================================

elif st.session_state.mode == "magic":

    st.header("🎩 Mathematical Magic")

    st.write(
        "Let's try another mysterious mathematical trick!"
    )

    st.write("Think of any number.")

    st.write("1️⃣ Multiply it by **2**")
    st.write("2️⃣ Add **8**")
    st.write("3️⃣ Divide by **2**")
    st.write("4️⃣ Subtract your original number")

    st.write("---")

    if st.button("✨ Perform Magic", use_container_width=True):

        st.session_state.math_done = True

    if st.session_state.math_done:

        st.success("🎩 Magic complete!")

        st.subheader("Your answer is...")

        st.title("4")

        st.write(
            "The original number disappears from the equation!"
        )

        st.write("---")

        st.subheader("🔢 Bonus Digit-Sum Trick")

        st.write(
            "Take any two-digit number and subtract "
            "the sum of its digits from it."
        )

        st.write(
            "The result will always be divisible by 9."
        )

        st.info(
            "For example: 54 → 5 + 4 = 9 → "
            "54 - 9 = 45"
        )

    if st.button("⬅️ Back to Menu"):

        st.session_state.mode = "menu"
        st.session_state.math_done = False

        st.rerun()


# ==================================================
# 4. SECRET CHALLENGE
# ==================================================

elif st.session_state.mode == "challenge":

    st.header("🕵️ Secret Challenge")

    st.write(
        "You've seen the first trick."
    )

    st.write(
        "Now let's see if you can discover "
        "how the mind reading actually works."
    )

    answer = st.radio(
        "Why does the Guaranteed Prediction always work?",
        [
            "The computer randomly guesses the answer",
            "The mathematics cancels out the original number",
            "The computer can actually read minds",
            "The answer changes every time"
        ]
    )

    if st.button("🔍 Check Answer", use_container_width=True):

        if answer == "The mathematics cancels out the original number":

            st.success("🎉 Correct!")

            st.write(
                "You're beginning to discover the secret "
                "behind the trick."
            )

        else:

            st.error("❌ Not quite!")

            st.info(
                "💡 Think about what happens when the "
                "original number is subtracted."
            )

    if st.button("⬅️ Back to Menu"):

        st.session_state.mode = "menu"
        st.rerun()


# ==================================================
# 5. REVEAL THE SECRET
# ==================================================

elif st.session_state.mode == "secret":

    st.header("🧠 Reveal the Secret")

    st.write(
        "The first trick isn't actually supernatural."
    )

    st.write("Suppose your original number is **X**.")

    st.write("### Step 1")

    st.code("X × 2 = 2X")

    st.write("### Step 2")

    st.code("2X + 10")

    st.write("### Step 3")

    st.code("(2X + 10) ÷ 2 = X + 5")

    st.write("### Step 4")

    st.code("(X + 5) - X = 5")

    st.success(
        "🎯 The X disappears, leaving 5!"
    )

    st.write("---")

    st.subheader("🔢 Why the Number Mind Reader works")

    st.write(
        "The cards represent powers of 2:"
    )

    st.code("1 + 2 + 4 + 8 + 16")

    st.write(
        "Every number from 1 to 31 can be represented "
        "as a combination of these values."
    )

    st.write(
        "When you say YES to a card, the program adds "
        "that card's value to reconstruct your number."
    )

    st.success(
        "🧠 So the computer isn't actually reading your mind — "
        "it's using mathematics!"
    )

    if st.button("⬅️ Back to Menu"):

        st.session_state.mode = "menu"
        st.rerun()


# -----------------------------
# FOOTER
# -----------------------------

st.write("---")
st.caption("🧠 Mind Reader 2.0 • Built with Python + Streamlit")
