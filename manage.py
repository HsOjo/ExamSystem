from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import db, create_app
from app.admin.models import MenuModel
from app.common import check_rule_valid, json_load, json_dump
from app.exam.models import QuestionModel, CategoryModel
from app.user.models import UserModel
from config import Config

app = create_app(Config)
je = app.jinja_env.globals
je['enumerate'] = enumerate
je['MenuModel'] = MenuModel
je['CategoryModel'] = CategoryModel
je['check_rule_valid'] = check_rule_valid
je['json_load'] = json_load
je['json_dump'] = json_dump

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(
        db=db,
        MenuModel=MenuModel,
        UserModel=UserModel,
        CategoryModel=CategoryModel,
        QuestionModel=QuestionModel,
    )


manager.add_command("shell", Shell(make_context=make_shell_context))


@manager.command
def deploy():
    UserModel.inject_test_data()
    MenuModel.inject_test_data()


if __name__ == '__main__':
    manager.run()
