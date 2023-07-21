from init import db
from flask import Blueprint
from models.genre import Genre, genre_schema, genres_schema

genres_bp = Blueprint('genres', __name__, url_prefix='/genres')

@genres_bp.route('/')
def get_all_genres():
    '''/genres GET route displays all genres to the user'''
    stmt = db.select(Genre).order_by(Genre.id.desc()) # filters the database to genres, in descending order
    genres = db.session.scalars(stmt)
    return genres_schema.dump(genres) # returns the genres to the user

@genres_bp.route('<int:id>')
def get_one_genre(id):
    '''/genres/id GET route displays genre to user based on the requested ID'''
    stmt = db.select(Genre).filter_by(id=id) # filters the database to genres, by the requested ID
    genre = db.session.scalar(stmt)
    if genre:
        return genre_schema.dump(genre) # if genre with that ID is found, return the genre
    else:
        return {'error': f'A genre with the id {id} does not exist.'} # if genre with that ID is not found, return this error message