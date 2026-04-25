import yfinance as yf

def get_stock_data(ticker: str):
    stock = yf.Ticker(ticker=ticker)

    info = stock.info
    hist = stock.history(period="5d")
    return {
        "current_price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "volume": info.get("volume"),
        "history": hist["Close"].tolist()
    }