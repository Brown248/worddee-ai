"""
Test API routes
"""
import pytest
from fastapi.testclient import TestClient
from app import create_app

client = TestClient(create_app())


def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_health_check():
    """Test health check endpoint"""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_send_message():
    """Test message endpoint"""
    payload = {"message": "Hello Test"}
    response = client.post("/api/message", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "Received: Hello Test" in data["message"]
    assert "timestamp" in data


def test_process_data():
    """Test data processing endpoint"""
    payload = {"data": [1, 2, 3, 4, 5]}
    response = client.post("/api/data", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["count"] == 5
    assert data["result"]["sum"] == 15
    assert data["result"]["avg"] == 3.0


def test_ephemeral_store():
    """Test ephemeral store endpoints"""
    # Store data
    test_data = {"name": "test", "value": 123}
    response = client.post("/api/store/test_key", json=test_data)
    assert response.status_code == 200
    
    # Get data
    response = client.get("/api/store/test_key")
    assert response.status_code == 200
    assert response.json()["data"] == test_data
    
    # Delete data
    response = client.delete("/api/store/test_key")
    assert response.status_code == 200
    
    # Get deleted data (should fail)
    response = client.get("/api/store/test_key")
    assert response.status_code == 404