"""
Main application package
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

__version__ = "0.1.0"


def create_app() -> FastAPI:
    """Application factory pattern"""
    
    app = FastAPI(
        title="My Backend API",
        description="Simple backend without database",
        version=__version__,
    )
    
    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # ใน production ควรระบุ domain ชัดเจน
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Register routes
    from .api import router
    app.include_router(router, prefix="/api")
    
    @app.get("/")
    async def root():
        return {
            "message": "Welcome to Backend API",
            "version": __version__,
            "docs": "/docs"
        }
    
    return app