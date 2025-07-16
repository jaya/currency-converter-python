import pytest
from datetime import datetime
from src.currency_converter.db.repositories import ConversionRepository
from src.currency_converter.db.models import ConversionTransaction

@pytest.mark.asyncio
async def test_create_transaction(db_session):
    repo = ConversionRepository(db_session)
    
    transaction = await repo.create_transaction(
        user_id="test_user",
        from_currency="USD",
        to_currency="BRL",
        from_value=100.0,
        to_value=520.0,
        rate=5.2
    )
    
    assert transaction.id is not None
    assert transaction.user_id == "test_user"

@pytest.mark.asyncio
async def test_get_transactions(db_session, test_transaction):
    repo = ConversionRepository(db_session)
    
    transactions = await repo.get_transactions_by_user("test_user")
    
    assert len(transactions) == 1
    assert transactions[0].id == test_transaction.id