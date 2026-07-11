import bcrypt


class PasswordService:

    @staticmethod
    def hash_password(password: str) -> str:

        password_bytes = password.encode("utf-8")

        salt = bcrypt.gensalt()

        hashed = bcrypt.hashpw(
            password_bytes,
            salt
        )

        return hashed.decode("utf-8")


    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:

        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )