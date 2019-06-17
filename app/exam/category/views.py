from flask import render_template

from ..models import CategoryModel
from .. import exam_category


@exam_category.route('view/<int:id>')
def view(id):
    category = CategoryModel.query.get(id)
    return render_template('exam/category/view.html', category=category)
