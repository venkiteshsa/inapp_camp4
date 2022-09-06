from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, InputRequired

class RegistrationForm(FlaskForm):
    ''' Login form '''

    username = StringField('username', validators=
        [InputRequired(message="Username required"), 
        Length(min=4, max=25, message="Username must be between 4 and 25 characters")])
    password = PasswordField('password', validators=
        [InputRequired(message="Password required"), 
        Length(min=7, max=25, message="Password must be between 7 and 25 characters")])
    submit_button = SubmitField('Login')