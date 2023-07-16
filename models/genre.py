from init import db, ma

class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String)

    movies = db.relationship('Movie', back_populates=('genre'))
    books = db.relationship('Book', back_populates=('genre'))

class GenreSchema(ma.Schema):
    class Meta:
        fields = ('id', 'genre')

genre_schema = GenreSchema
genres_schema = GenreSchema(many=True)