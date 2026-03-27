from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class VerifyForm(FlaskForm):
    code = StringField('Code', validators=[DataRequired(), Length(min=6, max=6)])