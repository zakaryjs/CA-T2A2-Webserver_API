from init import db
from flask import Blueprint
from models.format import Format, format_schema, formats_schema

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