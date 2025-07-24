from pydantic import BaseModel
from datetime import datetime
from typing import List

class TransactionBase(BaseModel):
    user_id: str
    from_currency: str
    to_currency: str
    from_value: float
    to_value: float
    rate: float

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    timestamp: datetime
    
    class Config:
        orm_mode = True

class TransactionListResponse(BaseModel):
    transactions: List[Transaction]