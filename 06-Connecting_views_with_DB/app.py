"""
Connection DB with Flask views

- We’ve finally learned enough to make a real website!
- Key Features
    - Display Templates
    - Accept User Information through Forms
    - Save Supplied Information in Database
    - Report back saved information

Troubleshoot links:
- Flask-SQLAlchemy nullable=False -> https://stackoverflow.com/questions/9844150/flask-sqlalchemy-nullable-false/9845764
"""

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddEntry, DeleteEntry, AddUser, DeleteUser
import os, datetime as dt


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


# Database Configuration

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'journalsDB.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


# Create Database Models

class Journal(db.Model):

    __tablename__ = 'journals'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, userid, title, date, content):
        self.userid = userid
        self.title = title
        self.date = date
        self.content = content
    
    def __repr__(self):
        return f"Journal<'{self.user}, {self.date}', '{self.title}'>"


class Users(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    journal_entry = db.relationship('Journal', backref='user', lazy="dynamic")

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return f"User<'{self.username}'>"

# Create Database Views

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    form = AddUser()
    if form.validate_on_submit():
        username=form.username.data
        new_user = Users(username)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('user.html', form=form)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddEntry()
    if form.validate_on_submit():
        user = form.userid.data
        title = form.title.data
        date = dt.datetime.now()
        content = form.content.data
        new_entry = Journal(user, title, date, content)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DeleteEntry()
    if form.validate_on_submit():
        id = form.id.data
        entry = Journal.query.get(id)
        db.session.delete(entry)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('delete.html', form=form)


@app.route('/deleteuser', methods=['GET', 'POST'])
def deleteuser():
    form = DeleteUser()
    if form.validate_on_submit():
        id = form.id.data
        user = Users.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('deleteuser.html', form=form)


@app.route('/list', methods=['GET', 'POST'])
def list():
    entries = Journal.query.all()
    return render_template('list.html', entries=entries)


@app.route('/listusers', methods=['GET', 'POST'])
def listusers():
    userslist = Users.query.all()
    return render_template('listusers.html', userslist=userslist)

if __name__ == "__main__":
    app.run(debug=True)