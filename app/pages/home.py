"""Home Page"""

import streamlit as st
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from typing import List
from app.vector_store import get_notes_vector_Store
from langchain_core.prompts import SystemMessagePromptTemplate
from app.templates import NOTES_TEMPLATE

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

vector_store = get_notes_vector_Store()


if "messages" not in st.session_state:
    st.session_state["messages"] = [AIMessage(content="How can I help you?")]


for msg in st.session_state.messages:
    st.chat_message(msg.type).write(msg.content)

if prompt := st.chat_input():
    humanMessage = HumanMessage(content=prompt)
    st.session_state.messages.append(humanMessage)
    st.chat_message(humanMessage.type).write(humanMessage.content)

    promptTemplate = SystemMessagePromptTemplate.from_template(template=NOTES_TEMPLATE)
    result = vector_store.similarity_search_with_score(prompt, 5)

    notes = [
        {
            "note": doc.page_content,
            "date": doc.metadata["date"] if "date" in doc.metadata else "",
        }
        for doc in result
    ]

    message = promptTemplate.format(
        notes=json.dumps(notes),
        prompt=prompt,
    )

    response = llm.invoke(message.content)

    aiMessage = AIMessage(content=response.content)
    st.session_state.messages.append(aiMessage)
    st.chat_message(aiMessage.type).write(aiMessage.content)
