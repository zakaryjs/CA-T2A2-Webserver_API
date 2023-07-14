from init import db
from flask import Blueprint, request
from models.movie import Movie, movie_schema, movies_schema
from models.user import User
from flask_jwt_extended import get_jwt_identity, jwt_required
from controllers.book_controller import authorise_admin

movies_bp = Blueprint('movies', __name__, url_prefix='/movies')

@movies_bp.route('/')
def get_all_movies():
    stmt = db.select(Movie).order_by(Movie.id.desc())
    movies = db.session.scalars(stmt)
    return movies_schema.dump(movies)

@movies_bp.route('/<int:id>')
def get_one_movie(id):
    stmt = db.select(Movie).filter_by(id=id)
    movie = db.session.scalar(stmt)
    if movie:
        return movie_schema.dump(movie)
    else:
        return {'error': f'A movie with the id {id} does not exist.'}, 404
    
@movies_bp.route('/', methods=['POST'])
@jwt_required
def create_movie():
    json_data = movie_schema.load(request.get_json)
    movie = Movie(
        title=json_data.get('title'),
        genre=json_data.get('genre'),
        run_time=json_data.get('run_time'),
        format=json_data.get('format'),
        user_id=get_jwt_identity()
    )
    db.session.add(movie)
    db.session.commit()
    return movie_schema.dump(movie), 201