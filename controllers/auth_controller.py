from init import db, bcrypt
from flask import Blueprint, request
from models.user import User, user_schema
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token
from datetime import timedelta

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
        
@authentication_blueprint.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    stmt = db.select(User).filter_by(email=json_data.get('email'))
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, json_data.get('password')):
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=7))
        return {'Login Succesful': user.name, 'email': user.email, 'token': token, 'is_admin': user.is_admin}
    else:
        return {'Error': 'You have entered the wrong email or the wrong password. Please try again.'}, 401