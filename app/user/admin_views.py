from flask import render_template, request, flash, redirect
from flask_login import login_user

from .admin_forms import UserAddForm, UserEditForm
from .. import db
from ..admin import admin
from ..admin.utils import admin_required
from ..user.models import UserModel


@admin.route('/user')
@admin.route('/user/index')
@admin_required
def user():
    users = UserModel.query.all()
    return render_template('user/admin/user/index.html', users=users)


@admin.route('/user/add', methods=['GET', 'POST'])
@admin_required
def user_add():
    form = UserAddForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = UserModel.query.filter_by(username=form.username.data).first()  # type: UserModel
        if user is None:
            user = UserModel(username=form.username.data, password=form.password.data, is_admin=form.is_admin.data)
            db.session.add(user)
            db.session.commit()

            login_user(user)
            flash('%s 添加成功！' % user.username, 'success')
        else:
            flash('%s 添加失败！用户已存在。' % user.username, 'danger')

    return render_template('user/admin/user/add.html', form=form)


@admin.route('/user/edit/<int:id>', methods=['GET', 'POST'])
@admin_required
def user_edit(id):
    form = UserEditForm()
    user = UserModel.query.get(id)  # type: UserModel

    if request.method == 'POST' and form.validate_on_submit():
        user.username = form.username.data
        user.password = form.password.data
        user.is_admin = form.is_admin.data

        db.session.add(user)
        db.session.commit()
        flash('%s 编辑成功！' % user.name, 'success')
    else:
        form.username.data = user.username
        form.password.data = user.password
        form.is_admin.data = user.is_admin

    return render_template('user/admin/user/edit.html', form=form)


@admin.route('/user/delete/<int:id>')
@admin_required
def user_delete(id):
    user = UserModel.query.get(id)  # type: UserModel

    db.session.delete(user)
    db.session.commit()
    flash('%s 删除成功！' % user.name, 'success')

    return redirect(request.referrer)
