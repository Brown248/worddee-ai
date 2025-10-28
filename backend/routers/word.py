from fastapi import APIRouter, HTTPException
from schemas.word_schema import WordResponse
from services.word_service import get_random_word

router = APIRouter(prefix="/api", tags=["Word of the Day"])

@router.get("/word", response_model=WordResponse)
def get_word():
    try:
        return get_random_word()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
