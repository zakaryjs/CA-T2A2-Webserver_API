from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, And, Regexp

# define format model for database
class Format(db.Model):
    __tablename__ = 'formats'

    id = db.Column(db.Integer, primary_key=True)
    format = db.Column(db.String)

    books = db.relationship('Book', back_populates=('format'))

# define marshmallow schema to serialise data
class FormatSchema(ma.Schema):

    format = fields.String(required=True, validate=And(
        Length(min=2, error='The name of a format must be at least two characters long.'),
        Regexp('^[a-zA-Z0-9 ]+$', error='Only letters, numbers, and spaces are allowed in format names.')
    ))

    class Meta:
        fields = ('id', 'format')
        ordered = True

format_schema = FormatSchema()
formats_schema = FormatSchema(many=True)