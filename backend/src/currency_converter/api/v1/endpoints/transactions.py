from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from ....schemas.conversion import TransactionResponse
from ....db.session import get_db
from ....db.repositories import ConversionRepository
from ....services.conversion import ConversionService

router = APIRouter()

@router.get("/", response_model=List[TransactionResponse])
async def get_user_transactions(
    user_id: str,
    db: AsyncSession = Depends(get_db)
):
    try:
        service = ConversionService(ConversionRepository(db))
        transactions = await service.get_user_transactions(user_id)
        return [
            {
                "id": t.id,
                "user_id": t.user_id,
                "from_currency": t.from_currency,
                "to_currency": t.to_currency,
                "from_value": float(t.from_value),
                "to_value": float(t.to_value),
                "rate": float(t.rate),
                "timestamp": t.timestamp
            }
            for t in transactions
        ]
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch transactions: {str(e)}"
        )
