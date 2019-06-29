from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CategoryForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired()])


class CategoryAddForm(CategoryForm):
    submit = SubmitField('添加')


class CategoryEditForm(CategoryForm):
    submit = SubmitField('编辑')
