from fastapi import APIRouter,HTTPException
from src.books.book_data import books
from src.books.schemas import Book,UpdateBook
from typing import List

book_router=APIRouter()

@book_router.get('/',response_model=List[Book])
async def get_books():
    return books

@book_router.get('/{book_id}')
async def get_book_by_id(book_id:int)->dict:
    for book in books:
        if book['id']==book_id:
            return book
        
    raise HTTPException(status_code=404,detail='Book not found')

@book_router.post('/')
async def create_book(book:Book):
    new_book=book.model_dump()
    books.append(new_book)

    return new_book

@book_router.put('/book_id}')
async def update_book(book_id:int,book:UpdateBook)->dict:
    for book in books:
        if book['id']==book_id:
            book['title']=book.title
            book['author']=book.author
            book['publisher']=book.publisher
            book['published_date']=book.published_date
            book['page_count']=book.page_count
            book['language']=book.language
            
            return book
    raise HTTPException(status_code=404,detail='book not found')


@book_router.delete('/{book_id}')
async def delete_book(book_id:int)->dict:
    for i,book in enumerate(books):
        if book['id']==book_id:
            books.pop(i)

            return {'message':'Book deleted!'}
    
    raise HTTPException(status_code=404,detail='book not found')