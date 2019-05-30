from flask import render_template, request, flash, redirect, url_for

from .admin_forms import CategoryAddForm, CategoryEditForm
from .models import CategoryModel
from .. import db
from ..admin import admin
from ..admin.utils import admin_required


@admin.route('/admin/category')
@admin.route('/admin/category/index')
@admin_required
def category():
    categories = CategoryModel.query.all()
    return render_template('exam/admin/category/index.html', categories=categories)


@admin.route('/admin/category/add', methods=['GET', 'POST'])
@admin_required
def category_add():
    form = CategoryAddForm()

    if request.method == 'POST' and form.validate_on_submit():
        category = CategoryModel(name=form.name.data)
        db.session.add(category)
        db.session.commit()
        flash('%s 添加成功！' % category.name, 'success')

    return render_template('exam/admin/category/add.html', form=form)


@admin.route('/admin/category/edit/<int:id>', methods=['GET', 'POST'])
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


@admin.route('/admin/category/delete/<int:id>')
@admin_required
def category_delete(id):
    category = CategoryModel.query.get(id)  # type: CategoryModel

    db.session.delete(category)
    db.session.commit()
    flash('%s 删除成功！' % category.name, 'success')

    return redirect(request.referrer)
