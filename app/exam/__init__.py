from flask import Blueprint

from ..libs.nestable_blueprint import NestableBlueprint

exam = NestableBlueprint('exam', __name__, template_folder='templates', static_folder='static')
exam_admin = NestableBlueprint('exam.admin', __name__, template_folder='templates', static_folder='static')
exam_admin_category = Blueprint('exam.admin.category', __name__, template_folder='templates', static_folder='static')
exam_admin_question = Blueprint('exam.admin.question', __name__, template_folder='templates', static_folder='static')

exam_admin.register_blueprint(exam_admin_category, url_prefix='/category')
exam_admin.register_blueprint(exam_admin_question, url_prefix='/question')
exam.register_blueprint(exam_admin, url_prefix='/admin')

exam_category = Blueprint('exam.category', __name__, template_folder='templates', static_folder='static')
exam_question = Blueprint('exam.question', __name__, template_folder='templates', static_folder='static')

exam.register_blueprint(exam_category, url_prefix='/category')
exam.register_blueprint(exam_question, url_prefix='/question')

from . import views, models
from .admin.category import views
from .admin.question import views

from .category import views
