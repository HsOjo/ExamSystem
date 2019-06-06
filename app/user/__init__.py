from flask import Blueprint

from ..libs.nestable_blueprint import NestableBlueprint

user = NestableBlueprint('user', __name__, template_folder='templates')
user_admin = Blueprint('user_admin', __name__, template_folder='templates')

user.register_blueprint(user_admin, url_prefix='/admin')

from . import views, models
from .admin import views
