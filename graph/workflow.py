from langgraph.graph import StateGraph, START, END
from graph.state import AgentState

from agents.data_agent import data_agent
from agents.news_agent import news_agent
from agents.sentiment_agent import sentiment_agent
from agents.feature_agent import feature_agent
from agents.risk_agent import risk_agent
from agents.decision_agent import decision_agent
from agents.memory_agent import memory_agent
from memory.vector_store import store_memory
from agents.modeling_agent import modeling_agent

from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY

def generate_response(state: AgentState):

    print("Generating structured response...")

    features = state.get("features") or {}

    response = {
        "ticker": state.get("ticker"),
        "sentiment": state.get("sentiment"),
        "trend": features.get("price_trend"),
        "risk": state.get("risk"),
        "predicted_price": state.get("predicted_price"),
        "decision": state.get("decision"),
        "memory_used": state.get("memory", [])
    }

    # Store memory
    store_memory([
        f"""
        Ticker: {state.get('ticker')}
        Decision: {state.get('decision')}
        Sentiment: {state.get('sentiment')}
        Predicted Price: {state.get('predicted_price')}
        """
    ])

    state["response"] = response

    print("Final Output:", response)

    return state


def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("data_agent", data_agent)
    builder.add_node("news_agent", news_agent)
    builder.add_node("sentiment_agent", sentiment_agent)
    builder.add_node("feature_agent", feature_agent)
    builder.add_node("risk_agent", risk_agent)
    builder.add_node("memory_agent", memory_agent)
    builder.add_node("decision_agent", decision_agent)
    builder.add_node("modeling_agent", modeling_agent)
    builder.add_node("generate_response", generate_response)

    builder.add_edge(START, "data_agent")
    builder.add_edge("data_agent", "news_agent")
    builder.add_edge("news_agent", "sentiment_agent")
    builder.add_edge("sentiment_agent", "feature_agent")
    builder.add_edge("feature_agent", "modeling_agent")
    builder.add_edge("modeling_agent", "risk_agent")
    builder.add_edge("risk_agent", "memory_agent")
    builder.add_edge("memory_agent", "decision_agent")
    builder.add_edge("decision_agent", "generate_response")
    builder.add_edge("generate_response", END)

    return builder.compile()