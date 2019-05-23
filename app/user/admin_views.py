from flask import render_template, request, flash
from flask_login import login_user

from .admin_forms import UserAddForm
from .. import db
from ..admin import admin
from ..admin.utils import admin_required
from ..user.models import UserModel


@admin.route('/admin/user')
@admin.route('/admin/user/index')
@admin_required
def user():
    users = UserModel.query.all()
    return render_template('user/admin/user/index.html', users=users)


@admin.route('/admin/user/add', methods=['GET', 'POST'])
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
