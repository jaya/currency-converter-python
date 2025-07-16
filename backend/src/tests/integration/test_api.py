import pytest
from httpx import AsyncClient
from src.currency_converter.main import app

@pytest.mark.asyncio
async def test_convert_currency():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post(
            "/api/v1/conversion/convert",
            json={
                "user_id": "test_user",
                "from_currency": "USD",
                "to_currency": "BRL",
                "amount": 100
            }
        )
    
    assert response.status_code == 200
    data = response.json()
    assert "transaction_id" in data
    assert data["from_currency"] == "USD"
    assert data["to_currency"] == "BRL"

@pytest.mark.asyncio
async def test_get_transactions():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get(
            "/api/v1/transactions/?user_id=test_user"
        )
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)