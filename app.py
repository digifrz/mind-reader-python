import streamlit as st

st.set_page_config(
    page_title="Escape Room",
    page_icon="🔐",
    layout="centered"
)

# -------------------------
# GAME STATE
# -------------------------

if "room" not in st.session_state:
    st.session_state.room = 1

if "attempts" not in st.session_state:
    st.session_state.attempts = 0


# -------------------------
# TITLE
# -------------------------

st.title("🔐 ESCAPE ROOM")
st.subheader("THE LOCKED CLASSROOM")

st.write(
    "After school, you find yourself trapped inside a locked classroom."
)

st.write(
    "A clock, a mysterious note, a locked box, and a painting "
    "may hold the key."
)

st.divider()


# -------------------------
# PROGRESS
# -------------------------

st.progress(
    min(st.session_state.room / 3, 1.0),
    text=f"Room {min(st.session_state.room, 3)} of 3"
)


# -------------------------
# ROOM 1
# -------------------------

if st.session_state.room == 1:

    st.header("🕰️ ROOM 1 — THE CLOCK")

    st.write(
        "The clock is stopped at **7:25**."
    )

    st.write(
        "Enter the time as four digits **(HHMM)**."
    )

    guess = st.text_input(
        "Clock code:",
        max_chars=4
    )

    if st.button("🔓 Unlock Clock"):

        st.session_state.attempts += 1

        if guess.strip() == "0725":

            st.success("✅ Correct! The clock unlocks.")

            if st.button("➡️ Enter Room 2"):
                st.session_state.room = 2
                st.rerun()

        else:

            st.error("❌ Not quite.")

            st.info(
                "💡 Hint: Use a leading zero for the hour."
            )


# -------------------------
# ROOM 2
# -------------------------

elif st.session_state.room == 2:

    st.header("📜 ROOM 2 — THE MYSTERIOUS NOTE")

    st.write("You discover a strange encoded message:")

    st.code(
        "WKH ERA FRGH LV WKH FORFN'V KRXU SOXV WKH\n"
        "QXPEHU RI OHWWHUV LQ 'FODVVURRP'."
    )

    st.write(
        "The message was encoded by shifting each letter "
        "**forward three places**."
    )

    st.write(
        "Decode the message and discover the two-digit "
        "combination for the box."
    )

    with st.expander("🧩 Need a hint?"):

        st.write("The clock hour is **7**.")
        st.write("CLASSROOM has **9 letters**.")
        st.write("Add them together.")

    guess = st.text_input(
        "Box combination:",
        max_chars=2
    )

    if st.button("🔓 Unlock Box"):

        st.session_state.attempts += 1

        if guess.strip() == "16":

            st.success("✅ Correct! The box clicks open!")

            st.write("📦 Inside the box you find a note:")

            st.warning(
                "The painting holds the door code."
            )

            if st.button("➡️ Enter Final Room"):
                st.session_state.room = 3
                st.rerun()

        else:

            st.error("❌ Not quite.")

            st.info(
                "💡 Hint: 7 + 9 = ?"
            )


# -------------------------
# FINAL ROOM
# -------------------------

elif st.session_state.room == 3:

    st.header("🚪 FINAL ROOM — THE DOOR")

    st.write(
        "The painting shows:"
    )

    st.write("""
    🧱 **4 walls**

    🪑 **8 desks**

    🪟 **2 windows**

    🪑 **6 chairs**
    """)

    st.write(
        "Put those numbers together in the same order "
        "to create the four-digit door code."
    )

    guess = st.text_input(
        "🔐 Door code:",
        max_chars=4
    )

    if st.button("🚪 Escape!"):

        st.session_state.attempts += 1

        if guess.strip() == "4826":

            st.balloons()

            st.success(
                "🎉 ESCAPE SUCCESSFUL!"
            )

            st.write(
                "You unlocked the classroom door!"
            )

            st.write(
                f"🏆 Total attempts: {st.session_state.attempts}"
            )

            st.success(
                "🕵️ Detective Rating: ⭐⭐⭐⭐⭐"
            )

            if st.button("🔄 Play Again"):

                st.session_state.room = 1
                st.session_state.attempts = 0
                st.rerun()

        else:

            st.error(
                "❌ The door remains locked."
            )

            st.info(
                "💡 Hint: Put 4, 8, 2 and 6 together."
            )


# -------------------------
# SIDEBAR
# -------------------------

with st.sidebar:

    st.header("🕵️ Detective Panel")

    st.write(
        "Solve each puzzle to escape!"
    )

    st.metric(
        "Current Room",
        f"{min(st.session_state.room, 3)}/3"
    )

    st.metric(
        "Attempts",
        st.session_state.attempts
    )

    st.divider()

    st.write(
        "🔐 Escape Room: The Locked Classroom"
    )
