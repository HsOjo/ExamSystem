from flask import Blueprint

from ..libs.nestable_blueprint import NestableBlueprint

exam = NestableBlueprint('exam', __name__, template_folder='templates')
exam_admin = NestableBlueprint('exam_admin', __name__, template_folder='templates')
exam_admin_category = Blueprint('exam_admin_category', __name__, template_folder='templates')
exam_admin_question = Blueprint('exam_admin_question', __name__, template_folder='templates')

exam_admin.register_blueprint(exam_admin_category, url_prefix='/category')
exam_admin.register_blueprint(exam_admin_question, url_prefix='/question')
exam.register_blueprint(exam_admin, url_prefix='/admin')

from . import views, models
from .admin.category import views
from .admin.question import views
