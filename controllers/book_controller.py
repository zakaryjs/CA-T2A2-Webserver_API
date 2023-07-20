from init import db
from flask import Blueprint, request
from models.book import Book, book_schema, books_schema
from models.user import User
from flask_jwt_extended import get_jwt_identity, jwt_required

def authorise_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    return user.is_admin

books_bp = Blueprint('books', __name__, url_prefix='/books')

@books_bp.route('/')
def get_all_books():
    stmt = db.select(Book).order_by(Book.id.desc())
    books = db.session.scalars(stmt)
    return books_schema.dump(books)

@books_bp.route('/<int:id>')
def get_one_book(id):
    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)
    if book:
        return book_schema.dump(book)
    else:
        return {'error': f'A book with the id {id} does not exist.'}, 404
    
@books_bp.route('/', methods=['POST'])
@jwt_required()
def create_book():
    json_data = book_schema.load(request.get_json())
    book = Book(
        title=json_data.get('title'),
        genre_id=json_data.get('genre_id'),
        page_count=json_data.get('page_count'),
        format_id=json_data.get('format_id'),
        collection_id=json_data.get('collection_id'),
        user_id=get_jwt_identity()
    )
    db.session.add(book)
    db.session.commit()
    return book_schema.dump(book), 201

@books_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_book(id):
    admin_status = authorise_admin
    if not admin_status:
        return {'error': 'You must have admin permissions to delete books.'}
    stmt = db.select(Book).filter_by(id)
    book = db.session.scalar(stmt)
    if book:
        return {'error': f'Book {book.title} has been deleted succesfully.'}
    else: return {'error': f'A book with the id {id} does not exist.'}, 404

@books_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_book(id):
    json_data = book_schema.load(request.get_json(), partial=True)
    stmt = db.select(Book).filter_by(id=id)
    book = db.session.scalar(stmt)
    if book:
        if str(book.user_id) != get_jwt_identity():
            return {'error': 'You must be the owner of the book in order to edit it.'}, 403
        book.title = json_data.get('title') or book.title
        book.genre = json_data.get('genre') or book.genre
        book.page_count = json_data.get('page_count') or book.page_count
        book.format = json_data.get('format') or book.format
        return book_schema.dump(book)
    else:
        return {'error': f'A book with the id {id} does not exist.'}, 404