import pytest
from decimal import Decimal
from unittest.mock import AsyncMock
from src.currency_converter.services.conversion import ConversionService
from src.currency_converter.services.currency_api import CurrencyAPIService

@pytest.mark.asyncio
async def test_convert_currency_success():
    mock_repo = AsyncMock()
    mock_repo.create_transaction.return_value = AsyncMock(id=1)
    
    mock_api = AsyncMock()
    mock_api.get_exchange_rates.return_value = {
        "BRL": {"value": 5.2},
        "EUR": {"value": 0.85}
    }
    
    service = ConversionService(mock_repo)
    service.currency_api = mock_api
    
    result = await service.convert_currency(
        user_id="test_user",
        from_currency="USD",
        to_currency="BRL",
        amount=Decimal("100")
    )
    
    assert result["converted_amount"] == Decimal("520")
    mock_repo.create_transaction.assert_called_once()

@pytest.mark.asyncio
async def test_convert_same_currency():
    service = ConversionService(AsyncMock())
    with pytest.raises(ValueError, match="same currencies"):
        await service.convert_currency(
            user_id="test_user",
            from_currency="USD",
            to_currency="USD",
            amount=Decimal("100")
        )