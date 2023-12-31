from flask import Flask
import os
from init import db, ma, bcrypt, jwt
from controllers.cli_controller import database_commands
from controllers.auth_controller import authentication_blueprint
from controllers.book_controller import books_bp
from controllers.collection_controller import collections_bp
from controllers.movie_controller import movies_bp
from controllers.genre_controller import genres_bp
from controllers.format_controller import formats_bp
from controllers.format_movie_controller import movieformats_bp

def create_app():
    app = Flask(__name__)

    app.json.sort_keys = False

    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(database_commands)
    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(books_bp)
    app.register_blueprint(collections_bp)
    app.register_blueprint(movies_bp)
    app.register_blueprint(genres_bp)
    app.register_blueprint(formats_bp)
    app.register_blueprint(movieformats_bp)

    return app