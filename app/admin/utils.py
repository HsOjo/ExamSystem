from functools import wraps

from flask import current_app
from flask_login import current_user, login_required


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)

    return login_required(decorated_view)
