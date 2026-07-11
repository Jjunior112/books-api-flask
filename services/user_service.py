from database.database import db
from models.user import User


class UserService:

    def create(self, data):

        user = User(
            name=data["name"],
            email=data["email"],
            password=data["password"]
        )

        db.session.add(user)
        db.session.commit()

        return user