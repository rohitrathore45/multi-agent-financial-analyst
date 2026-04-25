from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

def decision_agent(state):
    prompt = f"""
    Based on the following:

    Sentiment: {state["sentiment"]}
    Features: {state["features"]}
    Risk: {state["risk"]}

    Decide:
    BUY, SELL, or HOLD

    Also give confidence (0-1)

    Return JSON:
    {{
        "action": "...",
        "confidence": ...
    }}
    """

    result = llm.invoke(prompt)
    state["decision"] = result.content
    return state