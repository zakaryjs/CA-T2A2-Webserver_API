from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

class Collection(db.Model):
    __tablename__ = 'collections'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='collections')
    movies = db.relationship('Movie', back_populates='collection')
    books = db.relationship('Book', back_populates='collection')

class CollectionSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    movies = fields.List(fields.Nested('MovieSchema', only=['id', 'title']))
    books = fields.List(fields.Nested('BookSchema', only=['id', 'title']))

    name = fields.String(required=True, validate=And(
        Length(min=2, error='The name of a collection must be at least two characters long.'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, numbers, and spaces are allowed in collection names.')
    ))

    class Meta:
        fields = ('id', 'name', 'user', 'movies', 'books')
        ordered = True

collection_schema = CollectionSchema()
collections_schema = CollectionSchema(many=True)