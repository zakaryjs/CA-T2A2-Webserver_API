from init import db
from flask import Blueprint, request
from models.movie import Movie, movie_schema, movies_schema
from models.user import User
from flask_jwt_extended import get_jwt_identity, jwt_required
from controllers.book_controller import authorise_admin

movies_bp = Blueprint('movies', __name__, url_prefix='/movies')

@movies_bp.route('/') # route for viewing all movies in database
def get_all_movies():
    '''/movies GET route that will display a full list of all the movies in the database'''
    stmt = db.select(Movie).order_by(Movie.id.desc()) # select all movies in database and display them in descending order
    movies = db.session.scalars(stmt) # makes movies displayable
    return movies_schema.dump(movies) # returns movies to users

@movies_bp.route('/<int:id>') # route for viewing singular movie in database
def get_one_movie(id):
    '''/movies/id GET route that will display a movie corresponding to the ID in the URL'''
    stmt = db.select(Movie).filter_by(id=id) # search the database with a filter being that of the ID in the URL
    movie = db.session.scalar(stmt) # convert movie to viewable format
    if movie:
        return movie_schema.dump(movie) # return movie to user
    else:
        return {'error': f'A movie with the id {id} does not exist.'}, 404 # if movie not found, return this error message
    
@movies_bp.route('/', methods=['POST'])
@jwt_required()
def create_movie():
    '''/movies POST route that will receive raw JSON with fields {title, genre_id, run_time, format_id and collection_id} before being validated and then added to database'''
    json_data = movie_schema.load(request.get_json()) # gets the JSON from user
    movie = Movie( # creates new instance of movie
        title=json_data.get('title'),
        genre_id=json_data.get('genre_id'),
        run_time=json_data.get('run_time'),
        format_id=json_data.get('format_id'),
        collection_id=json_data.get('collection_id'),
        user_id=get_jwt_identity() # attaches jwt identity to book for verification
    )
    db.session.add(movie) # adds movie to session
    db.session.commit() # commits movie to database
    return movie_schema.dump(movie), 201 # returns movie to user

@movies_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_movie(id):
    '''/movies/id DELETE route that will use the ID in the URL to locate the movie, verify the user as admin and then remove the movie from the database'''
    admin_status = authorise_admin() # authorise_admin function checks whether user has admin permissions
    if not admin_status:
        return {'error': 'You must have admin permissions to delete movies.'} # if not admin return this error message
    stmt = db.select(Movie).filter_by(id=id) # filter movies by the id to find specific movie
    movie = db.session.scalar(stmt)
    if movie:
        db.session.delete(movie)
        db.session.commit()
        return {'error': f'Movie {movie.title} has been deleted succesfully.'} # if movie has been found and user has admin permissions, drop movie from database
    else:
        return {'error': f'A movie with the id {id} does not exist.'}, 404 # if movie not found return this error message
    
@movies_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_movie(id):
    '''/movies/id PUT/PATCH route that will use the ID in the URL in order to find the movie, verify the user as the owner of the movie, and then allow the user to update details of the movie'''
    json_data = movie_schema.load(request.get_json(), partial=True) # loads schema for movie, uses partial tag as not all details may be updated
    stmt = db.select(Movie).filter_by(id=id) # filter movies by the id to find specific book
    movie = db.session.scalar(stmt)
    if movie:
        if str(movie.user_id) != get_jwt_identity():
            return {'error': 'You must be the owner of the movie in order to edit it.'}, 403  # if movie is found and user ID does not match the jwt, return this error message
        movie.title = json_data.get('title') or movie.title
        movie.genre = json_data.get('genre') or movie.genre
        movie.run_time = json_data.get('run_time') or movie.run_time
        movie.format = json_data.get('format') or movie.format
        return movie_schema.dump(movie) # return edited movie to user
    else:
        return {'error': f'A movie with the id {id} does not exist.'}, 404 # if movie is not found return this error message