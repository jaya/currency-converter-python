from fastapi import FastAPI

from service import CurrencyService
from validators import Convert

app = FastAPI()


@app.post("/convert/")
async def convert(data: Convert):
    service = CurrencyService()
    transaction = service.calculate_transaction(data)
    service.persist(transaction)
    return {
        "transaction_id": transaction.id,
        "user_id": transaction.user_id,
        "from_currency": transaction.from_currency,
        "to_currency": transaction.to_currency,
        "from_value": data.value,
        "to_value": transaction.value,
        "rate": transaction.rate,
        "timestamp": transaction.timestamp,
    }
