"""
Configuration settings
"""
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # App
    APP_NAME: str = "Backend API"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True
    
    # API
    API_PREFIX: str = "/api"
    
    # External Service (ตัวอย่าง)
    EXTERNAL_API_URL: Optional[str] = None
    EXTERNAL_API_KEY: Optional[str] = None
    
    # Ephemeral Store
    CACHE_TTL: int = 300  # seconds
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# Singleton instance
settings = Settings()