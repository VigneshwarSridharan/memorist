from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import SingleStoreDB
import os

load_dotenv()


def get_notes_vector_Store():
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    return SingleStoreDB(
        embedding=embeddings,
        table_name="notes",
    )
