from flask import Flask, render_template,Blueprint
from flask_bootstrap import Bootstrap
from .main import main as main_blueprint
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
from app.models import db
import sys

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    bootstrap.init_app(app)
    
    app.config.from_object(Config)
    db = SQLAlchemy(app)
    db.init_app(app)
    app.register_blueprint(main_blueprint)
    sys.dont_write_bytecode = True

    #返回app实例对象
    return app
