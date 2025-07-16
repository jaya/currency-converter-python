from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://user:password@localhost:5432/currency_converter"
    CURRENCY_API_KEY: str = "your-api-key-here"
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"

settings = Settings()