from sqlalchemy import Column, Integer, String, Numeric, DateTime
from sqlalchemy.sql import func
from .session import Base

class ConversionTransaction(Base):
    __tablename__ = "conversion_transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    from_currency = Column(String(3))
    to_currency = Column(String(3))
    from_value = Column(Numeric(10, 2))
    to_value = Column(Numeric(10, 2))
    rate = Column(Numeric(10, 6))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
