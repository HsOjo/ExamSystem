from flask import Blueprint

exam = Blueprint('exam', __name__, template_folder='templates')

from . import views
from . import admin_views
