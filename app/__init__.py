from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from app.user.forms import LoginForm, RegisterForm
from .main import main as bp_main
from .user import user as bp_user

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)

    bootstrap.init_app(app)
    # 使用本地资源，禁用cdn
    bootstrap_cdns = app.extensions['bootstrap']['cdns']
    bootstrap_cdns['bootstrap'] = bootstrap_cdns['local']
    bootstrap_cdns['jquery'] = bootstrap_cdns['local']

    # login_manager.init_app(app)

    app.register_blueprint(bp_main)
    app.register_blueprint(bp_user)

    return app
