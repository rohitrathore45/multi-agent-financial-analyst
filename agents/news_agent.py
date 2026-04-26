from tavily import TavilyClient
from app.config import TAVILY_API_KEY

def news_agent(state):
    client = TavilyClient(api_key=TAVILY_API_KEY)
    ticker = state['ticker']

    query = f"{ticker} stock financial news latest earnings analysis"

    try:
        results = client.search(query=query, limit=3)

        articles = results.get("results", [])

        news = [r.get("title", "No title") for r in articles]

        if not news:
            news = ["No recent news found"]

    except Exception as e:
        print("News error:", e)
        news = ["Error fetching news"]

    state['news'] = news
    return state