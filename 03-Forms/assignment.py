"""
Expand the code from the previous lecture
 - Add a string field for breed
 - Save the input to the session
 - Send a flash message to the user indicating their choice of breed
"""

from flask import Flask, render_template, session, redirect, flash, url_for    
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class SimpleForm(FlaskForm):
    mood = StringField('How are you feeling today?')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        session['mood'] = form.mood.data
        flash('Your mood is {} today'.format(session['mood']))
        return redirect(url_for('index'))
    return render_template('assignment.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)