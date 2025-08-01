from os import getenv


class Config:

    CURRENCY_API_KEY = getenv("CURRENCY_KEY")
    DATABASE_DRIVER = getenv("DATABASE_DRIVER", "postgresql+psycopg2")
    DATABASE_USER = getenv("DATABASE_USER", "postgres")
    DATABASE_PASSWORD = getenv("DATABASE_PASSWORD", "example")
    DATABASE_HOST = getenv("DATABASE_HOST", "localhost")
    DATABASE_PORT = getenv("DATABASE_PORT", "5432")
    DATABASE_NAME = getenv("DATABASE_NAME", "postgres")
    TEST_DATABASE = ""
