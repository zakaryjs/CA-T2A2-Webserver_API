from init import db
from flask import Blueprint, request
from models.format_movie import FormatMovie, formatmovies_schema, formatsmovies_schema
from flask_jwt_extended import get_jwt_identity, jwt_required
from controllers.book_controller import authorise_admin

movieformats_bp = Blueprint('movie_formats', __name__, url_prefix='/movie_formats')

movieformats_bp.route('/')
def get_all_movie_formats():
    '''/movie_formats GET route displays all formats to the user'''
    stmt = db.select(FormatMovie).order_by(FormatMovie.id.desc()) # filters the database to formats, in descending order
    formats = db.session.scalars(stmt)
    return formatsmovies_schema.dump(formats) # returns the formats to the user

@movieformats_bp.route('/<int:id>')
def get_one_movie_format(id):
    '''/movie_formats/id GET route displays movie format to user based on the requested ID'''
    stmt = db.select(FormatMovie).filter_by(id=id)
    format = db.session.scalar(stmt)
    if format:
        return formatmovies_schema.dump(format) # if format with that ID is found, return the format
    else:
        return {'error': f'A format with the id {id} does not exist.'} # if format with that ID is not found, return this error message
    
@movieformats_bp.route('/', methods=['POST'])
@jwt_required()
def create_format():
    '''/movie_formats POST route that will receive JSON with fields {format}'''
    json_data = formatmovies_schema.load(request.get_json())
    format = FormatMovie(
        format=json_data.get('format')
    )
    db.session.add(format)
    db.session.commit()
    return formatmovies_schema.dump(format), 201

@movieformats_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_movie_format(id):
    '''/movie_formats/id DELETE route that will use the ID in the URL to locate the movie format, verify the user as admin and then remove the movie format from the database'''
    admin_status = authorise_admin()
    if not admin_status:
        return {'error': 'You must have admin permissions to delete movie formats.'} # if not admin return this error message
    stmt = db.select(FormatMovie).filter_by(id=id)
    format = db.session.scalar(stmt)
    if format:
        db.session.delete(format)
        db.session.commit()
        return {'message': f'Movie format {format.id} has been deleted succesfully.'} # if movie format is found, return this message
    else:
        return {'error': f'A movie format with the id {id} does not exist.'}, 404 # if movie format is not found, return this error message

@movieformats_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_movie_format(id):
    json_data = formatmovies_schema.load(request.get_json(), partial=True)
    stmt = db.select(FormatMovie).filter_by(id=id)
    format = db.session.scalar(stmt)
    if format:
        format.format = json_data.get('format') or format.format
        return formatmovies_schema.dump(format)
    else:
        return {'error': f'A movie format with the id {id} does not exist.'}, 404 # if movie format is not found return this error message