from .. import db


class MenuModel(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR)
    module = db.Column(db.VARCHAR)
    url = db.Column(db.VARCHAR)

    @staticmethod
    def inject_test_data():
        menus = [
            {'name': '菜单管理', 'module': 'admin.menu'},
            {'name': '用户管理', 'module': 'user.admin.index'},
            {'name': '问题分类管理', 'module': 'exam.admin.category'},
            {'name': '问题管理', 'module': 'exam.admin.question'},
        ]

        for menu in menus:
            item = MenuModel(**menu)
            db.session.add(item)
            db.session.commit()
