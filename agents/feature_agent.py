def feature_agent(state):

    data = state['market_data']

    if not data or "history" not in data:
        return state
    
    history = data['history']

    if len(history) < 2:
        return state

    trend = "upward" if history[-1] > history[0] else "downward"

    features = {
        "price_trend": trend,
        "volume": data.get("volume")
    }

    state["features"] = features
    return state