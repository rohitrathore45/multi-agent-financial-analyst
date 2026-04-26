from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

def sentiment_agent(state):
    news = state["news"]

    prompt = f"""
    Analyze the sentiment of news:
    {news}
    Return only the word: positive, negative, or neutral.
    """
    
    result = llm.invoke(prompt)

    state["sentiment"] = result.content.strip().lower()
    return state