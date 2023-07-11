from init import db, bcrypt
from flask import Blueprint, request
from models.user import User, user_schema
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes

authentication_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@authentication_blueprint.route('/register', methods=['POST'])
def register():
    try:
        json_data = request.get_json()

        user=User()
        user.name=json_data.get('name')
        user.email=json_data.get('email')
        if json_data.get('password'):
            user.password=bcrypt.generate_password_hash(json_data.get('password')).decode('utf-8')
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201
    except IntegrityError as e:
        if e.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {'error': 'This email address is already in use.'}, 409
        if e.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {'error': f'The {e.orig.diag.column_name} is required.'}, 409