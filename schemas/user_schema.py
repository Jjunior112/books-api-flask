from pydantic import BaseModel, Field, EmailStr
from datetime import datetime


class UserRequest(BaseModel):

    name: str = Field(
        min_length=3,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=100
    )

class UserResponse(BaseModel):

    id: int
    name: str
    email: EmailStr
    created_at: datetime

    model_config = {
        "from_attributes": True
    }