from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ConversionRequest(BaseModel):
    user_id: str
    from_currency: str = Field(..., min_length=3, max_length=3)
    to_currency: str = Field(..., min_length=3, max_length=3)
    amount: float = Field(..., gt=0)

class ConversionResponse(BaseModel):
    transaction_id: int
    user_id: str
    from_currency: str
    to_currency: str
    from_value: float
    to_value: float
    rate: float
    timestamp: Optional[datetime] = None

class TransactionResponse(BaseModel):
    id: int
    user_id: str
    from_currency: str
    to_currency: str
    from_value: float
    to_value: float
    rate: float
    timestamp: datetime