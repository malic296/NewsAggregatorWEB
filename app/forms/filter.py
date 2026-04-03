from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class FilterForm(FlaskForm):
    hours = IntegerField("Hours", validators=[DataRequired()])

class ChannelFilterForm(FlaskForm):
    submit = SubmitField("Save")