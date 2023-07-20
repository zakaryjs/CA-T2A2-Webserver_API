from init import db, ma
from marshmallow import fields

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

    class Meta:
        fields = ('id', 'user', 'title', 'genre', 'page_count', 'format', 'collection')
        ordered = True

book_schema = BookSchema()
books_schema = BookSchema(many=True)