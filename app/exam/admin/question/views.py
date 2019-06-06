from flask import render_template, request, flash, redirect

from .forms import QuestionAddForm, QuestionEditForm
from ... import exam_admin_question
from ...models import QuestionModel
from .... import db
from ....admin.utils import admin_required


@exam_admin_question.route('/')
@exam_admin_question.route('/index')
@admin_required
def index():
    questions = QuestionModel.query.all()
    return render_template('exam/admin/question/index.html', questions=questions)


@exam_admin_question.route('/add', methods=['GET', 'POST'])
@admin_required
def add():
    form = QuestionAddForm()

    if request.method == 'POST' and form.validate_on_submit():
        question = QuestionModel(name=form.name.data)
        db.session.add(question)
        db.session.commit()
        flash('%s 添加成功！' % question.name, 'success')

    return render_template('exam/admin/question/add.html', form=form)


@exam_admin_question.route('/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit(id):
    form = QuestionEditForm()
    question = QuestionModel.query.get(id)  # type: QuestionModel

    if request.method == 'POST' and form.validate_on_submit():
        question.name = form.name.data

        db.session.add(question)
        db.session.commit()
        flash('%s 编辑成功！' % question.name, 'success')
    else:
        form.name.data = question.name

    return render_template('exam/admin/question/edit.html', form=form)


@exam_admin_question.route('/delete/<int:id>')
@admin_required
def delete(id):
    question = QuestionModel.query.get(id)  # type: QuestionModel

    db.session.delete(question)
    db.session.commit()
    flash('%s 删除成功！' % question.name, 'success')

    return redirect(request.referrer)
