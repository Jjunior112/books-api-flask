from .book_schema import BookResponse
from .user_schema import UserResponse


def book_to_response(book):

    return BookResponse.model_validate(book)


def user_to_response(user):

    return UserResponse.model_validate(user)