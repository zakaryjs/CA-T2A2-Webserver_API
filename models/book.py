from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp, Range

VALID_FORMATS = (1, 2, 3, 4, 5)

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    page_count = db.Column(db.Integer)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    format_id = db.Column(db.Integer, db.ForeignKey('formats.id'))
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False)

    collection = db.relationship('Collection', back_populates='books', cascade='all, delete')
    genre = db.relationship('Genre', back_populates='books')
    format = db.relationship('Format', back_populates='books')
    user = db.relationship('User', back_populates='books')

class BookSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    genre = fields.Nested('GenreSchema', exclude=['id'])
    format = fields.Nested('FormatSchema', exclude=['id'])
    collection = fields.Nested('CollectionSchema', exclude=['movies', 'books'])

    title = fields.String(required=True, validate=And(
        Length(min=2, error='The title of a book must be at least 2 characters long.'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, numbers, and spaces are allowed in book titles.')
    ))

    page_count = fields.Integer(required=True, validate=[Range(min=1, error="A books page count must be greater than zero.")])

    format_id = fields.Integer(validate=[Range(min=1, max=5, error="A book must belong to a book based format.")])

    class Meta:
        fields = ('id', 'user', 'title', 'genre', 'page_count', 'format', 'collection', 'collection_id', 'genre_id', "format_id', 'user_id'")
        ordered = True

book_schema = BookSchema()
books_schema = BookSchema(many=True)