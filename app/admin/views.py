from flask import render_template, request, flash

from . import admin
from .forms import MenuAddForm
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
