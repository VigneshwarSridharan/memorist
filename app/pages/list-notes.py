import streamlit as st
from app.notes import get_all_notes

notes = get_all_notes()

st.write("# List Notes")

for note in notes:
    st.write(note["content"])
    st.divider()
