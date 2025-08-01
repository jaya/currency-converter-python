from typing import List

from fastapi import FastAPI, Request
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from database import get_session
from exceptions import BaseCustomException
from logger import CustomLogger
from service import TransactionService
from validators import TransactionRequest, TransactionResponse

logger = CustomLogger().get_logger()
app = FastAPI()


@app.exception_handler(BaseCustomException)
async def exception_handler(request: Request, exc: BaseCustomException):
    status_code = exc.status_code
    message = exc.message
    return JSONResponse(status_code=status_code, content={"message": message})


@app.post("/transactions")
async def create_transaction(
    data: TransactionRequest, session: Session = Depends(get_session)
) -> TransactionResponse:
    service = TransactionService(session)
    transaction = service.calculate_transaction(data)
    date = transaction.timestamp.strftime("%Y-%m-%dT%H:%M:%S%z")
    response = TransactionResponse(
        transaction_id=transaction.id,
        user_id=transaction.user_id,
        from_currency=transaction.from_currency,
        to_currency=transaction.to_currency,
        from_value=data.value,
        to_value=transaction.to_value,
        rate=transaction.rate,
        timestamp=date,
    )
    return response


@app.get("/transactions")
async def get_transactions(
    user_id: int, session: Session = Depends(get_session)
) -> List[TransactionResponse]:
    service = TransactionService(session)
    response = []
    transactions = service.get_transactions_by_user_id(user_id)
    for transaction in transactions:
        transaction = transaction[0]
        logger.info(transaction)
        date = transaction.timestamp.strftime("%Y-%m-%dT%H:%M:%S%z")
        response.append(
            TransactionResponse(
                transaction_id=transaction.id,
                user_id=transaction.user_id,
                from_currency=transaction.from_currency,
                to_currency=transaction.to_currency,
                from_value=transaction.from_value,
                to_value=transaction.to_value,
                rate=transaction.rate,
                timestamp=date,
            )
        )
    return response
