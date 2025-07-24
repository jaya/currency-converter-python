import pytest
import pytest_asyncio
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_convert_and_get_transactions(client: AsyncClient):
    # create transaction
    user_id = "test_user_integration"
    response_post = await client.post(
        "/api/v1/conversion/convert",
        json={
            "user_id": user_id,
            "from_currency": "USD",
            "to_currency": "BRL",
            "amount": 100
        }
    )

    # create transaction validation
    assert response_post.status_code == 200
    data = response_post.json()
    assert "transaction_id" in data
    assert data["user_id"] == user_id
    assert data["from_currency"] == "USD"
    assert data["to_currency"] == "BRL"

    # get transactions
    response_get = await client.get(
        f"/api/v1/transactions/?user_id={user_id}"
    )

    # get transaction validation
    assert response_get.status_code == 200
    transactions = response_get.json()
    assert isinstance(transactions, list)
    assert len(transactions) == 1
    assert transactions[0]["id"] == data["transaction_id"]
    assert transactions[0]["user_id"] == user_id
