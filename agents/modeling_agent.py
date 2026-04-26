import numpy as np
from sklearn.linear_model import LinearRegression

def modeling_agent(state):
    """
    LangGraph agent
    """

    market_data = state.get("market_data")

    if not market_data or "history" not in market_data:
        state["predicted_price"] = None
        return state
    
    prices = market_data["history"]

    if len(prices) < 5:
        state["predicted_price"] = None
        return state
    
    # Prepare dataset
    X = np.arange(len(prices)).reshape(-1, 1)
    y = np.array(prices)

    # Train model
    model = LinearRegression()
    model.fit(X, y)

    # Predict next day
    next_day = np.array([[len(prices)]])
    prediction = model.predict(next_day)

    state["predicted_price"] = float(prediction[0])

    print("Predicted Price:", state.get("predicted_price"))

    return state