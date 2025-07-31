from unittest.mock import patch, MagicMock

from model import Transaction
from repository import TransactionRepository


@patch("repository.get_session", autospec=True)
def test_find_transaction_by_user_id(get_session: MagicMock) -> None:
    repository = TransactionRepository(get_session)
    repository._session.execute = MagicMock()
    repository.find_transactions_by_user_id(10)
    assert repository._session.execute.called


@patch("repository.get_session", autospec=True)
def test_persist(get_session: MagicMock) -> None:
    repository = TransactionRepository(get_session)
    repository._session.add = MagicMock()
    repository._session.commit = MagicMock()
    transaction = Transaction()
    transaction = repository.persist(transaction)
    assert repository._session.add.called
    assert repository._session.commit.called
