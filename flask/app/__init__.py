from flask import Flask, render_template,Blueprint
from flask_bootstrap import Bootstrap
from app.config import config
from .main import main as main_blueprint
<<<<<<< Updated upstream
=======
from app.config import Config
from app.models import db
>>>>>>> Stashed changes

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
<<<<<<< Updated upstream
    app.config.from_object(config[config_name])
    app.register_blueprint(main_blueprint)
    #config[config_name].init_app(app)

    bootstrap.init_app(app)
=======
    bootstrap.init_app(app)

    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(main_blueprint)
>>>>>>> Stashed changes

    #返回app实例对象
    return app