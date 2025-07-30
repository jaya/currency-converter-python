from currencyapicom import Client

from config import Config
from database import get_session
from exceptions import (
    CurrencyAPIException,
    FailToParseException,
    FailToStoreDataException,
)
from logger import CustomLogger
from model import Transaction
from validators import Convert


logger = CustomLogger().get_logger()


class CurrencyService:

    def __init__(self) -> None:
        try:
            self.__client = Client(Config.CURRENCY_API_KEY)
            self.__exchanges = self.__client.latest()
        except Exception:
            logger.exception("Failed to get currency exchange list")
            raise CurrencyAPIException("Currency API is unavailable")
        self._session = get_session()

    def calculate_transaction(self, data: Convert):
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

    def __build(self, data: Convert, rate: float, value: float) -> Transaction:
        transaction = Transaction()
        transaction.user_id = data.user_id
        transaction.rate = rate
        transaction.from_currency = data.from_currency
        transaction.to_currency = data.to_currency
        transaction.from_value = data.value
        transaction.to_value = value
        return transaction

    def persist(self, transaction: Transaction) -> Transaction:
        try:
            self._session.add(transaction)
            self._session.commit()
            return transaction
        except Exception:
            message = f"Failed to persist {transaction}"
            logger.exception(message)
            raise FailToStoreDataException(message)

    def __del__(self) -> None:
        self._session.close()
