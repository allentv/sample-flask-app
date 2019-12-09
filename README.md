# Introduction

This is a sample web application using Flask framework and SQLAlchemy to connect to a Postgres database. The whole application runs on Docker. The dependencies are available in a `requirements.txt` file which can be installed with `pip`.

## Database

The database is mounted in the local directory `data` for persistence. The credentials are mapped in the `docker-compose` file. Database migrations are available in the `migrations` folder which are created using `alembic`.

## Webapp

The application is available at `http://localhost:5000` and can use any API client to test the URLs. My preference is [Postman](https://www.getpostman.com/downloads/)
