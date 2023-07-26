from init import db, bcrypt
from flask import Blueprint
from models.user import User
from models.collection import Collection
from models.book import Book
from models.format import Format
from models.genre import Genre
from models.movie import Movie
from models.format_movie import FormatMovie

database_commands = Blueprint('db', __name__)

@database_commands.cli.command('create')
def create_database():
    '''This function creates the database tables based on the models inside of the /models folder - User, Book, Collection, Format, Genre and Movie'''
    db.create_all()
    print("Tables have been created.") # print this message once tables have been created

@database_commands.cli.command('drop')
def drop_database():
    '''This function deletes, or drops the database and its tables, along with all related data at the request of the user'''
    db.drop_all()
    print("Tables have been dropped.") # print this message once database has been dropped

@database_commands.cli.command('seed')
def seed_database():
    '''This function seeds the created database with placeholder pieces of data for all models in the database'''
    users = [ # seeds with users, one admin, one non-admin
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

    formats = [ # seeds with formats for both movies and books
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
        ),
    ]

    db.session.add_all(formats)

    movie_formats = [
        FormatMovie(
        format='DVD'
        ),
        FormatMovie(
        format='Blu-Ray'
        ),
        FormatMovie(
        format='Ultra HD Blu-ray (4K UHD)'
        )
    ]

    db.session.add_all(movie_formats)

    genres = [ # seeds with genres, applicable to both books and movies
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

    collections = [ # seeds with example collection, belonging to admin user
        Collection(
        name='Test Collection',
        user=users[0]
        )
    ]

    db.session.add_all(collections)
    db.session.commit()

    movies = [ # seeds example movie
        Movie(
        title='Test Movie',
        genre=genres[0],
        run_time=120,
        formatsmovie=movie_formats[0],
        collection=collections[0],
        user=users[0]
        )
    ]

    db.session.add_all(movies)

    books = [ # seeds example book
        Book(
        title='Test Book',
        genre=genres[0],
        page_count=120,
        format=formats[0],
        collection=collections[0],
        user=users[0]
        )
    ]

    db.session.add_all(books)
    db.session.commit()

    print("Tables have been seeded.") # print this message once all tables have been seeded