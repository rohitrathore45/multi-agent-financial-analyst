def feature_agent(state):

    data = state['market_data']

    if not data:
        return state
    
    history = data['history']

    trend = "upward" if history[-1] > history[0] else "downward"

    features = {
        "price_trend": trend,
        "volume": data["volume"]
    }

    state["features"] = features
    return state