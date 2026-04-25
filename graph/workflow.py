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

from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

def generate_response(state: AgentState):

    trend = state.get("features", {}).get("price_trend", "unknown")

    prompt = f"""
    You are a financial analyst.

    STOCK: {state["ticker"]}

    CURRENT SIGNALS:
    Sentiment: {state.get("sentiment")}
    Trend: {trend}
    Risk: {state.get("risk")}
    Decision: {state.get("decision")}

    PAST ANALYSIS:
    {state.get("memory", [])}

    Explain reasoning clearly.
    """

    result = llm.invoke(prompt)
    state["response"] = result.content
    store_memory([
        f"{state['ticker']} | {state['decision']} | {state['response']}"
    ])
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
    builder.add_node("generate_response", generate_response)

    builder.add_edge(START, "data_agent")
    builder.add_edge("data_agent", "news_agent")
    builder.add_edge("news_agent", "sentiment_agent")
    builder.add_edge("sentiment_agent", "feature_agent")
    builder.add_edge("feature_agent", "risk_agent")
    builder.add_edge("risk_agent", "decision_agent")
    builder.add_edge("decision_agent", "memory_agent")
    builder.add_edge("memory_agent", "generate_response")
    builder.add_edge("generate_response", END)

    return builder.compile()