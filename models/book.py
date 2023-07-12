from init import db, ma
from marshmallow import fields

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    page_count = db.Column(db.Integer)

    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    format_id = db.Colunm(db.Integer, db.ForeignKey('formats.id'))

    collection = db.relationship('Collection', back_populates='books')
    genre = db.relationship('Genre', back_populates='books')
    format = db.relationship('Format', back_populates='books')

class BookSchema(ma.Schema):
    genre = fields.List(fields.Nested('GenreSchema', exclude=['id']))
    format = fields.List(fields.Nested('FormatSchema', exclude=['id']))

    class Meta:
        fields = ('id', 'title', 'genre', 'page_count', 'format')

book_schema = BookSchema
books_schema = BookSchema(many=True)