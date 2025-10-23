"""
External service connectors and business logic
"""
import httpx
from typing import List, Any, Optional
from ..config import settings


class ExternalAPIConnector:
    """
    ตัวอย่าง connector สำหรับเชื่อมต่อ external API
    """
    
    def __init__(self):
        self.base_url = settings.EXTERNAL_API_URL
        self.api_key = settings.EXTERNAL_API_KEY
    
    async def fetch_data(self, endpoint: str) -> dict:
        """
        Fetch data from external API
        """
        if not self.base_url:
            return {"error": "External API URL not configured"}
        
        async with httpx.AsyncClient() as client:
            headers = {}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"
            
            response = await client.get(
                f"{self.base_url}/{endpoint}",
                headers=headers
            )
            response.raise_for_status()
            return response.json()


class DataService:
    """
    Business logic สำหรับประมวลผลข้อมูล
    """
    
    async def process(self, data: List[Any]) -> dict:
        """
        ประมวลผลข้อมูล - ตัวอย่างคำนวณค่าสถิติ
        """
        if not data:
            return {"error": "No data provided"}
        
        # ตัวอย่างการประมวลผล
        numeric_data = [x for x in data if isinstance(x, (int, float))]
        
        if not numeric_data:
            return {
                "message": "No numeric data to process",
                "items": data
            }
        
        return {
            "sum": sum(numeric_data),
            "avg": sum(numeric_data) / len(numeric_data),
            "min": min(numeric_data),
            "max": max(numeric_data),
            "count": len(numeric_data)
        }
    
    async def validate_and_transform(self, data: Any) -> Any:
        """
        Validate และ transform ข้อมูล
        """
        # ตัวอย่าง business logic
        if isinstance(data, str):
            return data.upper()
        elif isinstance(data, list):
            return [self.validate_and_transform(item) for item in data]
        else:
            return data