from flask import jsonify

from pydantic import ValidationError

from exceptions.custom_exceptions import BookNotFoundException

from exceptions.custom_exceptions import InvalidCredentialsException

def register_error_handlers(app):

    @app.errorhandler(BookNotFoundException)
    def handle_book_not_found(error):

        return jsonify({
            "message": str(error)
        }), 404


    @app.errorhandler(ValidationError)
    def handle_validation(error):

        errors = []

        for err in error.errors():

            errors.append({
                "field": ".".join(map(str, err["loc"])),
                "message": err["msg"]
            })

        return jsonify({
            "message": "Validation error",
            "errors": errors
        }), 400


    @app.errorhandler(Exception)
    def handle_internal(error):

        print(error)

        return jsonify({
            "message": "Internal server error"
        }), 500
    @app.errorhandler(
    InvalidCredentialsException
    )
    def handle_invalid_credentials(error):

        return {
            "message": str(error)
        }, 401