from init import db, ma

class Collection(db.Model):
    __tablename__ = 'collections'

    id = db.Column(db.Integer, primary_key=True)

    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    movie = db.relationship('Movie', back_populates=('collections'))
    book = db.relationship('Book', back_populates=('collections'))

class CollectionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'movie_id', 'book_id')

collection_schema = CollectionSchema
collections_schema = CollectionSchema(many=True)