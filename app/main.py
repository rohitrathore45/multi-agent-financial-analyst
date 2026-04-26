from graph.workflow import build_graph
import json

def main():
    graph = build_graph()

    query = input("Enter your query (e.g., Analyze AAPL): ")

    state = {
        "query": query,
        "ticker": None,
        "market_data": None,
        "news": None,
        "sentiment": None,
        "features": None,
        "risk": None,
        "decision": None,
        "memory": None,
        "predicted_price": None,
        "response": None
    }

    result = graph.invoke(state)
    print("\n RESULT : \n")
    print(json.dumps(result["response"], indent=2))

if __name__ == "__main__":
    main()