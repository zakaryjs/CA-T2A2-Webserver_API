from init import db, bcrypt
from flask import Blueprint, request
from models.user import User, user_schema
from sqlalchemy.exc import IntegrityError
from psycopg2 import errorcodes
from flask_jwt_extended import create_access_token
from datetime import timedelta

authentication_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@authentication_blueprint.route('/register', methods=['POST']) # route for registering new user (Crud - Create)
def register():
    try:
        json_data = request.get_json() # get users json filled with required info

        user=User()
        user.name=json_data.get('name')
        user.email=json_data.get('email')
        if json_data.get('password'): # if condition to encrypt input password as hash using bcrypt
            user.password=bcrypt.generate_password_hash(json_data.get('password')).decode('utf-8')
        db.session.add(user) # add user to session
        db.session.commit() # add user to database
        return user_schema.dump(user), 201 # show user finalised inputs as user
    except IntegrityError as e: # errors relating to duplicate/empty values
        if e.orig.pgcode == errorcodes.UNIQUE_VIOLATION:
            return {'error': 'This email address is already in use.'}, 409
        if e.orig.pgcode == errorcodes.NOT_NULL_VIOLATION:
            return {'error': f'The {e.orig.diag.column_name} is required.'}, 409
        
@authentication_blueprint.route('/login', methods=['POST']) # route for logging in as user (cRud - Read)
def login():
    json_data = request.get_json() # get users input login info
    stmt = db.select(User).filter_by(email=json_data.get('email'))
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, json_data.get('password')): # check password against encrypted password to see if they match
        token = create_access_token(identity=str(user.id), expires_delta=timedelta(days=7)) # create token to allow user to stay logged in for 7 days
        return {'Login Succesful': user.name, 'email': user.email, 'token': token, 'is_admin': user.is_admin} # return users login info and admin status
    else:
        return {'Error': 'You have entered the wrong email or the wrong password. Please try again.'}, 401 # if incorrect login details, return error specifying this