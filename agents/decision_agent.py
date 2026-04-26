from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY
import json

def decision_agent(state):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

    sentiment = state.get("sentiment")
    trend = state.get("features", {}).get("price_trend")
    risk = state.get("risk")

    market_data = state.get("market_data", {})
    current_price = market_data.get("current_price")
    predicted_price = state.get("predicted_price")

    memory = state.get("memory", [])

    # SAFETY CHECK
    if not sentiment or not trend or not risk:
        state["decision"] = {"action": "HOLD", "confidence": 0.5}
        return state

    # STEP 1: ML-BASED DECISION (PRIMARY)
    if predicted_price is not None and current_price is not None:

        diff = predicted_price - current_price
        percent_change = diff / current_price

        pct = round(abs(percent_change * 100), 2)

        print("Current Price:", current_price)
        print("Predicted Price:", predicted_price)
        print("Change %:", percent_change)

        # STRONG BUY
        if percent_change > 0.02:
            confidence = 0.75

            if risk == "high":
                confidence -= 0.1  # risk penalty

            state["decision"] = {
                "action": "BUY",
                "confidence": round(confidence, 2),
                "reason": f"Predicted price is {pct}% higher than current"
            }
            return state

        # STRONG SELL
        elif percent_change < -0.02:
            confidence = 0.75

            if risk == "high":
                confidence -= 0.1

            state["decision"] = {
                "action": "SELL",
                "confidence": round(confidence, 2),
                "reason": f"Predicted price is {pct}% lower than current"
            }
            return state

        # HOLD (NO LLM NEEDED)
        else:
            confidence = 0.6

            if risk == "high":
                confidence -= 0.1

            state["decision"] = {
                "action": "HOLD",
                "confidence": round(confidence, 2),
                "reason": f"Predicted change is small ({pct}%), no strong signal"
            }
            return state

    # STEP 2: LLM (ONLY IF ML NOT AVAILABLE)
    prompt = f"""
    You are a financial decision engine.

    Sentiment: {sentiment}
    Trend: {trend}
    Risk: {risk}

    Past Decisions:
    {memory}

    If signals conflict, return HOLD.

    Return STRICT JSON:
    {{
        "action": "BUY | SELL | HOLD",
        "confidence": 0 to 1
    }}
    """

    result = llm.invoke(prompt)

    try:
        decision = json.loads(result.content)
    except:
        decision = {"action": "HOLD", "confidence": 0.5}

    print("LLM Decision:", decision)

    state["decision"] = decision
    return state