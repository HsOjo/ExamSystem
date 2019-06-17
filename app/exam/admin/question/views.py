from flask import render_template, request, flash, redirect

from .forms import QuestionAddForm, QuestionEditForm
from ... import exam_admin_question
from ...models import QuestionModel, CategoryModel
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
    form.category.choices = [(category.id, category.name) for category in CategoryModel.query.all()]

    if request.method == 'POST' and form.validate_on_submit():
        question = QuestionModel(
            type=form.type.data,
            rank=form.rank.data,
            title=form.title.data,
            descroption=form.description.data,
            data=form.data.data,
            correct=form.correct.data,
            category_id=form.category.data,
        )
        db.session.add(question)
        db.session.commit()
        flash('添加成功！', 'success')

    return render_template('exam/admin/question/add.html', form=form)


@exam_admin_question.route('/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit(id):
    form = QuestionEditForm()
    form.category.choices = [(category.id, category.name) for category in CategoryModel.query.all()]
    question = QuestionModel.query.get(id)  # type: QuestionModel

    if request.method == 'POST' and form.validate_on_submit():
        question.type = form.type.data
        question.rank = form.rank.data
        question.title = form.title.data
        question.description = form.description.data
        question.data = form.data.data
        question.correct = form.correct.data
        question.category_id = form.category.data

        db.session.add(question)
        db.session.commit()
        flash('编辑成功！', 'success')
    else:
        form.type.data = question.type
        form.rank.data = question.rank
        form.title.data = question.title
        form.description.data = question.description
        form.data.data = question.data
        form.correct.data = question.correct
        form.category.data = question.category_id

    return render_template('exam/admin/question/edit.html', form=form)


@exam_admin_question.route('/delete/<int:id>')
@admin_required
def delete(id):
    question = QuestionModel.query.get(id)  # type: QuestionModel

    db.session.delete(question)
    db.session.commit()
    flash('删除成功！', 'success')

    return redirect(request.referrer)
