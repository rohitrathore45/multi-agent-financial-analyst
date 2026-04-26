from typing import TypedDict, Optional, Dict, List

class AgentState(TypedDict):
    query: str
    ticker: Optional[str]

    market_data: Optional[Dict]

    news: Optional[List[str]]
    sentiment: Optional[str]

    features: Optional[Dict]

    risk: Optional[str]
    decision: Optional[Dict]

    memory: Optional[List[str]]
    
    response: Optional[str]

    predicted_price: Optional[float]