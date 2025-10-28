from pydantic import BaseModel
from typing import List

class SummaryResponse(BaseModel):
    day_streak: int
    hours_learned: int
    recent_scores: List[float]
