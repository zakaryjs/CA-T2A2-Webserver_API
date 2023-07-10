from init import db, ma

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    run_time = db.Column(db.Integer)
    format = db.Column(db.String)

class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'genre', 'run_time', 'format')

movie_schema = MovieSchema
movies_schema = MovieSchema(many=True)