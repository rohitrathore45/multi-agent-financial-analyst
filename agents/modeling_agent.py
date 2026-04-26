import numpy as np
import xgboost as xgb

def create_features(prices):
    prices = np.array(prices)

    returns = np.diff(prices)
    returns = np.append(returns, returns[-1])

    moving_avg_3 = np.convolve(prices, np.ones(3)/3, mode='same')
    moving_avg_5 = np.convolve(prices, np.ones(5)/5, mode='same')

    X = []

    for i in range(len(prices)):
        vol = np.std(prices[max(0, i-5):i+1])

        X.append([
            prices[i],
            returns[i],
            moving_avg_3[i],
            moving_avg_5[i],
            vol
        ])

    return np.array(X), prices


def modeling_agent(state):
    print("Modeling Agent Running")

    market_data = state.get("market_data")

    if not market_data or "history" not in market_data:
        state["predicted_price"] = None
        return state
    
    prices = market_data["history"]

    print("Prices Length:", len(prices))

    if len(prices) < 20:
        print("Not enough data")
        state["predicted_price"] = None
        return state
    
    X, y = create_features(prices)

    model = xgb.XGBRegressor(
        n_estimators=100,
        max_depth=3,
        learning_rate=0.1
    )

    try:
        X_train = X[:-1]
        y_train = y[:-1]

        last_features = X[-1].reshape(1, -1)

        model.fit(X_train, y_train)
        prediction = model.predict(last_features)

        state["predicted_price"] = float(prediction[0])

    except Exception as e:
        print("XGBoost ERROR:", e)

        # FALLBACK
        from sklearn.linear_model import LinearRegression

        print("Falling back to Linear Regression")

        X_lr = np.arange(len(prices)).reshape(-1, 1)
        y_lr = np.array(prices)

        lr = LinearRegression()
        lr.fit(X_lr, y_lr)

        pred = lr.predict([[len(prices)]])
        state["predicted_price"] = float(pred[0])

    print("Predicted Price:", state["predicted_price"])

    return state