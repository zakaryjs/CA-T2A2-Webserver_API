from init import db, ma
from marshmallow import fields

class Collection(db.Model):
    __tablename__ = 'collections'

    id = db.Column(db.Integer, primary_key=True)

    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    movie = db.relationship('Movie', back_populates=('collections'))
    book = db.relationship('Book', back_populates=('collections'))

class CollectionSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])

    class Meta:
        fields = ('id', 'user_id', 'movie_id', 'book_id')

collection_schema = CollectionSchema
collections_schema = CollectionSchema(many=True)