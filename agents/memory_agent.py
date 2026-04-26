from memory.vector_store import retrieve_memory

def memory_agent(state):
    ticker = state.get("ticker")

    past_data = retrieve_memory(ticker)

    filtered = [m for m in past_data if ticker in m]

    state["memory"] = filtered

    return state