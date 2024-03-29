from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

# DB config
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)

# Login Config
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

from blogWebsite.home.views import home
from blogWebsite.users.views import users
from blogWebsite.blogs.views import blogs
from blogWebsite.error_pages.handlers import error_pages

app.register_blueprint(home)
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(blogs, url_prefix='/blogs')
app.register_blueprint(error_pages)