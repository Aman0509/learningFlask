"""
- Often for larger projects you will have multiple Models.
- These models may have a relationship to each other.
- To understand model relationships, we need to review Primary Keys and Foreign Keys in tables.
- Primary Key
    - A Primary Key is a unique identifier for each row in a table.
- Foreign Key
    - A Foreign Key is a unique identifier for each row in another table. In other words, primary key in another table.
- Example
    - Puppy Table
        - ID Tag (Primary Key)
        - Puppy Name
    - Owner Table
        - National ID Number (Primary Key)
        - Owner Name
        - Puppy ID (Foreign Key)
- Later on we will discuss more complex relationships.
- For now, let’s work through an example of connecting 2 tables together by connecting their respective models in the application .py script.
"""


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'db.sqlite')

db = SQLAlchemy(app)

Migrate(app, db)

class Citizen(db.Model):

    __tablename__ = 'citizens'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    # One to Many --> one citizen can have one or many vehicles
    vehicle = db.relationship('Vehicle', backref='citizen', lazy='dynamic')

    # One to One --> each citizen will be issued with one driving license
    driving_license = db.relationship('DriversLicense', backref='citizen', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.driving_license:
            return f'[Product -> {self.name}, Driving License -> {self.driving_license.license_number}]'
        else:
            return f'[Product -> {self.name}, Driving License -> No license assigned]' 

    def get_vehicles(self):
        for i in self.vehicle:
            print(i.name)

    
class Vehicle(db.Model):

    __tablename__ = 'vehicles'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(128))
    name = db.Column(db.String(128))

    # connecting citizen table
    citizen_id = db.Column(db.Integer, db.ForeignKey('citizens.id'))
    

    def __init__(self, type, name, citizen_id):
        self.type = type
        self.name = name
        self.citizen_id = citizen_id


class DriversLicense(db.Model):

    __tablename__ = 'license'

    id = db.Column(db.Integer, primary_key=True)
    license_number = db.Column(db.String(128))

    # connecting citizen table
    citizen_id = db.Column(db.Integer, db.ForeignKey('citizens.id'))

    def __init__(self, license_number, citizen_id):
        self.license_number = license_number
        self.citizen_id = citizen_id