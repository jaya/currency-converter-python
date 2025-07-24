import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from httpx import AsyncClient
from src.currency_converter.main import app
from src.currency_converter.db.session import get_db, Base

# setup memory database for testing
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# override get_db dependency to use the test database
async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session

app.dependency_overrides[get_db] = override_get_db

# fixture to create and clean the dabase tables for each test
@pytest_asyncio.fixture(autouse=True)
async def setup_and_teardown_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# fixture to provide an async HTTP client
@pytest_asyncio.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest_asyncio.fixture
async def db_session() -> AsyncSession:
    async with TestingSessionLocal() as session:
        yield session
