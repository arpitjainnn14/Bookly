from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlmodel import SQLModel

from src.config import config
from src.books.models import Book  # Import models so SQLModel knows about them

async_engine = create_async_engine(
    url=config.DATABASE_URL,
    echo=True
)

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)