from .. import db


class CategoryModel(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR)
    questions = db.relationship('QuestionModel', backref='category')

    def __init__(self, **kwargs):
        super(CategoryModel, self).__init__(**kwargs)

    @staticmethod
    def inject_test_data():
        categories = [
            {'name': '第一章'},
            {'name': '第二章'},
        ]

        for category in categories:
            item = CategoryModel(**category)
            db.session.add(item)
            db.session.commit()


class QuestionModel(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.Integer)
    rank = db.Column(db.Integer)
    title = db.Column(db.VARCHAR)
    description = db.Column(db.VARCHAR)
    data = db.Column(db.VARCHAR)
    correct = db.Column(db.VARCHAR)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __init__(self, **kwargs):
        super(QuestionModel, self).__init__(**kwargs)


class AnswerModel(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    answer = db.Column(db.VARCHAR)

    def __init__(self, **kwargs):
        super(AnswerModel, self).__init__(**kwargs)
