from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateTimeField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class AddEntry(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')


class DeleteEntry(FlaskForm):
    id = IntegerField('ID')
    submit = SubmitField('Delete')