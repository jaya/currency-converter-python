import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_convert_currency():
    payload = {
        "user_id": "testuser",
        "from_currency": "USD",
        "to_currency": "BRL",
        "amount": 10
    }

    response = client.post("/convert", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "testuser"
    assert data["from_currency"] == "USD"
    assert data["to_currency"] == "BRL"
    assert data["amount"] == 10
    assert data["converted_amount"] > 0
    assert data["conversion_rate"] > 0


def test_get_transactions():
    user_id = "testuser"
    response = client.get(f"/transactions?user_id={user_id}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    for tx in data:
        assert tx["user_id"] == user_id
