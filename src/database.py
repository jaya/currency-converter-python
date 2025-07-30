from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session

from config import Config


def get_engine() -> Engine:
    driver = Config.DATABASE_DRIVER
    user = Config.DATABASE_USER
    password = Config.DATABASE_PASSWORD
    host = Config.DATABASE_HOST
    port = Config.DATABASE_PORT
    database = Config.DATABASE_NAME
    database_url = f"{driver}://{user}:{password}@{host}:{port}/{database}"
    return create_engine(database_url, echo=False)


def get_session() -> Session:
    engine = get_engine()
    session = sessionmaker(bind=engine, expire_on_commit=False)
    return session()
