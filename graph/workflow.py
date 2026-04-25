from langgraph.graph import StateGraph, START, END
from graph.state import AgentState

from agents.data_agent import data_agent
from agents.news_agent import news_agent
from agents.sentiment_agent import sentiment_agent
from agents.feature_agent import feature_agent

from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

def generate_response(state: AgentState):

    prompt = f"""
    Analyze stock {state["ticker"]}

    Market Data: {state["market_data"]}
    News: {state["news"]}
    Sentiment: {state["sentiment"]}
    Features: {state["features"]}

    Give final insight.
    """

    result = llm.invoke(prompt)
    state["response"] = result.content
    return state

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("data_agent", data_agent)
    builder.add_node("news_agent", news_agent)
    builder.add_node("sentiment_agent", sentiment_agent)
    builder.add_node("feature_agent", feature_agent)
    builder.add_node("generate_response", generate_response)

    builder.add_edge(START, "data_agent")
    builder.add_edge("data_agent", "news_agent")
    builder.add_edge("news_agent", "sentiment_agent")
    builder.add_edge("sentiment_agent", "feature_agent")
    builder.add_edge("feature_agent", "generate_response")
    builder.add_edge("generate_response", END)

    return builder.compile()