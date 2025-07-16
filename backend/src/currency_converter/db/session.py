from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from ..core.config import settings

Base = declarative_base()

engine = create_async_engine(
    settings.DATABASE_URL,
    future=True,
    echo=True if settings.ENVIRONMENT == "development" else False
)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

async def get_db():
    async with async_session() as session:
        yield session