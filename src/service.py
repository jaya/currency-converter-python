from typing import Sequence

from currencyapicom import Client
from sqlalchemy import Row

from config import Config
from exceptions import (
    CurrencyAPIException,
    FailToParseException,
)
from logger import CustomLogger
from model import Transaction
from repository import TransactionRepository
from validators import TransactionRequest

logger = CustomLogger().get_logger()


class TransactionService:

    def __init__(self) -> None:
        try:
            self.__client = Client(Config.CURRENCY_API_KEY)
            self.__exchanges = self.__client.latest()
        except Exception:
            logger.exception("Failed to get currency exchange list")
            raise CurrencyAPIException("Currency API is unavailable")
        self._repository = TransactionRepository()

    def calculate_transaction(self, data: TransactionRequest):
        try:
            rate_to = self.__exchanges["data"][data.to_currency]["value"]
            rate_from = self.__exchanges["data"][data.from_currency]["value"]
            dollar_amount = 1 / rate_from * data.value
            value = dollar_amount * rate_to
            return self.__build(data, rate_to, value)
        except Exception:
            message = f"Failed to convert {data.to_currency} to {data.from_currency}"
            logger.exception(message)
            raise FailToParseException(message)

    def __build(
        self, data: TransactionRequest, rate: float, value: float
    ) -> Transaction:
        transaction = Transaction()
        transaction.user_id = data.user_id
        transaction.rate = rate
        transaction.from_currency = data.from_currency
        transaction.to_currency = data.to_currency
        transaction.from_value = data.value
        transaction.to_value = value
        self._repository.persist(transaction)
        return transaction

    def get_transactions_by_user_id(
        self, user_id: int
    ) -> Sequence[Row[tuple[Transaction]]]:
        return self._repository.find_transactions_by_user_id(user_id)
