from fastapi import APIRouter
from .endpoints import conversion, transactions

api_router = APIRouter()

api_router.include_router(
    conversion.router,
    prefix="/conversion",
    tags=["conversion"]
)
api_router.include_router(
    transactions.router,
    prefix="/transactions",
    tags=["transactions"]
)