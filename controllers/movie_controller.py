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
@jwt_required()
def create_movie():
    json_data = movie_schema.load(request.get_json())
    movie = Movie(
        title=json_data.get('title'),
        genre_id=json_data.get('genre_id'),
        run_time=json_data.get('run_time'),
        format_id=json_data.get('format_id'),
        collection_id=json_data.get('collection_id'),
        user_id=get_jwt_identity()
    )
    db.session.add(movie)
    db.session.commit()
    return movie_schema.dump(movie), 201

@movies_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_movie(id):
    admin_status = authorise_admin
    if not admin_status:
        return {'error': 'You must have admin permissions to delete movies.'}
    stmt = db.select(Movie).filter_by(id)
    movie = db.session.scalar(stmt)
    if movie:
        return {'error': f'Movie {movie.title} has been deleted succesfully.'}
    else:
        return {'error': f'A movie with the id {id} does not exist.'}, 404
    
@movies_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_movie(id):
    json_data = movie_schema.load(request.get_json(), partial=True)
    stmt = db.select(Movie).filter_by(id=id)
    movie = db.session.scalar(stmt)
    if movie:
        if str(movie.user_id) != get_jwt_identity():
            return {'error': 'You must be the owner of the movie in order to edit it.'}, 403
        movie.title = json_data.get('title') or movie.title
        movie.genre = json_data.get('genre') or movie.genre
        movie.run_time = json_data.get('run_time') or movie.run_time
        movie.format = json_data.get('format') or movie.format
        return movie_schema.dump(movie)
    else:
        return {'error': f'A movie with the id {id} does not exist.'}, 404