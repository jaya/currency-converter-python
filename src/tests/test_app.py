def test_transaction_post_should_fail_with_422(client) -> None:
    response = client.post("/transactions", json={})
    assert response.status_code == 422


def test_transaction_post_should_succeed(client) -> None:
    response = client.post(
        "/transactions",
        json={"value": 100, "from_currency": "BRL", "to_currency": "BRL", "user_id": 1},
    )
    assert response.status_code == 200


def test_transaction_get_should_succeed(client) -> None:
    response = client.get("/transactions?user_id=1")
    assert response.status_code == 200


def test_transaction_get_should_fail_with_404(client) -> None:
    response = client.get("/transactions?user_id=10")
    assert response.status_code == 404
