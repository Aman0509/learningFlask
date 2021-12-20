"""
Flashing Messages
- Often we want to send a message to the user that we don’t need to save or fix permanently to the template page.
- We can flash a message to the user that can then be closed.
- Flask makes this easy, let’s see how its done!
"""


from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class SimpleForm(FlaskForm):
    btn = SubmitField('Click Me')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        flash('You just clicked the button!')
        return redirect(url_for('index'))
    return render_template('3_home.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)