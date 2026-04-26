from fastapi import APIRouter
from app.schemas import AnalyzeRequest, AnalyzeResponse
from graph.workflow import build_graph

router = APIRouter()

# build graph once
graph = build_graph()

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_stock(request: AnalyzeRequest):
    state = {
        "query": request.query,
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
    return result['response']