"""
Form Fields
- Every possible HTML form field has a corresponding wtforms class you can import
- wtforms also has validators you can easily insert.
- Validators can perform checks on the form data, such as requiring a field to be filled
- We will also show how to use Flask’s session object to grab the information provided in the form and pass it to another template.
- Keep in mind, we will later on save this information once we understand databases with Flask.
"""


from random import choice, choices
from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField,
                    SelectField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

# Create a class that will be used to create the forms
# Later we will see how we can define forms in a separate file
class InfoForm(FlaskForm):
    name = StringField('What\'s your name?', validators=[DataRequired()])
    sub = BooleanField('Subscribe to our newsletter?')
    gender = RadioField('What\'s your gender?', choices=[('male', 'Male'), ('female', 'Female'), ('closed', 'prefer not to say')])
    relationshipStatus = SelectField('What\'s your relationship status?', choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('open', 'Open Relationship'), ('closed', 'Closed Relationship'), ('complicated', 'It\'s complicated'), ('separated', 'Separated'), ('widowed', 'Widowed'), ('closed', 'Prefer not to say')])
    birthDate = DateTimeField('When\'s your birthdate?', format='%Y-%m-%d')
    bio = TextAreaField('Tell us about yourself')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['sub'] = form.sub.data
        session['gender'] = form.gender.data
        session['relation'] = form.relationshipStatus.data
        session['birthday'] = form.birthDate.data
        session['bio'] = form.bio.data
        
        return redirect(url_for('thankyou'))

    return render_template('2_home.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('2_thankyou.html')

if __name__ == "__main__":
    app.run(debug=True)