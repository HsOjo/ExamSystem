from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import db, create_app
from config import Config

app = create_app(Config)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
