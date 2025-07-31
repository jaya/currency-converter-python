import pytest
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from app import app
from app import get_session
from model import Base


def override_session():
    engine = create_engine(
        "sqlite:///test.sqlite",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture(scope="session")
def client():
    app.dependency_overrides[get_session] = override_session
    return TestClient(app)
