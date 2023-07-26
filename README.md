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

### R3: Why have you chosen this database system. What are the drawbacks compared to others?

The database system that I chose to use for this assignment is PostgreSQL. I chose this database system as it is what I am familiar with.

**Advantages**

Postgres has many features that allow for the database to be reliable, keep strong data integrity, and be easily scalable. Postgres also has extensive documentation available online, which made troubleshooting much easier.

Postgres is also fully ACID compliant, which further helps enforce and ensure data integrity and reliability. This assists for those databases with CRUD functionality in mind, ensuring that data is able to be created, modified, viewed and deleted without issue.

Postgres also supports a wide variety of data types, resulting in an overall wider range of use cases for potential applications. Furthermore, users can also define their own parameters in regards to the relations, datatypes, or the database itself, allowing for functionality to be further specialised for its particular use.

Lastly, Postgres is Open-Source, meaning that developers are able to modify parts of the code as required.

**Disadvantages**

From a performance based perspective, Postgres, in most scenarios, is slower than other alternatives such as MySQL. This is more apparent in bigger databases, due to the way that Postgres handles reading operations. This is due to the fact that Postgres was designed with compatibility and integrity as a key focus, meaning that though Postgres is more feature rich, its performance takes a hit; more noticably at a larger scale.

Postgres also has less third party support when compared with other database management systems. This results in less extensive function in comparison to others such as MySQL, which has more third party support, a larger community, and more trained professionals available.

Postgres is also more complicated in regards to the setup, which creates a larger barrier for entry, leading to the overall experience being less beginner-friendly.

### R4: Identify and discuss the key functionalities and benefits of an ORM

ORM stands for Object Relational Mapping. An ORM is a way for an application to interact with a database. 

ORMs use a programming language, instead of plain SQL, for database related commands, making it easier to create queries, and modify the entirety of the database. This also means that developers dont have to constantly switch between writing SQL, and for example, Python, and can just write in the one language. 

ORMs allow for developers to use the object oriented functions of their chosen programming language. This means that knowledge from the functions of a specific programming language can be applied in the creation of database relations, relationships and validation paramaters. 

Furthermore, ORMS have strong support for most SQL tasks. The ORM that is used in this application, SQLAlchemy, makes it easy to create, seed and drop databases. It is also really easy to change which database the application is connected to; this can be done by simply modifying the .env file.

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

### R8: Describe your projects models in terms of the relationships they have with each other

### R9: Discuss the database relations to be implemented in your application

### R10: Describe the way tasks are allocated and tracked in your project

[Trello Board](https://trello.com/invite/b/LaCoYbLG/ATTI530e5c791577751ea1a95fcc9be416a1B3DB7C3C/t2a2-webserver-api)