from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

# define format model for database
class FormatMovie(db.Model):
    __tablename__ = 'formatsmovie'

    id = db.Column(db.Integer, primary_key=True)
    format = db.Column(db.String)

    movies = db.relationship('Movie', back_populates=('formatsmovie'))

# define marshmallow schema to serialise data
class FormatMovieSchema(ma.Schema):

    format = fields.String(required=True, validate=And(
        Length(min=2, error='The name of a format must be at least two characters long.'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, numbers, and spaces are allowed in format names.')
    ))

    class Meta:
        fields = ('id', 'format')
        ordered = True

formatmovies_schema = FormatMovieSchema()
formatsmovies_schema = FormatMovieSchema(many=True)