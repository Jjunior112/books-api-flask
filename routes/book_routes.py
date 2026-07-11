from flask import Blueprint, jsonify, request
from services.book_service import BookService
from schemas import BookRequest

book_bp = Blueprint(
    "books",
    __name__,
    url_prefix="/books"
)

service = BookService()


@book_bp.get("")
def find_all():

    books = service.find_all()

    return jsonify([
        {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "pages": book.pages
        }
        for book in books
    ])

@book_bp.get("/<int:book_id>")
def find_by_id(book_id):

    book = service.find_by_id(book_id)

    return jsonify({
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "pages": book.pages
    })

from flask import request

@book_bp.post("")
def create():

    data = BookRequest(**request.get_json())

    book = service.create(data.model_dump())

    return jsonify({
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "pages": book.pages
    }), 201

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