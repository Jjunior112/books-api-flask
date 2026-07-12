from auth.password_service import PasswordService

from services.user_service import UserService

from exceptions import (
    InvalidCredentialsException
)
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
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


        access_token = create_access_token(
            identity=str(user.id),
            additional_claims={
                "name": user.name,
                "email": user.email
            }
        )

        refresh_token = create_refresh_token(
            identity=str(user.id)
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }