class BookNotFoundException(Exception):

    def __init__(self, book_id):

        self.book_id = book_id

        super().__init__(f"Book {book_id} not found")   