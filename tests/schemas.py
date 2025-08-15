# tests/schemas.py
from pydantic import BaseModel

class PostSchema(BaseModel):
    id: int
    title: str
    body: str
    userId: int
