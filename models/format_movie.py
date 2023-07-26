from init import db, ma

# define format model for database
class FormatMovie(db.Model):
    __tablename__ = 'formatsmovie'

    id = db.Column(db.Integer, primary_key=True)
    format = db.Column(db.String)

    movies = db.relationship('Movie', back_populates=('formatsmovie'))

# define marshmallow schema to serialise data
class FormatMovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'format')
        ordered = True

formatmovies_schema = FormatMovieSchema()
formatsmovies_schema = FormatMovieSchema(many=True)