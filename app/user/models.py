from flask_login import UserMixin

from .. import db, login_manager


class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.VARCHAR, unique=True)
    password = db.Column(db.VARCHAR)
    is_admin = db.Column(db.BOOLEAN, default=False, nullable=False)

    def __init__(self, **kwargs):
        super(UserModel, self).__init__(**kwargs)

    def check_login(self, password):
        return self.password == password


@login_manager.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)
