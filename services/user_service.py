from database.database import db
from models.user import User
from auth.password_service import PasswordService


class UserService:

    def create(self, data):

        hashed_password = PasswordService.hash_password(
        data["password"])


        user = User(
            name=data["name"],
            email=data["email"],
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return user