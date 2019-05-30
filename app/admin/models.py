from .. import db


class MenuModel(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR)
    module = db.Column(db.VARCHAR)
    url = db.Column(db.VARCHAR)
