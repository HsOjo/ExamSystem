from functools import wraps

from flask import current_app, Flask
from flask_login import current_user, login_required


def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        return func(*args, **kwargs)

    return login_required(decorated_view)


def get_admin_top_modules():
    app = current_app  # type: Flask
    rules = [i.endpoint for i in list(app.url_map.iter_rules())]
    rules = list(set(rules))
    result = []
    for item in rules:
        mods = item.split('.')
        if len(mods) == 2 and mods[0] == 'admin' and '_' not in mods[1] and mods[1] != 'index':
            result.append(item)

    return result
