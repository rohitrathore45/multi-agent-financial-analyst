from memory.vector_store import retrieve_memory

def memory_agent(state):
    query = state["query"]

    past_data = retrieve_memory(query)

    state["memory"] = past_data

    return state