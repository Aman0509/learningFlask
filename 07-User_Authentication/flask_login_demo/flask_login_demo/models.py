from flask_login_demo import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


# To redirect the user to their profile page after successful login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# UserMixin has all those features to related to handling user login and authorization
class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
    
    def __repr__(self):
        return '<User {}-{}-{}>'.format(self.username, self.email, self.password)
    
    def check_password(self, password_entered):
        return check_password_hash(self.password, password_entered)

