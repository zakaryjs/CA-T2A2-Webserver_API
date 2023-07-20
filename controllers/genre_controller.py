from init import db
from flask import Blueprint
from models.genre import Genre, genre_schema, genres_schema

genres_bp = Blueprint('genres', __name__, url_prefix='/genres')

@genres_bp.route('/')
def get_all_genres():
    stmt = db.select(Genre).order_by(Genre.id.desc())
    genres = db.session.scalars(stmt)
    return genres_schema.dump(genres)

@genres_bp.route('<int:id>')
def get_one_genre(id):
    stmt = db.select(Genre).filter_by(id=id)
    genre = db.session.scalar(stmt)
    if genre:
        return genre_schema.dump(genre)
    else: return {'error': f'A genre with the id {id} does not exist.'}