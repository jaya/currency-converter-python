from fastapi import APIRouter, Depends, HTTPException
from decimal import Decimal
from ....schemas.conversion import ConversionRequest, ConversionResponse
from ....services.conversion import ConversionService
from ....db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/convert", response_model=ConversionResponse)
async def convert_currency(
    request: ConversionRequest,
    db: Session = Depends(get_db)
):
    try:
        service = ConversionService(ConversionRepository(db))
        result = await service.convert_currency(
            user_id=request.user_id,
            from_currency=request.from_currency,
            to_currency=request.to_currency,
            amount=Decimal(str(request.amount))
        )
        return {
            "transaction_id": result["transaction_id"],
            "user_id": request.user_id,
            "from_currency": request.from_currency,
            "to_currency": request.to_currency,
            "from_value": float(request.amount),
            "to_value": float(result["converted_amount"]),
            "rate": float(result["rate"])
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
