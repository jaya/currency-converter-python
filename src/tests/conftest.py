import json

from unittest.mock import MagicMock

import pytest
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from app import app
from app import get_session, get_exchanges
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


def exchange() -> dict:
    fixture = json.load(open("src/tests/fixtures/exchanges.json", "r"))
    return fixture


@pytest.fixture(scope="session")
def exchanges():
    return exchange()


@pytest.fixture(scope="session")
def client():
    app.dependency_overrides[get_session] = override_session
    app.dependency_overrides[get_exchanges] = exchange
    return TestClient(app)


@pytest.fixture(scope="function")
def session():
    return MagicMock()
