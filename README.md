# Plays

## Introduction

This task was completed using PostgreSQL for the database backend, Pyramid for the API server, and SQLAlchemy as the ORM. As such, the environment will require these python packages to be installed to run. They were chosen as these technologies is what the company itself uses. However, this is my first time using Pyramid and SQLAlchemy, so I kindly request that the reviewers keep this in mind when reviewing the code. :)

## Importing the data

A copy of the play data in JSON is included in this repo. The script to import this data is in `import.py` and can be executed with `python import.py`. The script makes several assumptions about the environment, such as, that there is a PostgreSQL **playapi** user set up, along with a database called **playdb** (where the data will be stored) in PostgreSQL. However, these parameters (and a couple others) can be modified in the script near the heading.
```python
DBUSER  = 'playapi'
DBPASS  = 'playapi'
DB      = 'playdb'
DBHOST  = '127.0.0.1'
DBPORT  = 5432
```

## API Server

The entry point for the API server is in `api_server/app.py` and can be started using `python api_server/app.py`. There is a `settings.json` file which contains a few parameters for the server, including the host and port the server listens on (default is 0.0.0.0:8080), and the database URL to connect to. Note: the default database URL is based on the set up assumed in the section above and if any assumptions are false, it will need to be changed accordingly.

The `models/` directory contain the ORM models used for SQLAlchemy.
The `routes.py` file defines the routes for the API server and the corresponding view.
The `views.py` file defines the functions which retrieve and return the data for its respective routes.

## API Documentation

**`/plays`**

This returns the plays that this API serves and the `playId` this API uses to identify it

**`/plays/{playId}`**

This returns all the lines in the play of `playId`

**`/plays/{playId}/act/{act}`**

This returns all the lines in a particular act of the play of `playId`

**`/plays/{playId}/act/{act}/scene/{scene}`**

This returns all the lines in a particular act and scene of the play of `playId`

**`/plays/{playId}/speaker/{speaker}`**

This returns all the lines in the play of `playId` spoken by a particular speaker
