from tools.market_tools import get_stock_data

def data_agent(state):
    query = state["query"]

    if not query or len(query.split()) == 0:
        state["response"] = "Please enter a valid entry like 'Analyze AAPL'"
        return state

    ticker = query.split()[-1].upper()

    data = get_stock_data(ticker=ticker)

    state['ticker'] = ticker
    state['market_data'] = data

    return state