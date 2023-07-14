from init import db, ma

class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String)

class GenreSchema(ma.Schema):
    class Meta:
        fields = ('id', 'genre')

genre_schema = GenreSchema
genres_schema = GenreSchema(many=True)