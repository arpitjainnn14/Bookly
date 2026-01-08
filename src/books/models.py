from sqlmodel import SQLModel,Field,Column
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime
import uuid

class Book(SQLModel,table=True):
    __tablename__='book'
    
    uid:uuid.UUID=Field(sa_column=Column(pg.UUID, default=uuid.uuid4(),primary_key=True,nullable=False))
    title:str
    author:str
    publisher:str
    published_date:str
    page_count:int
    language:str
    created_at:datetime=Field(Column(pg.TIMESTAMP,default=datetime.now))
    updated_at:datetime=Field(Column(pg.TIMESTAMP,default=datetime.now))


def __repr(self):
    return f"<Book {self.title}>"