from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from app.config import OPENAI_API_KEY
import os

DB_PATH = "faiss_index"

db = None

def get_embedding():
    return OpenAIEmbeddings(api_key=OPENAI_API_KEY)

def load_db():
    global db
    if os.path.exists(DB_PATH):
        embedding = get_embedding()
        db = FAISS.load_local(
            DB_PATH,
            embedding,
            allow_dangerous_deserialization=True
        )
        print("Loaded existing memory")

def save_db():
    if db:
        db.save_local(DB_PATH)
        print("Memory saved")

def store_memory(texts):
    global db

    if db is None:
        load_db()

    if db is None:
        embedding = get_embedding()
        db = FAISS.from_texts(texts, embedding)
    else:
        db.add_texts(texts)

    print("Storing: ", texts)
    save_db()

def retrieve_memory(query):
    global db

    if db is None:
        load_db()

    if db is None:
        print("No memory found")
        return []
    
    docs = db.similarity_search(query=query, k=5)

    result = [doc.page_content for doc in docs]

    print("Retrived:", result)

    return result