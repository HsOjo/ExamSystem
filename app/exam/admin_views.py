from flask import render_template

from .models import CategoryModel
from ..admin import admin
from ..admin.utils import admin_required


@admin.route('/admin/category')
@admin.route('/admin/category/index')
@admin_required
def category():
    categories = CategoryModel.query.all()
    return render_template('exam/admin/category/index.html', categories=categories)
