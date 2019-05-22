from .. import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, default=10000)
    username = db.Column(db.VARCHAR, unique=True)
    password = db.Column(db.VARCHAR, unique=True)
