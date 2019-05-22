from flask import request, render_template, redirect, url_for, flash
from flask_login import login_required, logout_user, login_user

from . import user
from .forms import LoginForm, RegisterForm
from .models import UserModel
from .. import db


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = UserModel.query.filter_by(username=form.username.data).first()  # type: UserModel
        if user is not None and user.check_login(form.password.data):
            login_user(user)
            flash('登陆成功！欢迎回来，%s!' % user.username, 'success')
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('登录失败！用户名或密码错误。', 'danger')

    return render_template('user/login.html', form=form)


@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate_on_submit():
        user = UserModel.query.filter_by(username=form.username.data).first()  # type: UserModel
        if user is None:
            user = UserModel(username=form.username.data, password=form.password.data)
            db.session.add(user)
            db.session.commit()

            login_user(user)
            flash('注册成功！欢迎，%s。' % user.username, 'success')
            return redirect(url_for('main.index'))
        else:
            flash('注册失败！用户已存在：%s。' % user.username, 'danger')

    return render_template('user/register.html', form=form)


@user.route("/logout")
@login_required
def logout():
    logout_user()
    flash('注销成功！', 'success')
    return redirect(request.referrer)
