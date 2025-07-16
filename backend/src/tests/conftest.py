import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.currency_converter.db.session import Base
from src.currency_converter.db.models import ConversionTransaction

@pytest.fixture
async def db_session():
    engine = create_async_engine(
        "postgresql+asyncpg://test:test@localhost:5432/test_db"
    )
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async_session = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    
    async with async_session() as session:
        yield session
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    
    await engine.dispose()

@pytest.fixture
async def test_transaction(db_session):
    transaction = ConversionTransaction(
        user_id="test_user",
        from_currency="USD",
        to_currency="BRL",
        from_value=100.0,
        to_value=520.0,
        rate=5.2
    )
    db_session.add(transaction)
    await db_session.commit()
    return transaction