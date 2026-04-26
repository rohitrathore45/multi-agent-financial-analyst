from pydantic import BaseModel
from typing import Optional, Dict, List

class AnalyzeRequest(BaseModel):
    query: str
    
class AnalyzeResponse(BaseModel):
    ticker: Optional[str]
    sentiment: Optional[str]
    trend: Optional[str]
    risk: Optional[str]
    predicted_price: Optional[float]
    decision: Optional[Dict]
    memory_used: Optional[List[str]]