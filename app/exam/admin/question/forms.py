from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, HiddenField
from wtforms.validators import DataRequired


class QuestionAddForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired()])
    rank = IntegerField('难度')
    data = HiddenField('数据')
    correct = HiddenField('正确答案')
    category_id = HiddenField('分类id')
    submit = SubmitField('添加')


class QuestionEditForm(FlaskForm):
    name = StringField('名称', validators=[DataRequired()])
    submit = SubmitField('编辑')
