from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#creating the form class inheriting from FlaskForm
class NameForm(FlaskForm):
    #StringField class represents the text input field of html
    #creating the object for the class StringField and have validators attached
    name = StringField('Enter your name', validators=[DataRequired()])
    #StringField class represents the input type submit of html
    submit = SubmitField('Submit')