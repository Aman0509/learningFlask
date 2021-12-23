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
from forms import AddEntry, DeleteEntry
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

    def __init__(self, title, date, content):
        self.title = title
        self.date = date
        self.content = content
    
    def __repr__(self):
        return f"Journal<'{self.date}', '{self.title}'>"


# Create Database Views

@app.route('/')
def index():
    return render_template("home.html")


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddEntry()
    if form.validate_on_submit():
        title = form.title.data
        date = dt.datetime.now()
        content = form.content.data
        new_entry = Journal(title, date, content)
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


@app.route('/list', methods=['GET', 'POST'])
def list():
    entries = Journal.query.all()
    return render_template('list.html', entries=entries)


if __name__ == "__main__":
    app.run(debug=True)