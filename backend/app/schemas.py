from pydantic import BaseModel
from datetime import datetime

class ConversionRequest(BaseModel):
    user_id: str
    from_currency: str
    to_currency: str
    amount: float

class TransactionOut(BaseModel):
    id: int
    user_id: str
    from_currency: str
    to_currency: str
    amount: float
    converted_amount: float
    conversion_rate: float
    timestamp: datetime

    class Config:
        orm_mode = True
