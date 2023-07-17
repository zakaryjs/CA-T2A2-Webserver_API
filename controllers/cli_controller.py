from init import db, bcrypt
from flask import Blueprint
from models.user import User
from models.collection import Collection
from models.book import Book
from models.format import Format
from models.genre import Genre
from models.movie import Movie

database_commands = Blueprint('db', __name__)

@database_commands.cli.command('create')
def create_database():
    db.create_all()
    print("Tables have been created.")

@database_commands.cli.command('drop')
def drop_database():
    db.drop_all()
    print("Tables have been dropped.")

@database_commands.cli.command('seed')
def seed_database():
    users = [
        User(
        name='Admin 1',
        email='admin1@admin.com',
        password=bcrypt.generate_password_hash('admin1').decode('utf-8'),
        is_admin=True
        ),
        User(
        name='User 1',
        email='user1@user.com',
        password=bcrypt.generate_password_hash('user1').decode('utf-8')
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    formats = [
        Format(
        format='Paperback'
        ),
        Format(
        format='Hardcover'
        ),
        Format(
        format='Comic'
        ),
        Format(
        format='Omnibus'
        ),
        Format(
        format='Graphic Novel'
        )
    ]

    db.session.add_all(formats)

    genres = [
        Genre(
        genre='Action'
        ),
        Genre(
        genre='Adventure'
        ),
        Genre(
        genre='Comedy'
        ),
        Genre(
        genre='Crime'
        ),
        Genre(
        genre='Fantasy'
        ),
        Genre(
        genre='Historical'
        ),
        Genre(
        genre='Horror'
        ),
        Genre(
        genre='Romance'
        ),
        Genre(
        genre='Science Fiction'
        )
    ]

    db.session.add_all(genres)

    collections = [
        Collection(
        user_id=users[0].id
        )
    ]

    db.session.add_all(collections)
    db.session.commit()

    movies = [
        Movie(
        title='Test Movie',
        genre=genres[0],
        run_time=120,
        format=formats[0],
        user_id=users[0].id
        )
    ]

    db.session.add_all(movies)

    books = [
        Book(
        title='Test Book',
        genre=genres[0],
        page_count=120,
        format=formats[0],
        user_id=users[0].id
        )
    ]

    db.session.add_all(books)
    db.session.commit()

    print("Tables have been seeded.")