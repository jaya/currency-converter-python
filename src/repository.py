from typing import Sequence

from sqlalchemy import select, Row
from sqlalchemy.orm import Session

from exceptions import TransactionNotFoundException, FailToStoreDataException
from logger import CustomLogger
from model import Transaction


logger = CustomLogger().get_logger()


class TransactionRepository:

    def __init__(self, session: Session) -> None:
        self._session = session

    def find_transactions_by_user_id(
        self, user_id: int
    ) -> Sequence[Row[tuple[Transaction]]]:
        statement = select(Transaction).where(Transaction.user_id == user_id)
        values = self._session.execute(statement).fetchall()
        if not values:
            msg = f"No transactions found for user_id {user_id}"
            logger.warning(msg)
            raise TransactionNotFoundException(msg)
        return values

    def persist(self, transaction: Transaction) -> Transaction:
        try:
            self._session.add(transaction)
            self._session.commit()
            return transaction
        except Exception:
            message = f"Failed to persist {transaction}"
            logger.exception(message)
            raise FailToStoreDataException(message)
