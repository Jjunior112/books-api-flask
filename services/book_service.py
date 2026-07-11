from models.book import Book
from database.database import db
from exceptions import BookNotFoundException

class BookService:

    def find_all(self, page, size):

        query = Book.query

        pagination = query.paginate(
            page=page,
            per_page=size,
            error_out=False
        )

        return pagination
    
    def find_by_id(self, book_id):

        book = db.session.get(Book, book_id)

        if book is None:
            raise BookNotFoundException(book_id)

        return book

    def create(self, data):

        book = Book(
            title=data["title"],
            author=data["author"],
            pages=data["pages"]
        )

        db.session.add(book)
        db.session.commit()

        return book

    def update(self, book_id, data):

        book = db.session.get(Book, book_id)

        if book is None:
            raise BookNotFoundException(book_id)

        book.title = data["title"]
        book.author = data["author"]
        book.pages = data["pages"]

        db.session.commit()

        return book

    def delete(self, book_id):

        book = db.session.get(Book, book_id)

        if book is None:
            raise BookNotFoundException(book_id)

        db.session.delete(book)
        db.session.commit()

        return True