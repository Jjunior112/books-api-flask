from pydantic import BaseModel, Field


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