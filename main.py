from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import SingleStoreDB
from langchain_core.documents import Document
import os

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

vector_store = SingleStoreDB(
    embedding=embeddings,
    table_name="notes",
)

while True:
    prompt = input("Prompt: ")
    if prompt == "exit":
        break

    result = vector_store.similarity_search_with_score(prompt, k=5)

    print(result)

    docs = [doc for doc, scrore in result if scrore > 0.9]

    print("===" * 30)
    print(docs)

    # for doc, score in result:
    #     print(f"document={doc.page_content}, score={score}")
