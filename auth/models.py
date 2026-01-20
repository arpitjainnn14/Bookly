from sqlmodel import Field,Column
from pydantic import BaseModel
import uuid

class User(BaseModel):
    __table__ = "user"

    id: uuid.UUID
    
