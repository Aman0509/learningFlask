from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


##########################################################################
# Creating sample user database to demonstrate token auth with Flask-JWT #
##########################################################################

class User():

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'User {self.username}'


users = [
            User(1, 'user1', 'password1'),
            User(2, 'user2', 'password2'),
            User(3, 'user3', 'password3'),
        ]

username_table = {u.username: u for u in users}
username_id_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and user.password == password:
        return user

def identity(payload):
    user_id = payload['identity']
    return username_id_table.get(user_id, None)


#######################
# Flask API Endpoints #
#######################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
api = Api(app)
jwt = JWT(app, authenticate, identity)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


# Create a Model class for names

class NameDB(db.Model):

    name = db.Column(db.String(80), primary_key=True)

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name}



class Names(Resource):

    def get(self, name):
        name_in_db = NameDB.query.filter_by(name=name).first()
        if name_in_db:
            return name_in_db.json()
        return {'name': f'{name} does not exist'}, 404
    
    def post(self, name):
        name_in_db = NameDB(name)
        db.session.add(name_in_db)
        db.session.commit()
        return {'status': 'created successfully'}, 201
    
    def delete(self, name):
        name_in_db = NameDB.query.filter_by(name=name).first()
        if name_in_db:
            db.session.delete(name_in_db)
            db.session.commit()
            return {'status': f'{name} deleted successfully'}, 200
        return {'name': f'{name} does not exist'}, 404


class AllNames(Resource):

    # @jwt_required()
    def get(self):
        names = NameDB.query.all()
        return [name.json() for name in names]

api.add_resource(Names, '/name/<string:name>')
api.add_resource(AllNames, '/names')


if  __name__ == "__main__":
    app.run(debug=True)