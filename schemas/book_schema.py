from pydantic import BaseModel, Field
from datetime import datetime


class BookRequest(BaseModel):

    title: str = Field(
        min_length=1,
        max_length=150
    )

    author: str = Field(
        min_length=1,
        max_length=150
    )

    pages: int = Field(
        gt=0
    )


class BookResponse(BaseModel):

    id: int
    title: str
    author: str
    pages: int
    created_at: datetime

    class Config:
        from_attributes = True