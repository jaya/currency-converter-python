from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .models import ConversionTransaction
from typing import List

class ConversionRepository:
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def create_transaction(
        self,
        user_id: str,
        from_currency: str,
        to_currency: str,
        from_value: float,
        to_value: float,
        rate: float
    ) -> ConversionTransaction:
        transaction = ConversionTransaction(
            user_id=user_id,
            from_currency=from_currency,
            to_currency=to_currency,
            from_value=from_value,
            to_value=to_value,
            rate=rate
        )
        self.session.add(transaction)
        await self.session.commit()
        await self.session.refresh(transaction)
        return transaction
    
    async def get_transactions_by_user(self, user_id: str) -> List[ConversionTransaction]:
        result = await self.session.execute(
            select(ConversionTransaction)
            .where(ConversionTransaction.user_id == user_id)
            .order_by(ConversionTransaction.timestamp.desc())
        )
        return result.scalars().all()