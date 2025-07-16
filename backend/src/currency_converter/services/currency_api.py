import os
import requests
from loguru import logger
from ..core.config import settings

class CurrencyAPIService:
    def __init__(self):
        self.base_url = "https://api.currencyapi.com/v3/latest"
        self.api_key = settings.CURRENCY_API_KEY
    
    async def get_exchange_rates(self, base_currency: str) -> dict:
        try:
            response = requests.get(
                self.base_url,
                params={
                    "apikey": self.api_key,
                    "base_currency": base_currency,
                    "currencies": "BRL,USD,EUR,JPY"
                },
                timeout=10
            )
            response.raise_for_status()
            return response.json()["data"]
        except Exception as e:
            logger.error(f"Failed to fetch exchange rates: {str(e)}")
            raise