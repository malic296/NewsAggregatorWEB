from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields import PasswordField, StringField

class LoginForm(FlaskForm):
    credential = StringField('Username/Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class VerifyForm(FlaskForm):
    code = StringField('Code', validators=[DataRequired(), Length(min=6, max=6)])