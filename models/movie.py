from init import db, ma
from marshmallow import fields

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    run_time = db.Column(db.Integer)

    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    format_id = db.Column(db.Integer, db.ForeignKey('formats.id'))

    collection = db.relationship('Collection', back_populates='movies')
    genre = db.relationship('Genre', back_populates='movies')
    format = db.relationship('Format', back_populates='movies')


class MovieSchema(ma.Schema):
    genre = fields.List(fields.Nested('GenreSchema', exclude=['id']))
    format = fields.List(fields.Nested('FormatSchema', exclude=['id']))

    class Meta:
        fields = ('id', 'title', 'genre', 'run_time', 'format')

movie_schema = MovieSchema
movies_schema = MovieSchema(many=True)