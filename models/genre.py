from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

# define genre model for database
class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String)

    movies = db.relationship('Movie', back_populates=('genre'))
    books = db.relationship('Book', back_populates=('genre'))

# define marshmallow schema to serialise data
class GenreSchema(ma.Schema):

    genre = fields.String(required=True, validate=And(
        Length(min=2, error='The name of a genre must be at least two characters long.'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, numbers, and spaces are allowed in genre names.')
    ))

    class Meta:
        fields = ('id', 'genre')
        ordered = True

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)