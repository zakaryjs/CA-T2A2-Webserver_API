from init import db
from flask import Blueprint, request
from models.book import Book, book_schema, books_schema
from models.user import User
from flask_jwt_extended import get_jwt_identity, jwt_required

def authorise_admin():
    '''Function to authorise whether or not a specific user has admin permissions'''
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    return user.is_admin

books_bp = Blueprint('books', __name__, url_prefix='/books')

@books_bp.route('/') # route for viewing all books in database
def get_all_books():
    '''/books GET route that will display a full list of all the books in the database'''
    stmt = db.select(Book).order_by(Book.id.desc()) # select all books in database and display them in descending order
    books = db.session.scalars(stmt) # makes books displayable
    return books_schema.dump(books) # returns books to users

@books_bp.route('/<int:id>') # route for viewing singular book in database
def get_one_book(id):
    '''/books/id GET route that will display a book corresponding to the ID in the URL'''
    stmt = db.select(Book).filter_by(id=id) # search the database with a filter being that of the ID in the URL
    book = db.session.scalar(stmt) # convert book to viewable format
    if book:
        return book_schema.dump(book) # return book to user
    else:
        return {'error': f'A book with the id {id} does not exist.'}, 404 # if book not found, return this error message
    
@books_bp.route('/', methods=['POST'])
@jwt_required()
def create_book():
    '''/books POST route that will receive raw JSON with fields {title, genre_id, page_count, format_id and collection_id} before being validated and then added to database'''
    json_data = book_schema.load(request.get_json()) # gets the JSON from user
    book = Book( # creates new instance of book
        title=json_data.get('title'),
        genre_id=json_data.get('genre_id'),
        page_count=json_data.get('page_count'),
        format_id=json_data.get('format_id'),
        collection_id=json_data.get('collection_id'),
        user_id=get_jwt_identity() # attaches jwt identity to book for verification
    )
    db.session.add(book) # adds book to session
    db.session.commit() # commits book to database
    return book_schema.dump(book), 201 # returns book to user

@books_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_one_book(id):
    '''/books/id DELETE route that will use the ID in the URL to locate the book, verify the user as admin and then remove the book from the database'''
    admin_status = authorise_admin # authorise_admin function checks whether user has admin permissions
    if not admin_status:
        return {'error': 'You must have admin permissions to delete books.'} # if not admin return this error message
    stmt = db.select(Book).filter_by(id=id) # filter books by the id to find specific book
    book = db.session.scalar(stmt)
    if book:
        db.session.delete(book)
        db.session.commit()
        return {'message': f'Book {book.title} has been deleted succesfully.'} # if book has been found and user has admin permissions, drop book from database
    else:
        return {'error': f'A book with the id {id} does not exist.'}, 404 # if book not found return this error message

@books_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_one_book(id):
    '''/books/id PUT/PATCH route that will use the ID in the URL in order to find the book, verify the user as the owner of the book, and then allow the user to update details of the book'''
    json_data = book_schema.load(request.get_json(), partial=True) # loads schema for book, uses partial tag as not all details may be updated
    stmt = db.select(Book).filter_by(id=id) # filter books by the id to find specific book
    book = db.session.scalar(stmt)
    if book:
        if str(book.user_id) != get_jwt_identity():
            return {'error': 'You must be the owner of the book in order to edit it.'}, 403 # if book is found and user ID does not match the jwt, return this error message
        book.title = json_data.get('title') or book.title
        book.genre = json_data.get('genre') or book.genre
        book.page_count = json_data.get('page_count') or book.page_count
        book.format = json_data.get('format') or book.format
        return book_schema.dump(book) # return edited book to user
    else:
        return {'error': f'A book with the id {id} does not exist.'}, 404 # if book is not found return this error message