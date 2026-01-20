from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from uuid import UUID
from datetime import datetime, timezone
from .models import Book as BookModel
from .schemas import CreateBook, UpdateBook


class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(BookModel).order_by(desc(BookModel.created_at))
        result = await session.exec(statement)
        return result.all()

    async def get_book_by_id(self, session: AsyncSession, book_uid: UUID):
        statement = select(BookModel).where(BookModel.uid == book_uid)
        result = await session.exec(statement)
        book = result.first()
        return book if book is not None else None

    async def create_book(self, book: CreateBook, session: AsyncSession):
        book_data = book.model_dump()
        # Ensure published_date is naive UTC
        if book_data.get('published_date') and book_data['published_date'].tzinfo is not None:
            book_data['published_date'] = book_data['published_date'].astimezone(timezone.utc).replace(tzinfo=None)
        
        new_book = BookModel(**book_data)
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return new_book

    async def update_book(self, session: AsyncSession, book_uid: UUID, book: UpdateBook):
        book_to_update = await self.get_book_by_id(session, book_uid)
        updated_data = book.model_dump()

        if book_to_update is not None:
            # Ensure published_date is naive UTC
            if updated_data.get('published_date') and updated_data['published_date'].tzinfo is not None:
                updated_data['published_date'] = updated_data['published_date'].astimezone(timezone.utc).replace(tzinfo=None)
            for k, v in updated_data.items():
                setattr(book_to_update, k, v)
            await session.commit()
            await session.refresh(book_to_update)
            return book_to_update
        else:
            return None

    async def delete_book(self, session: AsyncSession, book_uid: UUID) -> bool:
        del_book = await self.get_book_by_id(session, book_uid)
        if del_book is not None:
            await session.delete(del_book)
            await session.commit()
            return True
        else:
            return False
        