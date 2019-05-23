from .. import db


class CategoryModel(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR)

    def __init__(self, **kwargs):
        super(CategoryModel, self).__init__(**kwargs)


class AnswerModel(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    answer = db.Column(db.VARCHAR)

    def __init__(self, **kwargs):
        super(AnswerModel, self).__init__(**kwargs)


class QuestionModel(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.VARCHAR)
    rank = db.Column(db.Integer)
    data = db.Column(db.VARCHAR)
    correct = db.Column(db.VARCHAR)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def __init__(self, **kwargs):
        super(QuestionModel, self).__init__(**kwargs)
