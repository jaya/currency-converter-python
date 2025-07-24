from loguru import logger
import sys

def configure_logging():
    logger.remove()
    logger.add(
        sys.stdout,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        level="INFO",
        backtrace=True,
        diagnose=True
    )
    logger.add(
        "logs/currency_converter.log",
        rotation="10 MB",
        retention="30 days",
        level="DEBUG",
        enqueue=True
    )