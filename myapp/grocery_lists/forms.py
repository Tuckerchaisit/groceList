from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class GroceryForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    unit = StringField('Unit', validators=[DataRequired()])
    submit = SubmitField('Post')