from init import db
from flask import Blueprint, request
from models.genre import Genre, genre_schema, genres_schema
from flask_jwt_extended import get_jwt_identity, jwt_required
from controllers.book_controller import authorise_admin

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
    
@genres_bp.route('/', methods=['POST'])
@jwt_required()
def create_genre():
    '''/genres POST route that will receive JSON with fields {genre}'''
    json_data = genre_schema.load(request.get_json())
    genre = Genre(
        genre=json_data.get('genre')
    )
    db.session.add(genre)
    db.session.commit()
    return genre_schema.dump(genre), 201

@genres_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_genre(id):
    '''/genres/id DELETE route that will use the ID in the URL to locate the genre, verify the user as admin and then remove the genre from the database'''
    admin_status = authorise_admin
    if not admin_status:
        return {'error': 'You must have admin permissions to delete genres.'} # if not admin return this error message
    stmt = db.select(Genre).filter_by(id)
    genre = db.session.scalar(stmt)
    if genre:
        db.session.delete(genre)
        db.session.commit()
        return {'message': f'Genre {genre.id} has been deleted succesfully.'} # if genre is found, return this message
    else:
        return {'error': f'A genre with the id {id} does not exist.'}, 404 # if genre is not found, return this error message
    
@genres_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_genre(id):
    json_data = genre_schema.load(request.get_json(), partial=True)
    stmt = db.select(Genre).filter_by(id=id)
    genre = db.session.scalar(stmt)
    if genre:
        genre.genre = json_data.get('genre') or genre.name
        return genre_schema.dump(genre)
    else:
        return {'error': f'A genre with the id {id} does not exist.'}, 404 # if genre is not found return this error message
