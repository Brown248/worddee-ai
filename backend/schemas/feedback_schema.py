from pydantic import BaseModel, Field

class FeedbackRequest(BaseModel):
    word: str = Field(..., min_length=1)
    sentence: str = Field(..., min_length=1, max_length=1000)

class FeedbackResponse(BaseModel):
    score: float
    level: str
    corrected_sentence: str
    suggestion: str
