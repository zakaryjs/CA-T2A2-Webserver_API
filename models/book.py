from init import db, ma

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    genre = db.Column(db.String)
    page_count = db.Column(db.Integer)
    format = db.Column(db.String)

class BookSchema(db.Model):
    class Meta:
        fields = ('id', 'title', 'genre', 'page_count', 'format')

book_schema = BookSchema
books_schema = BookSchema(many=True)