import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from src.currency_converter.db.repositories import ConversionRepository
from decimal import Decimal

@pytest.mark.asyncio
async def test_repository_can_create_and_get_transaction(db_session: AsyncSession):
    # create converion transaction
    repo = ConversionRepository(db_session)

    user_id = "test_user_repo"
    transaction = await repo.create_transaction(
        user_id=user_id,
        from_currency="USD",
        to_currency="BRL",
        from_value=100.0,
        to_value=520.0,
        rate=5.2
    )

    # validate transaction
    assert transaction.id is not None
    assert transaction.user_id == user_id
    assert transaction.from_currency == "USD"

    # get transactions
    transactions = await repo.get_transactions_by_user(user_id)

    # validate transaction
    assert len(transactions) == 1
    assert transactions[0].id == transaction.id
    assert transactions[0].rate == Decimal('5.2')
