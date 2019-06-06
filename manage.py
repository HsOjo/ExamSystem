from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import db, create_app
from app.admin.models import MenuModel
from app.common import check_rule_valid
from app.user.models import UserModel
from config import Config

app = create_app(Config)
je = app.jinja_env.globals
je['MenuModel'] = MenuModel
je['check_rule_valid'] = check_rule_valid

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def deploy():
    UserModel.inject_test_data()
    MenuModel.inject_test_data()


if __name__ == '__main__':
    manager.run()
