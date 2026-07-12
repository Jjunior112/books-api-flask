class BookNotFoundException(Exception):

    def __init__(self, book_id):

        self.book_id = book_id

        super().__init__(f"Book {book_id} not found")

class InvalidSortFieldException(Exception):

    def __init__(self, field):

        self.field = field

        super().__init__(
            f"Invalid sort field: {field}"
        )

class InvalidCredentialsException(Exception):

    def __init__(self):

        super().__init__(
            "Invalid email or password"
        )
        
class UserAlreadyExistsException(Exception):

    def __init__(self, email: str):

        self.email = email

        super().__init__(
            f"User with email '{email}' already exists."
        )