"""
Pydantic schemas for request/response validation
"""
from pydantic import BaseModel, Field
from typing import List, Any


class MessageRequest(BaseModel):
    message: str = Field(..., min_length=1, description="ข้อความที่ต้องการส่ง")
    
    class Config:
        json_schema_extra = {
            "example": {
                "message": "Hello World"
            }
        }


class MessageResponse(BaseModel):
    message: str
    timestamp: str


class DataRequest(BaseModel):
    data: List[Any] = Field(..., description="ข้อมูลที่ต้องการประมวลผล")
    
    class Config:
        json_schema_extra = {
            "example": {
                "data": [1, 2, 3, 4, 5]
            }
        }


class DataResponse(BaseModel):
    result: Any
    count: int