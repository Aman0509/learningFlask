from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os


# Create the application object
app = Flask(__name__)

# Create the LoginManager object
login_manager = LoginManager()

# Set up the base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Set up configuration
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

# Set up the login manager
login_manager.init_app(app)

# Configuring the login_manager with view to be executed when user is trying to log in
login_manager.login_view = "login"
