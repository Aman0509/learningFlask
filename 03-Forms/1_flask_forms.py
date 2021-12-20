"""
- Let’s explore how we can use the flask_wtf and the wtforms packages to quickly create forms from our flask python scripts.
- First let’s discuss the main components to creating a form.
- Configure a secret key for security purposes.
  - Create Fields for each part of the form
- Set up a View Function
  - Add methods = [‘GET’,’POST’]
  - Create an instance of Form Class
  - Handle form submission
"""

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

# Configure a secret SECRET_KEY
# this is to prevent cross site request forgery attacks
# and is used to sign the session cookie
# Later, better way will be discussed to implement this
app.config['SECRET_KEY'] = 'mysecretkey'

class MoodForm(FlaskForm):
    mood = StringField('What is your mood today?')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MoodForm()
    mood = False
    if form.validate_on_submit():
        mood = form.mood.data
        form.mood.data = ''
    return render_template('1_home.html', form=form, mood=mood)

if __name__ == "__main__":
    app.run(debug=True)