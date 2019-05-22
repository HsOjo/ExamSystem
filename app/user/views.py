from flask import request, render_template
from flask_login import login_user

from . import user
from .forms import LoginForm, RegisterForm


@user.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST' and form.validate():
        print(form.username.data, form.password.data)
        login_user()

    return render_template('user/login.html', form=form)


@user.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST' and form.validate():
        print(form.username.data, form.password.data)
        login_user()

    return render_template('user/register.html', form=form)
