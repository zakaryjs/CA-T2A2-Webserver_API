from init import db
from flask import Blueprint, request
from models.format import Format, format_schema, formats_schema
from flask_jwt_extended import get_jwt_identity, jwt_required
from controllers.book_controller import authorise_admin

formats_bp = Blueprint('formats', __name__, url_prefix='/formats')

@formats_bp.route('/')
def get_all_formats():
    '''/formats GET route displays all formats to the user'''
    stmt = db.select(Format).order_by(Format.id.desc()) # filters the database to formats, in descending order
    formats = db.session.scalars(stmt)
    return formats_schema.dump(formats) # returns the formats to the user

@formats_bp.route('/<int:id>')
def get_one_format(id):
    '''/formats/id GET route displays format to user based on the requested ID'''
    stmt = db.select(Format).filter_by(id=id) # filters the database to formats, by the requested ID
    format = db.session.scalar(stmt)
    if format:
        return format_schema.dump(format) # if format with that ID is found, return the format
    else:
        return {'error': f'A format with the id {id} does not exist.'} # if format with that ID is not found, return this error message
    
@formats_bp.route('/', methods=['POST'])
@jwt_required()
def create_format():
    '''/genres POST route that will receive JSON with fields {format}'''
    json_data = format_schema.load(request.get_json())
    format = Format(
        format=json_data.get('format')
    )
    db.session.add(format)
    db.session.commit()
    return format_schema.dump(format), 201

@formats_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_format(id):
    '''/formats/id DELETE route that will use the ID in the URL to locate the format, verify the user as admin and then remove the format from the database'''
    admin_status = authorise_admin()
    if not admin_status:
        return {'error': 'You must have admin permissions to delete formats.'} # if not admin return this error message
    stmt = db.select(Format).filter_by(id=id)
    format = db.session.scalar(stmt)
    if format:
        db.session.delete(format)
        db.session.commit()
        return {'message': f'Format {format.id} has been deleted succesfully.'} # if format is found, return this message
    else:
        return {'error': f'A format with the id {id} does not exist.'}, 404 # if format is not found, return this error message
    
@formats_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_format(id):
    '''/formats/id PUT/PATCH route that will use the ID in the URL in order to find the format, and then allow the user to update details of the format'''
    json_data = format_schema.load(request.get_json(), partial=True)
    stmt = db.select(Format).filter_by(id=id)
    format = db.session.scalar(stmt)
    if format:
        format.format = json_data.get('format') or format.format
        return format_schema.dump(format)
    else:
        return {'error': f'A format with the id {id} does not exist.'}, 404 # if format is not found return this error message