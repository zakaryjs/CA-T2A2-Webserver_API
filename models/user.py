from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    collections = db.relationship('Collection', back_populates='user', cascade='all, delete')
    books = db.relationship('Book', back_populates='user')
    movies = db.relationship('Movie', back_populates='user')

class UserSchema(ma.Schema):
    collections = fields.List(fields.Nested('CollectionSchema'))

    name = fields.String(required=True, validate=And(
        Length(min=2, error='The name of a user must be at least two characters long.'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, numbers, and spaces are allowed in user names.')
    ))

    email = fields.String(required=True, validate=And(
        Length(min=2, error='A users email must be at least two characters long.'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, numbers, and spaces are allowed in emails.')
    ))
    
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')
        ordered = True

user_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=['password'])