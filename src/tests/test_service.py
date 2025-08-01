import pytest
from unittest.mock import patch, MagicMock, call

from exceptions import CurrencyAPIException, FailToParseException
from service import TransactionService, get_exchanges
from validators import TransactionRequest


@patch("service.TransactionRepository", return_value=MagicMock())
def test_calculate_transaction(transaction_repository: MagicMock, exchanges) -> None:
    service = TransactionService(MagicMock())
    service._build = MagicMock()
    data = TransactionRequest(
        from_currency="USD", to_currency="BRL", value=100, user_id=10
    )
    service.calculate_transaction(data, exchanges)
    assert service._build.call_args_list == [
        call(data, 5.5748607533, 557.4860753300001)
    ]


@patch("service.TransactionRepository", return_value=MagicMock())
def test_should_raise_exception_when_calculation_fails(repository: MagicMock) -> None:
    service = TransactionService(MagicMock())
    service._build = MagicMock()
    data = TransactionRequest(
        from_currency="USD", to_currency="BRL", value=100, user_id=10
    )
    with pytest.raises(FailToParseException):
        service.calculate_transaction(data, {})


@patch("service.Config", return_value=MagicMock())
def test_should_raise_exception_when_use_wrong_api_key(config: MagicMock) -> None:
    config.CURRENCY_API_KEY = ""
    with pytest.raises(CurrencyAPIException):
        get_exchanges()


@patch("service.TransactionRepository", return_value=MagicMock())
def test_should_build_transaction(repository: MagicMock) -> None:
    service = TransactionService(MagicMock())
    service._repository.persist = MagicMock()
    data = TransactionRequest(
        from_currency="USD", to_currency="BRL", value=100, user_id=10
    )
    transaction = service._build(data, 5.5748607533, 557.4860753300001)
    assert transaction.user_id == 10
    assert service._repository.persist.called
    assert service._repository.persist.call_args_list == [call(transaction)]


@patch("service.TransactionRepository", return_value=MagicMock())
def test_should_call_repository(repository: MagicMock) -> None:
    service = TransactionService(MagicMock())
    service._repository.find_transactions_by_user_id = MagicMock()
    service.get_transactions_by_user_id(11)
    assert service._repository.find_transactions_by_user_id.called
    assert service._repository.find_transactions_by_user_id.call_args_list == [call(11)]
