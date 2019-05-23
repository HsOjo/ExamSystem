from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import db, create_app
from app.admin.utils import get_admin_left_list
from config import Config

app = create_app(Config)
je = app.jinja_env.globals
je['get_admin_left_list'] = get_admin_left_list

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
