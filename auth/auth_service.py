from auth.password_service import PasswordService

from services.user_service import UserService

from exceptions import (
    InvalidCredentialsException
)


class AuthService:

    def __init__(self):

        self.user_service = UserService()


    def login(
            self,
            email,
            password
    ):

        user = self.user_service.find_by_email(
            email
        )

        if user is None:

            raise InvalidCredentialsException()


        valid_password = (
            PasswordService.verify_password(
                password,
                user.password
            )
        )

        if not valid_password:

            raise InvalidCredentialsException()


        return user