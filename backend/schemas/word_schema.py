from pydantic import BaseModel

class WordResponse(BaseModel):
    word: str
    suggestion: str
    level: str
    examples: list[str] | None = None
