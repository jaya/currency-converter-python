import json
import pytest
from unittest.mock import patch, MagicMock, call

from exceptions import CurrencyAPIException, FailToParseException
from service import TransactionService
from validators import TransactionRequest


@patch("service.TransactionRepository", return_value=MagicMock())
@patch("service.Client", return_value=MagicMock())
def test_calculate_transaction(
    client: MagicMock, transaction_repository: MagicMock
) -> None:
    service = TransactionService()
    fixture = json.load(open("tests/fixtures/exchanges.json", "r"))
    service._exchanges = fixture
    service._build = MagicMock()
    assert client.called
    data = TransactionRequest(
        from_currency="USD", to_currency="BRL", value=100, user_id=10
    )
    service.calculate_transaction(data)
    assert service._build.call_args_list == [
        call(data, 5.5748607533, 557.4860753300001)
    ]


@patch("service.TransactionRepository", return_value=MagicMock())
@patch("service.Client", return_value=MagicMock())
def test_should_raise_exception_when_calculation_fails(
    client: MagicMock, repository: MagicMock
) -> None:
    service = TransactionService()
    service._exchanges = {}
    service._build = MagicMock()
    data = TransactionRequest(
        from_currency="USD", to_currency="BRL", value=100, user_id=10
    )
    with pytest.raises(FailToParseException):
        service.calculate_transaction(data)


@patch("service.TransactionRepository", return_value=MagicMock())
@patch("service.Config", return_value=MagicMock())
def test_should_raise_exception_when_use_wrong_api_key(
    repository: MagicMock, config: MagicMock
) -> None:
    config.CURRENCY_API_KEY = ""
    with pytest.raises(CurrencyAPIException):
        TransactionService()


@patch("service.TransactionRepository", return_value=MagicMock())
@patch("service.Client", return_value=MagicMock())
def test_should_build_transaction(client: MagicMock, repository: MagicMock) -> None:
    service = TransactionService()
    service._repository.persist = MagicMock()
    data = TransactionRequest(
        from_currency="USD", to_currency="BRL", value=100, user_id=10
    )
    transaction = service._build(data, 5.5748607533, 557.4860753300001)
    assert transaction.user_id == 10
    assert service._repository.persist.called
    assert service._repository.persist.call_args_list == [call(transaction)]


@patch("service.TransactionRepository", return_value=MagicMock())
@patch("service.Client", return_value=MagicMock())
def test_should_call_repository(client: MagicMock, repository: MagicMock) -> None:
    service = TransactionService()
    service._repository.find_transactions_by_user_id = MagicMock()
    service.get_transactions_by_user_id(11)
    assert service._repository.find_transactions_by_user_id.called
    assert service._repository.find_transactions_by_user_id.call_args_list == [call(11)]
