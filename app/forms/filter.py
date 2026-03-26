from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired

class FilterForm(FlaskForm):
    hours = IntegerField('Hours', validators=[DataRequired()])