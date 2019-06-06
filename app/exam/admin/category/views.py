from flask import render_template, request, flash, redirect

from .forms import CategoryAddForm, CategoryEditForm
from ... import exam_admin_category
from ...models import CategoryModel
from .... import db
from ....admin.utils import admin_required


@exam_admin_category.route('/')
@exam_admin_category.route('/index')
@admin_required
def index():
    categories = CategoryModel.query.all()
    return render_template('exam/admin/category/index.html', categories=categories)


@exam_admin_category.route('/add', methods=['GET', 'POST'])
@admin_required
def add():
    form = CategoryAddForm()

    if request.method == 'POST' and form.validate_on_submit():
        category = CategoryModel(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        flash('%s 添加成功！' % category.name, 'success')

    return render_template('exam/admin/category/add.html', form=form)


@exam_admin_category.route('/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def edit(id):
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


@exam_admin_category.route('/delete/<int:id>')
@admin_required
def delete(id):
    category = CategoryModel.query.get(id)  # type: CategoryModel

    db.session.delete(category)
    db.session.commit()
    flash('%s 删除成功！' % category.name, 'success')

    return redirect(request.referrer)
