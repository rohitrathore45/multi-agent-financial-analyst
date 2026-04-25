from tools.market_tools import get_stock_data

def data_agent(state):
    query = state["query"]

    ticker = query.split()[-1].upper()

    data = get_stock_data(ticker=ticker)

    state['ticker'] = ticker
    state['market_data'] = data

    return state