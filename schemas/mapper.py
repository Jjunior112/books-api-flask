from .book_schema import BookResponse


def book_to_response(book):

    return BookResponse.model_validate(book)