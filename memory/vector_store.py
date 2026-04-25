from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from app.config import OPENAI_API_KEY

embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

db = None

def store_memory(texts):
    global db
    if db is None:
        db = FAISS.from_texts(texts, embedding)
    else:
        db.add_texts(texts)

def retrieve_memory(query):
    if db is None:
        return []
    
    docs = db.similarity_search(query=query, k=2)
    return [doc.page_content for doc in docs]