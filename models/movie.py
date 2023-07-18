from init import db, ma
from marshmallow import fields

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    run_time = db.Column(db.Integer)

    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    format_id = db.Column(db.Integer, db.ForeignKey('formats.id'))
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    collection = db.relationship('Collection', back_populates='movies', cascade='all, delete')
    genre = db.relationship('Genre', back_populates='movies')
    format = db.relationship('Format', back_populates='movies')

class MovieSchema(ma.Schema):
    genre = fields.Nested('GenreSchema', exclude=['id'])
    format = fields.Nested('FormatSchema')
    user = fields.Nested('UserSchema', only=['name', 'email'])

    class Meta:
        fields = ('id', 'title', 'genre_id', 'run_time', 'format_id')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)