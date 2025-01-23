import streamlit as st
from app.config import PASSCODE

if "is_passcode_valid" not in st.session_state:
    st.session_state.is_passcode_valid = False


st.logo("assets/logo.svg", size="large")


@st.dialog("Passcode")
def passcode_dialog():
    with st.form("passcode", clear_on_submit=True, border=False):
        entered_passcode = st.text_input(
            "Passcode", label_visibility="collapsed")
        if st.form_submit_button("Submit"):
            st.session_state.is_passcode_valid = entered_passcode == PASSCODE

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
