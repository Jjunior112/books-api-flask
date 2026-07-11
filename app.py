from flask import Flask
from flask_migrate import Migrate

from config import Config
from database.database import db

from models import book

from routes.book_routes import book_bp
from exceptions import register_error_handlers


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    Migrate(app, db)

    app.register_blueprint(book_bp)

    register_error_handlers(app)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)