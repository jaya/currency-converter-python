from unittest.mock import MagicMock

from model import Transaction
from repository import TransactionRepository


def test_find_transaction_by_user_id(session) -> None:
    repository = TransactionRepository(session)
    repository._session.execute = MagicMock()
    repository.find_transactions_by_user_id(10)
    assert repository._session.execute.called


def test_persist(session) -> None:
    repository = TransactionRepository(session)
    repository._session.add = MagicMock()
    repository._session.commit = MagicMock()
    transaction = Transaction()
    transaction = repository.persist(transaction)
    assert repository._session.add.called
    assert repository._session.commit.called
