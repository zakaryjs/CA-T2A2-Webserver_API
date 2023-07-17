from init import db, ma

class Format(db.Model):
    __tablename__ = 'formats'

    id = db.Column(db.Integer, primary_key=True)
    format = db.Column(db.String)

    movies = db.relationship('Movie', back_populates=('format'))
    books = db.relationship('Book', back_populates=('format'))

class FormatSchema(ma.Schema):
    class Meta:
        fields = ('id', 'format')

format_schema = FormatSchema()
formats_schema = FormatSchema(many=True)