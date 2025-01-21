import streamlit as st

st.logo("assets/logo.svg", size="large")

pages = [
    st.Page("app/pages/home.py", title="Home", default=True),
    st.Page("app/pages/add-notes.py", title="Create your Note"),
    st.Page("app/pages/list-notes.py", title="Manage your Notes"),
]

pg = st.navigation(pages)
pg.run()
