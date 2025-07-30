from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import services, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/convert")
def convert_currency(request: schemas.ConversionRequest, db: Session = Depends(get_db)):
    return services.convert_and_record(request, db)

@router.get("/transactions")
def get_transactions(user_id: str, db: Session = Depends(get_db)):
    return services.get_user_transactions(user_id, db)
