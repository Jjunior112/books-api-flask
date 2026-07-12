from auth.password_service import PasswordService
from database.database import db
from models.user import User
from exceptions import UserAlreadyExistsException


class UserService:

    def create(self, data: dict) -> User:

        existing_user = self.find_by_email(
            data["email"]
        )

        if existing_user:
            raise UserAlreadyExistsException(data["email"])

        hashed_password = PasswordService.hash_password(
            data["password"]
        )

        user = User(
            name=data["name"],
            email=data["email"],
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return user


    def find_by_email(
        self,
        email: str
    ) -> User | None:

        return User.query.filter_by(
            email=email
        ).first()


    def find_by_id(
        self,
        user_id: int
    ) -> User | None:

        return db.session.get(User, user_id)