from flask import Flask, render_template,Blueprint
from flask_bootstrap import Bootstrap
from .main import main as main_blueprint
from flask_sqlalchemy import SQLAlchemy
from app.config import Config


bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(main_blueprint)
    #config[config_name].init_app(app)

    bootstrap.init_app(app)
    db = SQLAlchemy(app)

    # 返回app实例对象
    return app