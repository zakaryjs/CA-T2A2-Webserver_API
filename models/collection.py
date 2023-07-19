from init import db, ma
from marshmallow import fields

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
    movies = fields.List(fields.Nested('MovieSchema'))
    books = fields.List(fields.Nested('BookSchema'))

    class Meta:
        fields = ('id', 'user', 'name', 'user', 'movie', 'book')

collection_schema = CollectionSchema()
collections_schema = CollectionSchema(many=True)