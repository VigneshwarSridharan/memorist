import streamlit as st
from vector_store import get_notes_vector_Store

st.write("# List Notes")

vector_store = get_notes_vector_Store()

docs = vector_store.g
