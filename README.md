# Introduction

This is a sample web application using Flask framework and SQLAlchemy to connect to a Postgres database. The whole application runs on Docker. The dependencies are available in a `requirements.txt` file which can be installed with `pip`.

Assuming Docker and `docker-compose` are installed, run `docker-compose up` to start the web application

## Database

The database is mounted in the local directory `data` for persistence. The credentials are mapped in the `docker-compose` file. Database migrations are available in the `migrations` folder which are created using `alembic`.

Accessing the database container can be done with the command : `docker-compose exec db /bin/bash -c "psql books books-user"`

### Setting up the database

Database tables can be setup by logging into the webapp container and running the database migrations and seed script.

Database migrations can be executed by

```bash
docker-compose exec webapp /bin/bash
flask db migrate -m "Create books and requests"
flask db upgrade
```

To seed the database:

```bash
docker-compose exec db /bin/bash
psql -U $POSTGRES_USER -d $POSTGRES_DB -a -f /home/sample-flask-app/seed_db.sql
```

You can verify that the tables are setup by access the Postgres shell in the `db` container and then using the command `\dt`. You should see 2 tables : `books` and `requests`.

### Erasing the database

Delete the existing `data` folder and create an empty folder. You will have to re-seed the database to have any data.

## Webapp

The application requires Python3 and will be available at `http://localhost:5000` and can use any API client to test the URLs. My preference is [Postman](https://www.getpostman.com/downloads/)

The workspace can be setup locally for testing with

```bash
rm -rf env/
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## Test Data

`curl -i http://localhost:5000` should display `Hello World!`

Running the seed data script should load the database with 5 records in the `books` table.
