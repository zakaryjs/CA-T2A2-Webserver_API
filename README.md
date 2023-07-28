# T2A2 - API Webserver Project

<u>**BUILT WITH**</u>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

<hr>

## Important Links

![Last Commit Badge](https://img.shields.io/github/last-commit/zakaryjs/T2A2-Webserver_API)

#### [Github Repository](https://github.com/zakaryjs/T2A2-Webserver_API)

#### [Trello Board](https://trello.com/invite/b/LaCoYbLG/ATTI530e5c791577751ea1a95fcc9be416a1B3DB7C3C/t2a2-webserver-api)

## Installation and Setup

Requirements:

- [Python 3](https://www.python.org/downloads/)

- [PostgreSQL](https://www.postgresql.org/download/)

- [This Repository (application source code)](https://github.com/zakaryjs/T2A2-Webserver_API) - You can either clone this by typing ```git clone git@github.com:zakaryjs/T2A2-Webserver_API.git``` inside of a terminal window, or download it directly from GitHub by clicking the green `Code` button, and then clicking `Download ZIP`.

Once you have ensured that these requirements are installed:

**PSQL SETUP**

1. Open a new CLI/Terminal window.

2. Enter ```psql``` into the terminal window

3. Depending on the selected authentication method, you may need to login.*

4. Create a new user, for the database: ```CREATE USER media_user WITH PASSWORD 'media_password';```

5. Create a new database: ```CREATE DATABASE media_management_db;```

6. Grant all permissions for the new database to the new user: ```GRANT ALL PRIVILEGES ON DATABASE media_management_db TO media_user;```

7. Connect to the database: ```\c media_management_db;```

**FLASK APP SETUP**

1. Open the the cloned/downloaded repository folder.

2. Rename the `.env.sample` file to `.env` and enter the database connection URL and the secret key:

```DATABASE_URL="postgresql+psycopg2://media_user:mediapassword@localhost:5432/media_management_db"```

```JWT_SECRET_KEY="placeholdersecretkey"```

3. Open a terminal window inside of the repository folder and create a new virtual environment and install the requirements:

`python3 -m venv .venv`

`source .venv/bin/activate`

`pip install -r requirements.txt`

4. Use the create and seed db commands to create the database tables and seed example entries for each table:

`flask db create`

`flask db seed`

5. If you wish to delete the tables, simply enter the drop command:

`flask db drop`

6. Run the Flask application, in order to start the server:

`flask run`

7. To access different parts of the server, it is best to use an API development platform such as [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/) in order to be able to send the required ``GET``, ``POST``, ``PUT``/``PATCH`` and ``DELETE`` ``http methods``. The server can be accessed by the URL ```localhost:8080```.


<hr>

## Requirements

### R1: Identification of the problem you are trying to solve by building this particular app.

The problem that I am trying to solve with this app is an organisational problem. For most types of media, whether that be music, film or books - there is a digital format available. Whether it be for convenience purposes, or space purposes, or solely due to preference, digital formats are now more popular than physical. These items are then downloaded, and then automatically organised onto your device. Physical media doesn't get this luxury. It is instead up to the owner to organise their items as they would please. This API takes books and movies and organises them according to their respective genres, formats and either run time/page count. 

### R2: Why is it a problem that needs solving?

This problem needs solving as it is too easy to lose track of what media you may own. A person may end up owning large amounts of physical media and having to store different items in different places, which would eventually lead to different types of physical media, such as books and movies, being unorganised. Having a database such as the flask database inside of this repository allows a user to add a piece of media to the database, and then, if they wanted to, store it, as it has now been permanently stored inside a collection in the database.

Another aspect of this problem is that a user may become overwhelmed by the idea of having to sort through their media to find a certain book/movie, and as such may stick to just rereading or rewatching specific books or movies, failing to take advantage of the pieces of media they own.

### R3: Why have you chosen this database system. What are the drawbacks compared to others? [^10]

The database system that I chose to use for this assignment is PostgreSQL. I chose this database system as it is what I am familiar with, and it supported everything that I needed in order to complete the assignment.

The database needed to be:

- Something I knew how to use
- Supported relational databases
- Had ORM functionality, one that I was familiar with (SQLAlchemy)

Postgres ticks all of these boxes, and as such I chose it for this assignment.

**Advantages**

Postgres has many features that allow for the database to be reliable, keep strong data integrity, and be easily scalable. Postgres also has extensive documentation available online, which made troubleshooting much easier. With over 35 years of support, new features and improvements are still being made and as such is a strong option for a database.

Postgres is also fully ACID compliant, which further helps enforce and ensure data integrity and reliability. This assists for those databases with CRUD functionality in mind, ensuring that data is able to be created, modified, viewed and deleted without issue. This, combined with the CRUD functionality requirements for my assignment, meant that I needed a database that would be able to handle all of these operations and ensure that every piece of data is stored correctly.

Postgres also supports a wide variety of data types, resulting in an overall wider range of use cases for potential applications. Furthermore, users can also define their own parameters in regards to the relations, datatypes, or the database itself, allowing for functionality to be further specialised for its particular use. This was especially important for my API as I needed to ensure that every piece of information was validated to set parameters, and appeared correctly.

Lastly, Postgres is Open-Source, meaning that developers are able to modify parts of the code as required.

**Disadvantages**

From a performance based perspective, Postgres, in most scenarios, is slower than other alternatives such as MySQL. This is more apparent in bigger databases, due to the way that Postgres handles reading operations. This is due to the fact that Postgres was designed with compatibility and integrity as a key focus, meaning that though Postgres is more feature rich, its performance takes a hit; more noticably at a larger scale.

Postgres also has less third party support when compared with other database management systems. This results in less extensive function in comparison to others such as MySQL, which has more third party support, a larger community, and more trained professionals available.

Postgres is also more complicated in regards to the setup, which creates a larger barrier for entry, leading to the overall experience being less beginner-friendly.

Though these are widely considered to be the most common disadvantages, these did not affect me as PSQL met my needs and was something that I was familiar with.

### R4: Identify and discuss the key functionalities and benefits of an ORM [^8]

**Functionality**

ORM stands for Object Relational Mapping. An ORM is a way for an application to interact with a database. 

ORMs use a programming language, instead of plain SQL, for database related commands, making it easier to create queries, and modify the entirety of the database. This also means that developers dont have to constantly switch between writing SQL, and for example, Python, and can just write in the one language. 

ORMs are designed to help simplify the interactions between a database, such as the one used in this assignment, and a programming language, such as Python. 

ORMs, by design, result in developers writing less code in most cases. As they don't have to spend time writing multiple similar, repeated statements and instead allow developers to use functions in order to create queries and other operations.

ORMs also allow developers to easily change the database that the app is currently connected to. In this apps current configuration, and in other apps that use the SQLAlchemy ORM, this can be changed by editing the `.env` file and changing the `DATABASE_URL`. 

ORMs also provide features to allow custom validation, and configuration as to the data types, and requirements of certain fields/tables. other libraries can extend this functionality, e.g. `Marshmallow`, and can be used to ensure data validity and integrity.

**Benefits**

SQL syntax is not required inside of an ORM, and instead may only be used inside of the actual database if it is required.

ORMs provide strong security in regards to database connections, to ensure that all operations are completed, and not intefered with.

ORMs allow for developers to use the object oriented functions of their chosen programming language. This means that knowledge from the functions of a specific programming language can be applied in the creation of database relations, relationships and validation paramaters. 

Furthermore, ORMS have strong support for most SQL tasks. The ORM that is used in this application, SQLAlchemy, makes it easy to create, seed and drop databases. It is also really easy to manipulate the data inside of a database that is connected to an ORM as this can be done through the use of functions, which can be repeated a multitude of times instead of having to write single queries.
### R5: Document all endpoints for your API

Endpoint documentation should include:
HTTP request verb
Required data where applicable 
Expected response data 
Authentication methods where applicable

#### <u>Authentication Used</u>

**authorise_admin (admin_status)**
- Is used to check whether or not a user has admin permissions.
- Admin permissions are required in order to delete things from the database; collections, books, movies.
- This function uses get_jwt_identity in order to get the users JWT token which is used to check whether is_admin is set to true for the specific user.

#### <u>Users (auth controller)</u>

##### /register
**HTTP Request Method:** POST

**Required Data:**
- Name (string) - must be at least 2 characters long and follow Regexp paramater
- Email (string) - must be in valid email format
- Password (string) - must be at least 6 characters long (is encrypted with bcrypt before stored in database)

**Expected Response:**
If successful the route will return the users ID, name, email, and admin status in JSON format.
- If the users email is not unique, an IntegrityError will be returned, accompanied with an error message.
- If a field is missing, an IntegrityError will be returned, accompanied with an error message specifying that the field must not be empty.
- If a field fails validation, a ValidationError will be returned, accompanied with an error message.

**Authorisation Methods:**
None

##### /login
**HTTP Request Method:** POST

**Required Data:**
- Email (string)
- Password (string)

**Expected Response:**
If the login is successful, the route will return a login successful message, with the users name, email, a JWT authentication token, and the users current admin status.
- If the user enters the wrong login information, an error will be returned stating this.

**Authorisation Methods:**
None

#### <u>Collections</u>

##### /collections
**HTTP Request Method:** GET

**Required Data:**
None

**Expected Response:**
If the request is successful, a list of all collections inside of the database will be returned in JSON format, in descending order. If there are any movies or books that belong to the collection, these will be returned, nested inside of the response.

- ID
- Name
- User who created the collection
- Movies
- Books

**Authorisation Methods:**
None

##### /collections/<int:id>
**HTTP Request Method:** GET

**Required Data:**
The ID of the collection that the user is searching for.

**Expected Response:**
If the request is successful, the collection inside of the database that matches the requested ID will be returned in JSON format. If there are any movies or books that belong to the collection, these will be returned, nested inside of the response.

**Authorisation Methods:**
None

##### /collections
**HTTP Request Method:** POST

**Required Data:**
- Name (string)
- User ID (jwt token)

**Expected Response:**
If the request is successful, the collections ID, name, and the user who created it will be returned.
- If a name is missing, or does not succeed in validation, a ValidationError will be returned, accompanied with a message.
- If there is no JWT token, "msg": "Missing Authorization Header" will be returned.

**Authorisation Methods:**
JWT Token

##### /collections/<int:id>
**HTTP Request Method:** DELETE

**Required Data:**
The ID of the collection that the user wishes to delete. 

**Expected Response:**
If the request is successful, a message is returned stating that the collection has been successfully deleted.
- If the user does not have admin privileges, an error message is returned.
- If a collection with the requested ID does not exist, an error message is returned.

**Authorisation Methods:**
authorise_admin

##### /collections/<int:id>
**HTTP Request Method:** PUT, PATCH

**Required Data:**
The ID of the collection that the user wants to update.
The updated collection name. (string)

**Expected Response:**
If the request is successful, the collections ID, name, and the user who created it along with any books/movies associated with it will be returned to the user.
- If the user trying to edit the collection didn't create the collection, an error message will be returned.
- If a collection with the requested ID doesn't exist, an error message will be returned.

**Authorisation Methods:**
JWT Token

#### <u>Books</u>

##### /books
**HTTP Request Method:** GET

**Required Data:**
None

**Expected Response:**
If the request is successful, a list of all books inside of the database will be returned in JSON format, in descending order. The collection, genre, format and user that the books belong to will be returned in nested schemas.

- ID
- User
- Title
- Genre
- Page_count
- Format
- Collection

**Authorisation Methods:**
None

##### /books/<int:id>
**HTTP Request Method:** GET

**Required Data:**
The ID of the book the user is searching for.

**Expected Response:**
If the request is successful, the book inside of the database that matches the requested ID will be returned in JSON format. The collection, genre, format and user that the book belongs to will be returned in nested schemas.

**Authorisation Methods:**
None

##### /books
**HTTP Request Method:** POST

**Required Data:**
- Title (string)
- Genre_id (integer)
- Page_count (integer)
- Format_id (integer)
- Collection_id (integer)
- User_id (JWT Token)

**Expected Response:**
If the request is successful, the books ID, title, the user who created it, page count, genre, format and the collection it belongs to will be returned.
- If a name is missing, or does not succeed in validation, a ValidationError will be returned, accompanied with a message.
- If there is no JWT token, "msg": "Missing Authorization Header" will be returned.

**Authorisation Methods:**
JWT Token

##### /books/<int:id>
**HTTP Request Method:** DELETE

**Required Data:**
The ID of the book that the user wants to delete.

**Expected Response:**
If the request is successful, a message is returned stating that the book has been successfully deleted.
- If the user does not have admin privileges, an error message is returned.
- If a book with the requested ID does not exist, an error message is returned.

**Authorisation Methods:**
authorise_admin

##### /books/<int:id>
**HTTP Request Method:** PUT, PATCH

**Required Data:**
The ID of the book that the user wants to update.
At least one of the following:
- Title (string)
- Genre_id (integer)
- Page_count (integer)
- Format_id (integer)
- Collection_id (integer)

**Expected Response:**
If the request is successful, the books ID, title, the user who created it, page count, genre, format and the collection it belongs to will be returned.
- If the user trying to edit the book didn't create the book, an error message will be returned.
- If a book with the requested ID doesn't exist, an error message will be returned.

**Authorisation Methods:**
JWT Token

#### <u>Movies</u>

##### /movies
**HTTP Request Method:** GET

**Required Data:**
None

**Expected Response:**
If the request is successful, a list of all movies inside of the database will be returned in JSON format, in descending order. The collection, genre, format and user that the movies belong to will be returned in nested schemas.

- ID
- User
- Title
- Genre
- Run_time
- Format
- Collection

**Authorisation Methods:**
None

##### /movies/<int:id>
**HTTP Request Method:** GET

**Required Data:**
The ID of the movie the user is searching for.

**Expected Response:**
If the request is successful, the movie inside of the database that matches the requested ID will be returned in JSON format. The collection, genre, format and user that the movie belongs to will be returned in nested schemas.

**Authorisation Methods:**
None

##### /movies
**HTTP Request Method:** POST

**Required Data:**
- Title (string)
- Genre_id (integer)
- Run_time (integer)
- Format_id (integer)
- Collection_id (integer)
- User_id (JWT Token)

**Expected Response:**
If the request is successful, the movies ID, title, the user who created it, run time, genre, format and the collection it belongs to will be returned.
- If a name is missing, or does not succeed in validation, a ValidationError will be returned, accompanied with a message.
- If there is no JWT token, "msg": "Missing Authorization Header" will be returned.

**Authorisation Methods:**
JWT Token

##### /movies/<int:id>
**HTTP Request Method:** DELETE

**Required Data:**
The ID of the movie that the user wants to delete.

**Expected Response:**
If the request is successful, a message is returned stating that the movie has been successfully deleted.
- If the user does not have admin privileges, an error message is returned.
- If a movie with the requested ID does not exist, an error message is returned.

**Authorisation Methods:**
authorise_admin

##### /movies/<int:id>
**HTTP Request Method:** PUT, PATCH

**Required Data:**
The ID of the movie that the user wants to update.
At least one of the following:
- Title (string)
- Genre_id (integer)
- Run_time (integer)
- Format_id (integer)
- Collection_id (integer)

**Expected Response:**
If the request is successful, the movies ID, title, the user who created it, page count, genre, format and the collection it belongs to will be returned.
- If the user trying to edit the movie didn't create the movie, an error message will be returned.
If a movie with the requested ID doesn't exist, an error message will be returned.

**Authorisation Methods:**
JWT Token

#### <u>Formats</u>

##### /formats
**HTTP Request Method:** GET

**Required Data:**
None

**Expected Response:**
If the request is successful, a list of all book formats inside of the database will be returned in JSON format, in descending order. 

- ID
- Format

**Authorisation Methods:**
None

##### /formats/<int:id>
**HTTP Request Method:** GET

**Required Data:**
None

**Expected Response:**
If the request is successful, the book format corresponding to the ID inside of the database will be returned in JSON format.

- ID
- Name

**Authorisation Methods:**
None

##### /formats
**HTTP Request Method:** POST

**Required Data:**
- Format (string)

**Expected Response:**
If the request is successful, the formats name will be returned.
- If the format name is missing, or does not succeed in validation, a ValidationError will be returned, accompanied with a message.
- If there is no JWT token, "msg": "Missing Authorization Header" will be returned.

**Authorisation Methods:**
JWT Token

##### /formats/<int:id>
**HTTP Request Method:** DELETE

**Required Data:**
The ID of the format that the user wants to delete.

**Expected Response:**
If the request is successful, a message is returned stating that the format has been successfully deleted.
- If the user does not have admin privileges, an error message is returned.
- If a format with the requested ID does not exist, an error message is returned.

**Authorisation Methods:**
authorise_admin

##### /formats/<int:id>
**HTTP Request Method:** PUT, PATCH

**Required Data:**
The ID of the format that the user wants to update.
The new format name. (string)

**Expected Response:**
If the request is successful, the formats ID and name will be returned.
If a format with the requested ID doesn't exist, an error message will be returned.

**Authorisation Methods:**
JWT Token

#### <u>Movie Formats</u>

##### /movie_formats
**HTTP Request Method:** GET

**Required Data:**
None

**Expected Response:**
If the request is successful, a list of all movie formats inside of the database will be returned in JSON format, in descending order. 

- ID
- Format

**Authorisation Methods:**
None

##### /movie_formats/<int:id>
**HTTP Request Method:** GET

**Required Data:**
None

**Expected Response:**
If the request is successful, the movie format corresponding to the ID inside of the database will be returned in JSON format.

- ID
- Name

**Authorisation Methods:**
None

##### /movie_formats
**HTTP Request Method:** POST

**Required Data:**
- Format (string)

**Expected Response:**
If the request is successful, the formats name will be returned.
- If the format name is missing, or does not succeed in validation, a ValidationError will be returned, accompanied with a message.
- If there is no JWT token, "msg": "Missing Authorization Header" will be returned.

**Authorisation Methods:**
JWT Token

##### /movie_formats/<int:id>
**HTTP Request Method:** DELETE

**Required Data:**
The ID of the format that the user wants to delete.

**Expected Response:**
If the request is successful, a message is returned stating that the format has been successfully deleted.
- If the user does not have admin privileges, an error message is returned.
- If a format with the requested ID does not exist, an error message is returned.

**Authorisation Methods:**
authorise_admin

##### /movie_formats/<int:id>
**HTTP Request Method:** PUT, PATCH

**Required Data:**
The ID of the format that the user wants to update.
The new format name. (string)

**Expected Response:**
If the request is successful, the formats ID and name will be returned.
If a format with the requested ID doesn't exist, an error message will be returned.

**Authorisation Methods:**
JWT Token

#### <u>Genres</u>

##### /genres
**HTTP Request Method:** GET

**Required Data:**
None

**Expected Response:**
If the request is successful, a list of all genres inside of the database will be returned in JSON format, in descending order. 

- ID
- Genre

**Authorisation Methods:**
None

##### /genres/<int:id>
**HTTP Request Method:** GET

**Required Data:**
None

**Expected Response:**
If the request is successful, the genre corresponding to the ID inside of the database will be returned in JSON format.

- ID
- Genre

**Authorisation Methods:**
None

##### /genres
**HTTP Request Method:** POST

**Required Data:**
- Genre (string)

**Expected Response:**
If the request is successful, the genres name will be returned.
- If the genre name is missing, or does not succeed in validation, a ValidationError will be returned, accompanied with a message.
- If there is no JWT token, "msg": "Missing Authorization Header" will be returned.

**Authorisation Methods:**
JWT Token

##### /genres/<int:id>
**HTTP Request Method:** DELETE

**Required Data:**
The ID of the genre that the user wants to delete.

**Expected Response:**
If the request is successful, a message is returned stating that the genre has been successfully deleted.
- If the user does not have admin privileges, an error message is returned.
- If a genre with the requested ID does not exist, an error message is returned.

**Authorisation Methods:**
authorise_admin

##### /genres/<int:id>
**HTTP Request Method:** PUT, PATCH

**Required Data:**
The ID of the genre that the user wants to update.
The new genre name. (string)

**Expected Response:**
If the request is successful, the genres ID and name will be returned.
If a genre with the requested ID doesn't exist, an error message will be returned.

**Authorisation Methods:**
JWT Token


### R6: An ERD for your app

### R7: Detail any third party services that your app will use

**Flask** [^1] [^2]
Flask is a lightweight, and easily expandable web framework built for Python. Flask is designed to be easy to use, and easy to fit to any users needs. Flask makes use of the Web Server Gateway Interface in order to process the requests between a web server and the Flask app itself. It allows users to efficiently build web applications. At its core, Flask provides users with the ability to design routes, with specified HTTP requests, and allows them to associate these routes with HTML and CSS, in order to create a front end. As it is a lightweight framework, a key feature is to be able to, as mentioned above, easily expand its functionality through the use of libraries or other extensions.

**Psycopg2** [^3]
Psycopg2 is a PostgreSQL database adapter for Python, that allows for Python apps to directly connect to a PostgreSQL database. The adapter was designed for databases which perform a significant number of CRUD based operations, and as such is able to efficiently perform these operations without issue. Psycopg2 is defined to be both efficient and secure, and as such is a reliable way to connect Python applications to PSQL databases.

**SQLAlchemy** [^9]
SQLAlchemy is an Object Relational Mapper that allows Python developers to take full advantage of the power of SQL, through an adapted language based on Python. SQLAlchemy allows developers to interact with SQL databases through the use of Python objects, which act as the data stored inside of an SQL database. Database tables are defined as classes, and nest inside them all fields of a certain table and their relationships between other tables. SQLAlchemy allows developers to perform highly sophisticated SQL queries without writing SQL itself, meaning that databases can be modified directly from the ORM.

**Marshmallow** [^4] [^5]
Marshmallow is a library that is used to both serialise and deserialise objects for use with Python and ORMs. Marshmallow is used to convert complex datatypes, including dictionaries, into the JSON format, from which they can then be used in web server APIs. Marshmallow also provides a schema functionality, which allows for validation of data, as well as deserialisation and serialisation of objects in order to ensure consistency and reliability when converting data between app-level objects and Python datatypes.

**Bcrypt** [^6]
Bcrypt is a library that uses cryptographic functions in order to securely hash, and then salt plain text, sensitive data, that results in an unreadable string. Bcrypt is designed to be slow at this process, in order to reduce the strength, severity, and speed of brute-force based attacks, in order to ensure that encrypted hashes are as secure as possible. Bcrypts abilities to prevent brute-force attacks, and compensate for future faster hardware ensure that the library will still be secure in the future.


**JWT Token (JSON Web Token)** [^7]
A JSON Web Token is a JSON Object which is used to reliably and securely transfer pieces of information between two destinations over the internet. JWT is often used in web apps and servers such as this Media Management API in order to verify a users identity before performing specific CRUD operations. A JWT has three parts: Header, Payload, and Signature. The header contains the type of the token (JWT), and the algorithm used for signing (eg SHA256). The Payload contains claims, which are the pieces of information that is being exchanged via the token. The signature is used to valid and ensure that the contents of the exchanged message were not modified in anyway.

### R8: Describe your projects models in terms of the relationships they have with each other

There are 7 models used in the Media Management API:
- User
- Collection
- Book
- Movie
- Genre
- Book Format
- Movie Format

**Model 1: User**

```py
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    collections = db.relationship('Collection', back_populates='user', cascade='all, delete')
    books = db.relationship('Book', back_populates='user')
    movies = db.relationship('Movie', back_populates='user')
```

The user model contains fields for a users ID (assigned at creation of new user), their name, email, password and admin status.

The user model has a one to many relationship with collections - a 'Collection' back populates a single user. When a user is deleted, the model cascades, and all collections associated with it are deleted.
The user model also has a one to many relationship with both books and movies - a multitude of books and movies can belong to a singular user.

**Model 2: Collection**

```py
class Collection(db.Model):
    __tablename__ = 'collections'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='collections')
    movies = db.relationship('Movie', back_populates='collection', cascade='all, delete')
    books = db.relationship('Book', back_populates='collection', cascade='all, delete')
```

The collection model contains fields for a collections ID (assigned at creation of new collection), and the name of a collection.

The collection model has a many to one relationship with users - a 'User' back populates multiple collections.
The collection model also has a many to one relationship with both books and movies - a multitude of books and movies can belong to a singular collection. The `cascade='all, delete'` at the end of the movies and books lines, means that if a collection is deleted, all of the books and movies inside the collection are too.

**Model 3: Book**

```py
class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    page_count = db.Column(db.Integer)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    format_id = db.Column(db.Integer, db.ForeignKey('formats.id'))
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False)

    collection = db.relationship('Collection', back_populates='books')
    genre = db.relationship('Genre', back_populates='books')
    format = db.relationship('Format', back_populates='books')
    user = db.relationship('User', back_populates='books')
```

The book model contains fields for a books ID (assigned at creation of new book), the user that created the book, the title of the book, the genre, the page count, the format, and the collection that it belongs to.

The book model has a many to one relationship with collections - a 'Collection' back populates multiple books.
The book model has a many to one relationship with both genres and formats - 'Genre' and 'Format' both back populate multiple books.
The book model has a many to one relationship with users - 'User' back populates multiple books.

**Model 4: Movie**

```py
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    run_time = db.Column(db.Integer)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    format_id = db.Column(db.Integer, db.ForeignKey('formatsmovie.id'))
    collection_id = db.Column(db.Integer, db.ForeignKey('collections.id'), nullable=False)

    collection = db.relationship('Collection', back_populates='movies')
    genre = db.relationship('Genre', back_populates='movies')
    formatsmovie = db.relationship('FormatMovie', back_populates='movies')
    user = db.relationship('User', back_populates='movies')
```
The movie model contains fields for a movies ID (assigned at creation of new movie), the user that created the movie, the title of the movie, the genre, the run time, the format, and the collection that it belongs to.

The movie model has a many to one relationship with collections - a 'Collection' back populates multiple movies.
The movie model has a many to one relationship with both genres and formatsmovies - 'Genre' and 'FormatMovie' both back populate multiple movies.
The movie model has a many to one relationship with users - 'User' back populates multiple movies.

**Model 5: Genre**

```py
class Genre(db.Model):
    __tablename__ = 'genres'

    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String)

    movies = db.relationship('Movie', back_populates=('genre'))
    books = db.relationship('Book', back_populates=('genre'))
```

The genre model contains fields for a genres ID (assigned at creation of new genre) and the genres name.

The genre model has a one to many relationship with both books and movies - a 'Movie' or 'Book' back populates multiple genres.

**Model 6: Format (Book)**

```py
class Format(db.Model):
    __tablename__ = 'formats'

    id = db.Column(db.Integer, primary_key=True)
    format = db.Column(db.String)

    books = db.relationship('Book', back_populates=('format'))
```

The format model contains fields for a formats ID (assigned at creation of new format) and the formats name.

The format model has a one to many relationship with books - a 'Book' back populates multiple formats.

**Model 7: Format (Movie)**

```py
class FormatMovie(db.Model):
    __tablename__ = 'formatsmovie'

    id = db.Column(db.Integer, primary_key=True)
    format = db.Column(db.String)

    movies = db.relationship('Movie', back_populates=('formatsmovie'))
```

The formatmovie model contains fields for a formats ID (assigned at creation of new format) and the formats name.

The formatmovie model has a one to many relationship with movies - a 'Movie' back populates multiple formats.

### R9: Discuss the database relations to be implemented in your application

There are 7 tables used in the Media Management API:
- User
- Collection
- Book
- Movie
- Genre
- Book Format
- Movie Format

**Table 1: User**

As shown in the ERD, the User table has a one to many relationship with the Collection, Book and Movie tables. 

The relationship between the User and Collection tables is established through the 'user_id' foreign key in the collection table. This key allows for the user who created the collection to have their unique user_id to be stored inside of any collection that they create.

The relationship between the User, and the Book and Movie tables is established through the 'user_id' foreign key in both the book and movie table. This key allows for the user who created the collection to have their unique user_id to be stored inside of any book or movie that they create.

The User Schema ensures that the name, email and password fields are all required to be entered on registration. The name field is required to be at least 2 characters long, and must follow the set character rules. The email field is required to be in the traditional email format, and must be unique - this is in order to prevent duplicates. Lastly, the password must be at least 6 characters long.

**Table 2: Collection**

As shown in the ERD, the Collection table has a many to one relationship with the User table. The Collection table also has a many to one relationship the Book and Movie tables. 

The relationship between the Collection and User tables is established through the 'user_id' foreign key in the collection table. This key allows for the user who created the collection to have their unique user_id to be stored inside of any collection that they create.

The relationship between the Collection, and the Book and Movie tables is established through the 'collection_id' foreign key located in both the book and movie tables. This key allows for the collection that the respective book/movie belongs to have their unique collection_id to be stored inside of any book or movie that belongs to that collection.

The Collection Schema ensures that the name of any collection in the database is required on creation. The name field is required to be at least 2 characters long, and must follow the set character rules. The user_id, as a foreign key, is a requirement, in order to ensure that every collection has an owner.

**Table 3: Book**

As shown in the ERD, the Book table has a many to one relationship with the Collection, Genre and Format tables.

The relationship between the Book and Collection tables is established through the 'collection_id' foreign key located in the book table. This key allows for the collection that the respective book belongs to have their unique collection_id to be stored inside of any book that belongs to that collection.

The relationship between the Book, and the Format and Genre tables is established through the 'genre_id' and 'format_id' foreign keys located in the book table. This allows for the genre/format that the book belongs to have their unique genre_id/format_id stored inside of any book that belongs to that genre/format.

The Book Schema ensures that the title of any book in the database is required on creation. The title field is required to be at least 2 characters long, and follow the set character rules. The page count field is required, and must have a value of at least 1 (which book has 0 pages?). The foreign keys, format_id, genre_id and collection_id are all required in order to link the tables together.

**Table 4: Movie**

As shown in the ERD, the Movie table has a many to one relationship with the Collection, Genre and Format tables.

The relationship between the Movie and Collection tables is established through the 'collection_id' foreign key located in the movie table. This key allows for the collection that the respective movie belongs to have their unique collection_id to be stored inside of any movie that belongs to that collection.

The relationship between the Movie, and the Format and Genre tables is established through the 'genre_id' and 'format_id' foreign keys located in the movie table. This allows for the genre/format that the movie belongs to have their unique genre_id/format_id stored inside of any movie that belongs to that genre/format.

The Movie Schema ensures that the title of any movie in the database is required on creation. The title field is required to be at least 2 characters long, and follow the set character rules. The run time field is required, and must have a value of at least 1 (which movie has a run time of 0 minutes?). The foreign keys, format_id, genre_id and collection_id are all required in order to link the tables together.

**Table 5: Genre**

As shown in the ERD, the Genre table has a one to many relationship with both the Book and Movie tables.

The relationship between the Genre, and the Book and Movie tables is established through the 'genre_id' foreign key that is located in both the Book and Movie tables. This allows for the genre that the book/movie belongs to have their unique genre_id stored inside of any book/movie that belongs to that genre.

The Genre Schema ensures that the name of any genre in the database is required on creation. The genre field is required to be at least 2 characters long, and follow the set character rules. 

**Table 6: Format (Book)**

As shown in the ERD, the Format table has a one to many relationship with the Book table.

The relationship between the Format, and the Book table is established through the 'format_id' foreign key that is located in the Book table. This allows for the format that the book belongs to have their unique format_id stored inside of any book that belongs to that format.

The Format Schema ensures that the name of any format in the database is required on creation. The format field is required to be at least 2 characters long, and follow the set character rules. 

**Table 7: Format (Movie)**

As shown in the ERD, the FormatMovie table has a one to many relationship with the Movie table.

The relationship between the FormatMovie, and the Movie table is established through the 'format_id' foreign key that is located in the Movie table. This allows for the format that the movie belongs to have their unique format_id stored inside of any movie that belongs to that format.

The FormatsMovies Schema ensures that the name of any format in the database is required on creation. The format field is required to be at least 2 characters long, and follow the set character rules. 


### R10: Describe the way tasks are allocated and tracked in your project

All tasks were estbalished and organised inside of my Trello Board:

[Trello Board](https://trello.com/invite/b/LaCoYbLG/ATTI530e5c791577751ea1a95fcc9be416a1B3DB7C3C/t2a2-webserver-api)

I first created custom labels, in order to establish a priority system:

Green = Low Priority
Yellow = Medium Priority
Red = High Priority

I then created the categories that I new had to be done - the planning, the coding, and the reviewing.
After this, I began putting specific tasks under their set category. For planning, this included drafting ideas, creating a draft ERD for submission, and deciding on the idea and creating the board.

I set the due date as July 7 - the day that all of the planning was done, in order to ensure that I was motivated to get it done so that I could begin work on the actual project. I also wanted to get the original repository set up on that day, as, again, I wanted to get started on the project the next time that I was ready to work on the project.

I had planned to have a majority of the code to be done after two weeks, however, gave myself a bit of extra space in regards to writing the README and doing the final checks so that if there were any issues, I would be able to solve them in time. 

This proved to be beneficial, as I did end up having issues regarding the collection and book/movies tables, however once these issues were solved I was able to work on the validation part of the assignment.

After this was done, I began work on the requirements for the README.
As of the 27th of July, as I am writing this, the Trello Board looks like this:





Having this Trello Board and making use of dates, labels and checklists, meant that I would be able to hold myself to deadlines, be able to see the progress, and most importantly, ensure that I would get the project done on time.


Sources:

[^1]: Flask. Full Stack Python. (n.d.). https://www.fullstackpython.com/flask.html 

[^2]: Stud, P. (2020, September 30). What is WSGI (web server gateway interface)?. Medium. https://medium.com/analytics-vidhya/what-is-wsgi-web-server-gateway-interface-ed2d290449e 

[^3]: PSYCOPG2. PyPI. (n.d.). https://pypi.org/project/psycopg2/ 

[^4]: Marshmallow. marshmallow. (n.d.). https://marshmallow.readthedocs.io/en/stable/ 

[^5]: Tran, B. (2020, December 10). Object serialization and deserialization in Python. DEV Community. https://dev.to/billtrn/object-serialization-and-deserialization-in-python-3i26#:~:text=Deserialization%20is%20the%20reverse%20process,them%20back%20into%20custom%20objects. 

[^6]: Engineer, D. A. C. (2021, February 25). Hashing in action: Understanding bcrypt. Auth0. https://auth0.com/blog/hashing-in-action-understanding-bcrypt/ 

[^7]: auth0.com. (n.d.). JSON web tokens introduction. JSON Web Token Introduction. https://jwt.io/introduction 

[^8]: Abba, I. V. (2022, October 21). What is an ORM – the meaning of object relational mapping database tools. freeCodeCamp.org. https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/ 

[^9]: Sqlalchemy. SQLAlchemy. (n.d.). https://www.sqlalchemy.org/ 

[^10]: What is postgresql?: Features: Advantages and disadvantages. EDUCBA. (2023, July 28).https://www.educba.com/what-is-postgresql/