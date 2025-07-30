import os
import httpx
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CURRENCY_API_KEY")
BASE_URL = "https://api.currencyapi.com/v3/latest"


def get_conversion_rate(from_currency: str, to_currency: str) -> float:
    params = {
        "apikey": API_KEY,
        "base_currency": from_currency,
        "currencies": to_currency,
    }
    response = httpx.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Erro na API de câmbio")

    data = response.json()
    try:
        return data["data"][to_currency]["value"]
    except KeyError:
        raise HTTPException(status_code=400, detail="Moeda inválida")


def convert_and_record(request: schemas.ConversionRequest, db: Session):
    rate = get_conversion_rate(request.from_currency, request.to_currency)
    converted_amount = request.amount * rate

    transaction = models.Transaction(
        user_id=request.user_id,
        from_currency=request.from_currency,
        to_currency=request.to_currency,
        amount=request.amount,
        converted_amount=converted_amount,
        conversion_rate=rate,
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


def get_user_transactions(user_id: str, db: Session):
    return db.query(models.Transaction).filter_by(user_id=user_id).all()
