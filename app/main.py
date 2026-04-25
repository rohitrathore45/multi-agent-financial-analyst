from graph.workflow import build_graph

def main():
    graph = build_graph()

    query = input("Enter your query (e.g., Analyze AAPL): ")

    state = {
        "query": query,
        "ticker": None,
        "market_data": None,
        "response": None
    }

    result = graph.invoke(state)
    print("\n RESULT : \n")
    print(result["response"])

if __name__ == "__main__":
    main()