def news_agent(state):
    ticker = state['ticker']

    # Dummy news (we’ll use real API later)
    news = [
        f"{ticker} reports poor earnings",
        f"{ticker} faces market pressure",
        f"{ticker} shows less growth potential"
    ]

    state['news'] = news
    return state