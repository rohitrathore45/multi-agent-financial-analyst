from typing import TypedDict, Optional, Dict, List

class AgentState(TypedDict):
    query: str
    ticker: Optional[str]

    market_data: Optional[Dict]
    
    response: Optional[str]