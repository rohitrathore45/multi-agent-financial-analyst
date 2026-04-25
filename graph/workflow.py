from langgraph.graph import StateGraph, START, END
from graph.state import AgentState
from agents.data_agent import data_agent
from langchain_openai import ChatOpenAI
from app.config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

def generate_response(state: AgentState):
    data = state["market_data"]
    ticker = state["ticker"]

    prompt = f"""
    Analyze the stock {ticker} based on the following data:
    {data}
    Give a short insight.
    """

    result = llm.invoke(prompt)
    state["response"] = result.content
    return state

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("data_agent", data_agent)
    builder.add_node("generate_response", generate_response)

    builder.add_edge(START, "data_agent")
    builder.add_edge("data_agent", "generate_response")
    builder.add_edge("generate_response", END)

    return builder.compile()