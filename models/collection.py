from init import db, ma

class Collection(db.Model):
    __tablename__ = 'collections'

    id = db.Column(db.Integer, primary_key=True)
    movie_id =
    book_id = 

class CollectionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'movie_id', 'book_id')

collection_schema = CollectionSchema
collections_schema = CollectionSchema(many=True)