from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import db, create_app
from app.admin.models import MenuModel
from config import Config

app = create_app(Config)
je = app.jinja_env.globals
je['MenuModel'] = MenuModel

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
