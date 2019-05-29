from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class MenuAddForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired()])
    module = StringField('模块', validators=[DataRequired()])
    submit = SubmitField('添加')


class MenuEditForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired()])
    module = StringField('模块', validators=[DataRequired()])
    submit = SubmitField('编辑')
