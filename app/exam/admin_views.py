from flask import render_template, request, flash, redirect

from .admin_forms import CategoryAddForm, CategoryEditForm, QuestionAddForm, QuestionEditForm
from .models import CategoryModel, QuestionModel
from .. import db
from ..admin import admin
from ..admin.utils import admin_required


@admin.route('/exam/category')
@admin.route('/exam/category/index')
@admin_required
def category():
    categories = CategoryModel.query.all()
    return render_template('exam/admin/category/index.html', categories=categories)


@admin.route('/exam/category/add', methods=['GET', 'POST'])
@admin_required
def category_add():
    form = CategoryAddForm()

    if request.method == 'POST' and form.validate_on_submit():
        category = CategoryModel(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        flash('%s 添加成功！' % category.name, 'success')

    return render_template('exam/admin/category/add.html', form=form)


@admin.route('/exam/category/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def category_edit(id):
    form = CategoryEditForm()
    category = CategoryModel.query.get(id)  # type: CategoryModel

    if request.method == 'POST' and form.validate_on_submit():
        category.name = form.name.data

        db.session.add(category)
        db.session.commit()
        flash('%s 编辑成功！' % category.name, 'success')
    else:
        form.name.data = category.name

    return render_template('exam/admin/category/edit.html', form=form)


@admin.route('/exam/category/delete/<int:id>')
@admin_required
def category_delete(id):
    category = CategoryModel.query.get(id)  # type: CategoryModel

    db.session.delete(category)
    db.session.commit()
    flash('%s 删除成功！' % category.name, 'success')

    return redirect(request.referrer)


@admin.route('/exam/question')
@admin.route('/exam/question/index')
@admin_required
def question():
    questions = QuestionModel.query.all()
    return render_template('exam/admin/question/index.html', questions=questions)


@admin.route('/exam/question/add', methods=['GET', 'POST'])
@admin_required
def question_add():
    form = QuestionAddForm()

    if request.method == 'POST' and form.validate_on_submit():
        question = QuestionModel(name=form.name.data)
        db.session.add(question)
        db.session.commit()
        flash('%s 添加成功！' % question.name, 'success')

    return render_template('exam/admin/question/add.html', form=form)


@admin.route('/exam/question/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def question_edit(id):
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


@admin.route('/exam/question/delete/<int:id>')
@admin_required
def question_delete(id):
    question = QuestionModel.query.get(id)  # type: QuestionModel

    db.session.delete(question)
    db.session.commit()
    flash('%s 删除成功！' % question.name, 'success')

    return redirect(request.referrer)
