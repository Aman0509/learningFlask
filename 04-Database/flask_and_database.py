"""
Databases with Python and Flask

- Typically, when working with any SQL database, you would need to learn SQL statements
    - SELECT * FROM some_table …
- Luckily with the aid of some useful libraries we will be able to use pure Python!
- Python and Flask can connect to a variety of SQL Database engines, including PostgreSQL, MySQL, SQLite, and more.
- SQLite is a simple SQL database engine that comes with Flask and can handle all our needs.
- SQLite (despite its name) can actually scale quite well for basic applications (100,000 hits per day).
- To connect Python, Flask, and SQL together we will need an ORM (Object Relational Mapper)
- An ORM will allow us to directly use Python instead of SQL syntax to create, edit, update, and delete from our database.
- The most common ORM for Python is SQL Alchemy
- Flask-SQLAlchemy is an extension that allows for an easy connection of Flask with SQLAlchemy
    - pip install Flask-SQLAlchemy

- To begin working with Databases, we’ll do the following
    - Set up SQLite Database in a Flask App
    - Create a Model in Flask App
    - Perform basic CRUD on our model
- To create a SQLite database
    - Create Flask App
    - Configure Flask App for SQLAlchemy
    - Pass our application into the SQLAlchemy class call

Models
- Models directly link to a table in a SQL database.
- You do not need to create the table manually with SQL.
- Instead we simply create a Model class in Python that generates the table for us!
- Similar to creating a FlaskForm, for models:
    - Create a model class
    - Inherit from db.Model
    - Optionally provide a table name
    - Add in table columns as attributes
    - Add in methods for __init__ and __repr__
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# This gives the absolute path where this file in which we are currently working is located
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Configure the database - Setting the path of our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')

# If you want to stop tracking everything that happens in the database, you can turn this off
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create an instance of the SQLAlchemy class and passing our app into it
db = SQLAlchemy(app)

# Creating a model class - Setting up a table in pur database
class Person(db.Model):

    # Setting up a table in our database - By default, table name is same as class name
    __tablename__ = "persons"

    # Setting up columns in our table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"<Person: {self.name}>"
