from flask import render_template, request, flash, redirect

from . import admin
from .forms import MenuAddForm, MenuEditForm
from .models import MenuModel
from .utils import admin_required
from .. import db
from ..common import check_rule_valid


@admin.route('/')
@admin.route('/index')
@admin_required
def index():
    return render_template('admin/index.html')


@admin.route('/menu')
@admin_required
def menu():
    menus = MenuModel.query.all()
    return render_template('admin/menu/index.html', menus=menus)


@admin.route('/menu/add', methods=['GET', 'POST'])
@admin_required
def menu_add():
    form = MenuAddForm()

    if request.method == 'POST' and form.validate_on_submit():
        if check_rule_valid(form.module.data) or form.module.data == '':
            menu = MenuModel(name=form.name.data, module=form.module.data, url=form.url.data)

            db.session.add(menu)
            db.session.commit()
            flash('%s 添加成功！' % menu.name, 'success')
        else:
            flash('%s 添加失败！不存在该模块。' % form.module.data, 'danger')

    return render_template('admin/menu/add.html', form=form)


@admin.route('/menu/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def menu_edit(id):
    form = MenuEditForm()
    menu = MenuModel.query.get(id)  # type: MenuModel

    if request.method == 'POST' and form.validate_on_submit():
        if check_rule_valid(form.module.data) or form.module.data == '':
            menu.name = form.name.data
            menu.module = form.module.data
            menu.url = form.url.data

            db.session.add(menu)
            db.session.commit()
            flash('%s 编辑成功！' % menu.name, 'success')
        else:
            flash('%s 编辑失败！不存在该模块。' % form.module.data, 'danger')
    else:
        form.name.data = menu.name
        form.module.data = menu.module
        form.url.data = menu.url

    return render_template('admin/menu/edit.html', form=form)


@admin.route('/menu/delete/<int:id>')
@admin_required
def menu_delete(id):
    menu = MenuModel.query.get(id)  # type: MenuModel

    db.session.delete(menu)
    db.session.commit()
    flash('%s 删除成功！' % menu.name, 'success')

    return redirect(request.referrer)
