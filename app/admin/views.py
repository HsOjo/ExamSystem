from flask import render_template, flash, redirect, url_for
from flask_login import login_user

from . import admin
from .forms import UserAddForm
from .utils import admin_required
from .. import db
from ..user.models import UserModel


@admin.route('/admin')
@admin.route('/admin/index')
@admin_required
def index():
    return render_template('admin/index.html')


@admin.route('/admin/user')
@admin_required
def user():
    users = UserModel.query.all()
    form_user_add = UserAddForm()
    return render_template('admin/user.html', users=users, form_user_add=form_user_add)


@admin.route('/admin/userAdd', methods=['POST'])
@admin_required
def user_add():
    form = UserAddForm()

    if form.validate_on_submit():
        user = UserModel.query.filter_by(username=form.username.data).first()  # type: UserModel
        if user is None:
            user = UserModel(username=form.username.data, password=form.password.data, is_admin=form.is_admin.data)
            db.session.add(user)
            db.session.commit()

            login_user(user)
            flash('%s 添加成功！' % user.username, 'success')
        else:
            flash('%s 添加失败！用户已存在。' % user.username, 'danger')

    return redirect(url_for('admin.user'))
