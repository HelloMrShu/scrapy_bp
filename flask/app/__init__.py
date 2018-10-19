from flask import Flask, render_template,Blueprint
from flask_bootstrap import Bootstrap
from app.config import config
from .main import main as main_blueprint

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    bootstrap.init_app(app)

    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(main_blueprint)

    #返回app实例对象
    return app
