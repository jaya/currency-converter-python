from decimal import Decimal
from loguru import logger
from ..db.repositories import ConversionRepository
from .currency_api import CurrencyAPIService

class ConversionService:
    def __init__(self, conversion_repo: ConversionRepository):
        self.conversion_repo = conversion_repo
        self.currency_api = CurrencyAPIService()

    async def convert_currency(
        self,
        user_id: str,
        from_currency: str,
        to_currency: str,
        amount: Decimal
    ) -> dict:
        if from_currency == to_currency:
            raise ValueError("Cannot convert between same currencies")

        rates = await self.currency_api.get_exchange_rates(from_currency)

        if to_currency not in rates:
            raise ValueError(f"Unsupported target currency: {to_currency}")

        rate = Decimal(str(rates[to_currency]["value"]))
        converted_amount = amount * rate

        transaction = await self.conversion_repo.create_transaction(
            user_id=user_id,
            from_currency=from_currency,
            to_currency=to_currency,
            from_value=amount,
            to_value=converted_amount,
            rate=rate
        )

        return {
            "original_amount": amount,
            "converted_amount": converted_amount,
            "rate": rate,
            "transaction_id": transaction.id,
            "timestamp": transaction.timestamp
        }

    async def get_user_transactions(self, user_id: str):
        return await self.conversion_repo.get_transactions_by_user(user_id)
