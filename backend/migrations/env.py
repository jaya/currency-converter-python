# migrations/env.py
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
import asyncio
from alembic import context
import os
import sys

# Adicione o path do seu projeto
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.currency_converter.db.session import Base
from src.currency_converter.db.models import ConversionTransaction

# Configuração do Alembic
config = context.config
fileConfig(config.config_file_name)

target_metadata = Base.metadata

def do_run_migrations(connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,
        compare_server_default=True
    )

    with context.begin_transaction():
        context.run_migrations()

async def run_async_migrations():
    connectable = create_async_engine(
        os.getenv("DATABASE_URL"),
        echo=True
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

if context.is_offline_mode():
    do_run_migrations(context.connection)
else:
    asyncio.run(run_async_migrations())
