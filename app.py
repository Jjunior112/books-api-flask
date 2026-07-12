from flask import Flask, app
from flask_migrate import Migrate

from config import Config
from database.database import db

from models import book

from routes.book_routes import book_bp
from routes.user_routes import user_bp
from routes.auth_routes import auth_bp
from exceptions import register_error_handlers
from flask_jwt_extended import JWTManager


def create_app():

    app = Flask(__name__)
    
    jwt = JWTManager()
    
    app.config.from_object(Config)
    

    db.init_app(app)

    jwt.init_app(app)

    Migrate(app, db)

    app.register_blueprint(book_bp)

    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    register_error_handlers(app)

    return app
    
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)