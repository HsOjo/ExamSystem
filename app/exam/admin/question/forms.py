from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, HiddenField, SelectField, TextAreaField
from wtforms.validators import DataRequired

QUESTION_JUDGE = 1
QUESTION_SELECT_SINGLE = 2
QUESTION_SELECT_MULTI = 3


class QuestionAddForm(FlaskForm):
    type = SelectField('类型', coerce=int, choices=list(
        {
            QUESTION_JUDGE: '判断题',
            QUESTION_SELECT_SINGLE: '单选题',
            QUESTION_SELECT_MULTI: '多选题',
        }.items()
    ))
    rank = IntegerField('难度', validators=[DataRequired()])
    title = StringField('题目', validators=[DataRequired()])
    description = TextAreaField('描述', validators=[DataRequired()])
    data = HiddenField('数据', validators=[DataRequired()])
    correct = HiddenField('正确答案', validators=[DataRequired()])
    category = SelectField('分类', coerce=int, validators=[DataRequired()])
    submit = SubmitField('添加')


class QuestionEditForm(QuestionAddForm):
    submit = SubmitField('编辑')
