from init import db
from flask import Blueprint
from models.format import Format, format_schema, formats_schema

formats_bp = Blueprint('formats', __name__, url_prefix='/formats')

@formats_bp.route('/')
def get_all_formats():
    stmt = db.select(Format).order_by(Format.id.desc())
    formats = db.session.scalars(stmt)
    return formats_schema.dump(formats)

@formats_bp.route('/<int:id>')
def get_one_format(id):
    stmt = db.select(Format).filter_by(id=id)
    format = db.session.scalar(stmt)
    if format:
        return format_schema.dump(format)
    else:
        return {'error': f'A format with the id {id} does not exist.'}