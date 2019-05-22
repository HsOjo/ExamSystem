from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'user.login'


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)
    config.init_app(app)

    bootstrap.init_app(app)
    # 使用本地资源，禁用cdn
    bootstrap_cdns = app.extensions['bootstrap']['cdns']
    bootstrap_cdns['bootstrap'] = bootstrap_cdns['local']
    bootstrap_cdns['jquery'] = bootstrap_cdns['local']

    db.init_app(app)
    login_manager.init_app(app)

    # 在头部导入会出现闭环导入问题
    from .main import main as bp_main
    app.register_blueprint(bp_main)

    from .user import user as bp_user
    app.register_blueprint(bp_user)

    return app
