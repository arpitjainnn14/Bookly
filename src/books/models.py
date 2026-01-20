from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
import uuid

class Book(SQLModel, table=True):
    __tablename__ = 'book'

    uid: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, nullable=False)
    title: str
    author: str
    publisher: str
    published_date: datetime
    page_count: int
    language: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc).replace(tzinfo=None))

    def __repr__(self) -> str:
        return f"<Book {self.title}>"