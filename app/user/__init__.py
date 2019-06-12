from flask import Blueprint

from ..libs.nestable_blueprint import NestableBlueprint

user = NestableBlueprint('user', __name__, template_folder='templates', static_folder='static')
user_admin = Blueprint('user.admin', __name__, template_folder='templates', static_folder='static')

user.register_blueprint(user_admin, url_prefix='/admin')

from . import views, models
from .admin import views
