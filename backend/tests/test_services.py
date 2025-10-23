"""
Test services
"""
import pytest
from app.services import DataService
from app.utils import EphemeralStore


@pytest.mark.asyncio
async def test_data_service_process():
    """Test data processing service"""
    service = DataService()
    
    # Test with numeric data
    result = await service.process([1, 2, 3, 4, 5])
    assert result["sum"] == 15
    assert result["avg"] == 3.0
    assert result["min"] == 1
    assert result["max"] == 5
    
    # Test with empty data
    result = await service.process([])
    assert "error" in result


@pytest.mark.asyncio
async def test_data_service_validate():
    """Test data validation and transformation"""
    service = DataService()
    
    # Test string transformation
    result = await service.validate_and_transform("hello")
    assert result == "HELLO"
    
    # Test list transformation
    result = await service.validate_and_transform(["hello", "world"])
    assert result == ["HELLO", "WORLD"]


def test_ephemeral_store():
    """Test ephemeral store"""
    store = EphemeralStore()
    
    # Test set and get
    store.set("key1", "value1")
    assert store.get("key1") == "value1"
    
    # Test exists
    assert store.exists("key1") == True
    assert store.exists("nonexistent") == False
    
    # Test delete
    assert store.delete("key1") == True
    assert store.delete("key1") == False  # already deleted
    
    # Test TTL
    store.set("expire_key", "value", ttl=1)
    assert store.get("expire_key") == "value"
    
    import time
    time.sleep(2)
    assert store.get("expire_key") is None  # expired
    
    # Test stats
    store.set("k1", "v1")
    store.set("k2", "v2")
    stats = store.get_stats()
    assert stats["total_keys"] == 2
    
    # Test clear
    store.clear()
    assert store.get_stats()["total_keys"] == 0