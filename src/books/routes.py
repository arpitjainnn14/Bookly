from fastapi import APIRouter, HTTPException, Depends
from typing import List
from uuid import UUID
from sqlmodel.ext.asyncio.session import AsyncSession

from .crud import BookService
from src.books.schemas import Book as BookSchema, UpdateBook, CreateBook
from src.db.main import get_session


book_router = APIRouter()
book_service = BookService()


@book_router.get('/', response_model=List[BookSchema])
async def get_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books


@book_router.get('/{book_uid}', response_model=BookSchema)
async def get_book_by_id(book_uid: UUID, session: AsyncSession = Depends(get_session)):
    book = await book_service.get_book_by_id(session, book_uid)
    if book:
        return book
    raise HTTPException(status_code=404, detail='book not found')


@book_router.post('/', response_model=BookSchema)
async def create_book(book: CreateBook, session: AsyncSession = Depends(get_session)):
    new_book = await book_service.create_book(book, session)
    return new_book


@book_router.put('/{book_uid}', response_model=BookSchema)
async def update_book(book_uid: UUID, book: UpdateBook, session: AsyncSession = Depends(get_session)):
    updated_book = await book_service.update_book(session, book_uid, book)
    if updated_book:
        return updated_book
    raise HTTPException(status_code=404, detail='book not found')


@book_router.delete('/{book_uid}')
async def delete_book(book_uid: UUID, session: AsyncSession = Depends(get_session)) -> dict:
    deleted = await book_service.delete_book(session, book_uid)
    if deleted:
        return {'message': 'book deleted successfully!'}
    raise HTTPException(status_code=404, detail='book not found')