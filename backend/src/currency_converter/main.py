from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from loguru import logger
from .core.logging import configure_logging
from .api.v1.routers import api_router
from .db.session import get_db
from .core.config import settings

configure_logging()

app = FastAPI(
    title="Currency Converter API",
    description="API for converting between currencies and tracking transactions",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health_check(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "healthy"}
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return {"status": "unhealthy"}, 500
