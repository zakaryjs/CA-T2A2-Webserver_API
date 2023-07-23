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

### R5: Document all endpoints for your API

### R6: An ERD for your app

### R7: Detail any third party services that your app will use

### R8: Describe your projects models in terms of the relationships they have with each other

### R9: Discuss the database relations to be implemented in your application

### R10: Describe the way tasks are allocated and tracked in your project

[Trello Board](https://trello.com/invite/b/LaCoYbLG/ATTI530e5c791577751ea1a95fcc9be416a1B3DB7C3C/t2a2-webserver-api)