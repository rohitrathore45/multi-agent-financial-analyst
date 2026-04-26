from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY
import json

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

def decision_agent(state):

    sentiment = state.get("sentiment")
    trend = state.get("features", {}).get("price_trend")
    risk = state.get("risk")

    if not sentiment or not trend or not risk:
        state["decision"] = {
            "action": "HOLD",
            "confidence": 0.5
        }
        return state

    market_data = state.get("market_data", {})
    current_price = market_data.get("current_price")

    predicted_price = state.get("predicted_price")

    # create ML signal
    ml_signal = "UNKNOWN"
    if predicted_price is not None and current_price is not None:
        if predicted_price > current_price:
            ml_signal = "UPWARD (BUY signal)"
        elif predicted_price < current_price:
            ml_signal = "DOWNWARD (SELL signal)"
        else:
            ml_signal = "STABLE (HOLD signal)"

    memory = state.get("memory", [])

    prompt = f"""
    You are an advanced financial decision engine.

    Based on:

    Sentiment: {sentiment}
    Trend: {trend}
    Risk: {risk}

    Current Price: {current_price}
    Predicted Price: {predicted_price}

    Past Decisions:
    {memory}

    ML Signal: {ml_signal}

    Rules:
    - If ML predicts price increase → favor BUY
    - If ML predicts price decrease → favor SELL
    - High risk → reduce confidence
    - Conflicting signals → HOLD

    Return STRICT JSON ONLY:

    {{
        "action": "BUY | SELL | HOLD",
        "confidence": 0 to 1
    }}
    """

    result = llm.invoke(prompt)
    
    try:
        decision = json.loads(result.content)
    except:
        decision = {
            "action": "HOLD",
            "confidence": 0.5
        }
    
    print("Decision : ", decision)

    state["decision"] = decision
    return state