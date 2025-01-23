import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

if "is_passcode_valid" not in st.session_state:
    st.session_state.is_passcode_valid = False

_PASSCODE = os.getenv("PASSCODE")

st.logo("assets/logo.svg", size="large")


@st.dialog("Passcode")
def passcode_dialog():

    entered_passcode = st.text_input("Passcode", label_visibility="collapsed")
    if st.button("Submit"):
        print(entered_passcode)
        st.session_state.is_passcode_valid = entered_passcode == _PASSCODE

        if st.session_state.is_passcode_valid:
            st.rerun()
        else:
            st.error("Invalid Passcode")


if st.session_state.is_passcode_valid:
    pages = [
        st.Page("app/pages/home.py", title="Home", default=True),
        st.Page("app/pages/add-notes.py", title="Create your Note"),
        st.Page("app/pages/list-notes.py", title="Manage your Notes"),
    ]

    pg = st.navigation(pages)
    pg.run()
else:
    passcode_dialog()
