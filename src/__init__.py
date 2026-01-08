from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db

#DB is ready before the traffic hits
@asynccontextmanager
async def life_span(app:FastAPI):
    print('Server is starting...')
    await init_db() #using await becuase init_db is an async function
    yield
    print('Server has been stopped...')


version='v1'

app=FastAPI(
    title='Bookly App',
    description='My first FastAPI Project service',
    version=version,
    lifespan=life_span
)

app.include_router(book_router,prefix=f'/api/{version}/books',tags=['Books'])

