from flask import render_template

from . import admin
from .utils import admin_required


@admin.route('/admin')
@admin.route('/admin/index')
@admin_required
def index():
    return render_template('admin/index.html')
