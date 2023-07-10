from init import db, ma

class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String)

class GenreSchema(db.Model):
    class Meta:
        fields = ('id', 'schema')

genre_schema = GenreSchema
genres_schema = GenreSchema(many=True)