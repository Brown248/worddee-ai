"""
In-memory ephemeral data store
ข้อมูลจะหายเมื่อ restart server
"""
import time
from typing import Any, Optional, Dict
from datetime import datetime, timedelta


class EphemeralStore:
    """
    Simple in-memory key-value store with TTL support
    """
    
    def __init__(self, default_ttl: int = 300):
        """
        Args:
            default_ttl: Time to live in seconds (default 5 minutes)
        """
        self._store: Dict[str, Dict[str, Any]] = {}
        self.default_ttl = default_ttl
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """
        Store a value with optional TTL
        """
        expire_time = time.time() + (ttl or self.default_ttl)
        self._store[key] = {
            "value": value,
            "expire_at": expire_time
        }
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get a value if it exists and hasn't expired
        """
        self._cleanup_expired()
        
        if key not in self._store:
            return None
        
        item = self._store[key]
        if time.time() > item["expire_at"]:
            del self._store[key]
            return None
        
        return item["value"]
    
    def delete(self, key: str) -> bool:
        """
        Delete a key
        Returns True if key existed, False otherwise
        """
        if key in self._store:
            del self._store[key]
            return True
        return False
    
    def exists(self, key: str) -> bool:
        """
        Check if key exists and hasn't expired
        """
        return self.get(key) is not None
    
    def clear(self) -> None:
        """
        Clear all stored data
        """
        self._store.clear()
    
    def _cleanup_expired(self) -> None:
        """
        Remove expired items
        """
        current_time = time.time()
        expired_keys = [
            key for key, item in self._store.items()
            if current_time > item["expire_at"]
        ]
        for key in expired_keys:
            del self._store[key]
    
    def get_stats(self) -> dict:
        """
        Get store statistics
        """
        self._cleanup_expired()
        return {
            "total_keys": len(self._store),
            "keys": list(self._store.keys())
        }