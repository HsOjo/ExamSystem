from flask import render_template

from .. import exam_question
from ..models import QuestionModel


@exam_question.route('view/<int:id>')
def view(id):
    question = QuestionModel.query.get(id)  # type: QuestionModel
    return render_template('exam/question/view.html', question=question)
