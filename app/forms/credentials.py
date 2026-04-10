from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, EqualTo

class CredentialsForm(FlaskForm):
    old_password = PasswordField("Current Password", validators=[DataRequired()])
    new_username = StringField("New Username")
    new_password = PasswordField("New Password")
    new_password_integrity = PasswordField(
        "Confirm New Password",
        validators=[EqualTo('new_password', message='Passwords must match')]
    )