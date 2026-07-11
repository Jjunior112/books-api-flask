from pydantic import BaseModel
from typing import Generic, TypeVar, List


T = TypeVar("T")


class PageResponse(BaseModel, Generic[T]):

    content: List[T]

    page: int
    size: int

    total_elements: int
    total_pages: int