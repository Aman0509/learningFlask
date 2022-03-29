"""
- We can use the Flask-JWT library to require authorization before being able to create a REST API call.
- Users will need to provide a username and password to an authentication page, then they will receive 
  a key they can attach to their calls.
- To install flask-jwt, use:
    pip install Flask-JWT

Implementation of JWT:
- create the JWT object and pass your flask object, authentication function, and the identity function
- a route 'auth' will be created by JWT where user can first login and receive a token
- In the header, set content-type, application/json as key value pair and then in the body, sent user ID and password as JSON data

    ```
        {
            "username":"user3",
            "password":"password3"
        }
    ```
- The JWT object will then create a token and send it back to the user
- The user will then be able to access the protected routes. For that, in the header, set Authorization as key and JWT <JWT token> as value and then sent the requested at your protected route.
"""


from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required


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
names = []

class Names(Resource):

    def get(self, name):
        for n in names:
            if n.get('name') == name:
                return n
        return {'name': f'{name} does not exist'}, 404
    
    def post(self, name):
        name = {'name': name}
        names.append(name)
        return {'status': 'created successfully'}, 201
    
    def delete(self, name):
        for i in names:
            if i.get('name') == name:
                names.pop(names.index(i))
                return {'status': f'{name} delete successfully'}, 200
        return {'name': f'{name} does not exist'}, 404


class AllNames(Resource):

    @jwt_required()
    def get(self):
        return {'names': names}


api.add_resource(Names, '/name/<string:name>')
api.add_resource(AllNames, '/names')


if  __name__ == "__main__":
    app.run(debug=True)