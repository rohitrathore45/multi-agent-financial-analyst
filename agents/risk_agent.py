def risk_agent(state):
    features = state["features"]

    if not features:
        return state
    
    if features["price_trend"] == "downward":
        risk = "high"
    else:
        risk = "low"

    state["risk"] = risk
    return state