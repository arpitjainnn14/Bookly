from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def read_root():
    return {'message':'Hello,world!'}


#Path parameter
@app.get("/greet/{name}")
async def greet(name:str)->dict:
    return {"message": f"Hello, {name}"}

#Query Parameter
@app.get('/welcome')
async def welcome(name:str)->dict:
    return {"message": f"Hello, {name}"}

#using both parameters
@app.get('/info/{name}')
async def information(name:str,age:int)->dict:
    return {
        'message':f'Hello,{name}. You are {age} years old'
    }

#using query parameter with default values
@app.get('/info1/')
async def information(age:Optional[int]=0,name:Optional[str]='user')->dict:
    return {
        'message':f'Hello,{name}. You are {age} years old'
    }


class BookCreate(BaseModel):
    title:str
    author:str
    publisher:str

@app.post('/create_book')
async def create_book(book:BookCreate):
    return {
        'Book Name':book.title,
        'Book Author':book.author,
        'Book Publisher':book.publisher,

        "message":'Book created successfully'
    }


@app.get('/get_headers',status_code=200)
async def get_headers(accept:str=Header(None),content:str=Header(None),user_agent:str=Header(None),host:str=Header(None)):
    request_headers={}

    request_headers['Accept']=accept
    request_headers['Content']=content
    request_headers['User-Agent']=user_agent
    request_headers['Host']=host

    return request_headers