from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class FilterForm(FlaskForm):
    hours = StringField("Hours", validators=[DataRequired()])

class ChannelFilterForm(FlaskForm):
    submit = SubmitField("Save")