from flask import render_template, request, flash, redirect, url_for

from . import admin
from .forms import MenuAddForm, MenuEditForm
from .models import MenuModel
from .utils import admin_required
from .. import db


@admin.route('/admin')
@admin.route('/admin/index')
@admin_required
def index():
    return render_template('admin/index.html')


@admin.route('/admin/menu')
@admin_required
def menu():
    menus = MenuModel.query.all()
    return render_template('admin/menu/index.html', menus=menus)


@admin.route('/admin/menu/add', methods=['GET', 'POST'])
@admin_required
def menu_add():
    form = MenuAddForm()

    if request.method == 'POST' and form.validate_on_submit():
        menu = MenuModel(name=form.name.data, module=form.module.data)

        db.session.add(menu)
        db.session.commit()
        flash('%s 添加成功！' % menu.name, 'success')

    return render_template('admin/menu/add.html', form=form)


@admin.route('/admin/menu/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def menu_edit(id):
    form = MenuEditForm()

    if request.method == 'POST' and form.validate_on_submit():
        menu = MenuModel.query.get(id)  # type: MenuModel
        menu.name = form.name.data
        menu.module = form.module.data

        db.session.add(menu)
        db.session.commit()
        flash('%s 编辑成功！' % menu.name, 'success')

    return render_template('admin/menu/edit.html', form=form)


@admin.route('/admin/menu/delete/<int:id>')
@admin_required
def menu_delete(id):
    menu = MenuModel.query.get(id)  # type: MenuModel

    db.session.delete(menu)
    db.session.commit()
    flash('%s 删除成功！' % menu.name, 'success')

    return redirect(url_for('admin.menu'))
