from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, Range

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    run_time = db.Column(db.Integer)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    format_id = db.Column(db.Integer, db.ForeignKey('formats.id'))
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False)

    collection = db.relationship('Collection', back_populates='movies', cascade='all, delete')
    genre = db.relationship('Genre', back_populates='movies')
    format = db.relationship('Format', back_populates='movies')
    user = db.relationship('User', back_populates='movies')

class MovieSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    genre = fields.Nested('GenreSchema', exclude=['id'])
    format = fields.Nested('FormatSchema', exclude=['id'])
    collection = fields.Nested('CollectionSchema', exclude=['movies', 'books'])

    title = fields.String(required=True, validate=And(
        Length(min=2, error='The title of a movie must be at least 2 characters long.'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, numbers, and spaces are allowed in movie titles.')
    ))

    run_time = fields.Integer(required=True, validate=[Range(min=1, error="A movies run time must be greater than zero.")])

    format_id = fields.Integer(validate=[Range(min=6, max=8, error="A movie must belong to a movie based format.")])

    class Meta:
        fields = ('id', 'user', 'title', 'genre', 'run_time', 'format', 'collection', 'collection_id', 'genre_id', 'format_id', 'user_id')
        ordered = True

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)