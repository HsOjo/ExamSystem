from flask import Blueprint

exam = Blueprint('exam', __name__)

from . import views
from . import admin_views
