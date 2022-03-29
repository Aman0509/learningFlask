from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


# classes inheriting Resource class can define get, post, put, delete etc methods to handle API requests
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# Connecting our HelloWorld class to a route
api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    app.run(debug=True)