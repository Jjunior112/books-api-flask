from flask import Blueprint, jsonify, request
from schemas.mapper import book_to_response
from services.book_service import BookService
from schemas import BookRequest
from flask import request


book_bp = Blueprint(
    "books",
    __name__,
    url_prefix="/books"
)

service = BookService()

@book_bp.get("")
def find_all():

    page = request.args.get(
        "page",
        default=1,
        type=int
    )

    size = request.args.get(
        "size",
        default=10,
        type=int
    )


    title = request.args.get(
        "title"
    )

    author = request.args.get(
        "author"
    )


    pagination = service.find_all(
        page,
        size,
        title,
        author
    )


    books = [
        book_to_response(book)
        for book in pagination.items
    ]


    return {
        "content": [
            book.model_dump()
            for book in books
        ],
        "page": page,
        "size": size,
        "total_elements": pagination.total,
        "total_pages": pagination.pages
    }

@book_bp.get("/<int:book_id>")
def find_by_id(book_id):

    book = service.find_by_id(book_id)

    response = book_to_response(book)

    return response.model_dump()

@book_bp.post("")
def create():

    data = BookRequest(**request.get_json())

    book = service.create(
        data.model_dump()
    )

    response = book_to_response(book)


    return response.model_dump(), 201

@book_bp.put("/<int:book_id>")
def update(book_id):

    data = BookRequest(**request.get_json())

    book = service.update(
        book_id,
        data.model_dump()
    )

    if book is None:
        return {"message": "Book not found"}, 404

    return jsonify({
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "pages": book.pages
    })

@book_bp.delete("/<int:book_id>")
def delete(book_id):

    deleted = service.delete(book_id)

    if not deleted:
        return {"message": "Book not found"}, 404

    return "", 204