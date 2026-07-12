from datetime import datetime

from database.database import db


class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(150),
        nullable=False
    )

    author = db.Column(
        db.String(150),
        nullable=False
    )

    pages = db.Column(
        db.Integer,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    user_id = db.Column(
    db.Integer,
    db.ForeignKey("users.id"),
    nullable=False
    )
    user = db.relationship(
    "User",
    back_populates="books"
    )