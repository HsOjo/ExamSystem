from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CategoryAddForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired()])
    submit = SubmitField('添加')
