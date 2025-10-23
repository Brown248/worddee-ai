"""
API Routes
"""
from fastapi import APIRouter, HTTPException
from .schemas import (
    MessageRequest, 
    MessageResponse, 
    DataRequest, 
    DataResponse
)
from ..services import DataService
from ..utils import ephemeral_store

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@router.post("/message", response_model=MessageResponse)
async def send_message(request: MessageRequest):
    """
    ส่งข้อความและได้รับ response กลับ
    """
    return MessageResponse(
        message=f"Received: {request.message}",
        timestamp="2025-10-22T10:00:00Z"
    )


@router.post("/data", response_model=DataResponse)
async def process_data(request: DataRequest):
    """
    ประมวลผลข้อมูลผ่าน service layer
    """
    service = DataService()
    result = await service.process(request.data)
    
    return DataResponse(
        result=result,
        count=len(request.data)
    )


@router.post("/store/{key}")
async def store_data(key: str, data: dict):
    """
    เก็บข้อมูลชั่วคราวใน ephemeral store
    """
    ephemeral_store.set(key, data)
    return {"message": f"Stored data with key: {key}"}


@router.get("/store/{key}")
async def get_data(key: str):
    """
    ดึงข้อมูลจาก ephemeral store
    """
    data = ephemeral_store.get(key)
    if data is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"key": key, "data": data}


@router.delete("/store/{key}")
async def delete_data(key: str):
    """
    ลบข้อมูลจาก ephemeral store
    """
    deleted = ephemeral_store.delete(key)
    if not deleted:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"message": f"Deleted key: {key}"}