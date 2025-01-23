from dotenv import load_dotenv
from langchain_core.documents import Document
import streamlit as st
from app.vector_store import get_notes_vector_Store
from datetime import date

vector_store = get_notes_vector_Store()

st.write("# Add new Note")


@st.fragment
def addNotePage():
    with st.form("add_note", border=False, clear_on_submit=True):
        value = st.text_area(
            "Note", key="note", height=500, label_visibility="collapsed"
        )

        isSummited = st.form_submit_button(
            "Save", use_container_width=True, type="primary"
        )
        if isSummited:
            if not value:
                st.error("Please enter notes")
            print("value", value)
            doc = Document(value, metadata={"date": date.today().isoformat()})
            vector_store.add_documents([doc])
            st.success("Done!")


addNotePage()
