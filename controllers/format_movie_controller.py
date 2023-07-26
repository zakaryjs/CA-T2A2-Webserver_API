from init import db
from flask import Blueprint
from models.format_movie import FormatMovie, formatmovies_schema, formatsmovies_schema

movieformats_bp = Blueprint('movie_formats', __name__, url_prefix='/movie_formats')

movieformats_bp.route('/')
def get_all_movie_formats():
    '''/formats GET route displays all formats to the user'''
    stmt = db.select(FormatMovie).order_by(FormatMovie.id.desc()) # filters the database to formats, in descending order
    formats = db.session.scalars(stmt)
    return formatsmovies_schema.dump(formats) # returns the formats to the user