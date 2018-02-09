from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)

    # creating configuration options
    app.config.from_object(config_options[config_name])

    # initializing extensions
    db.init_app(app)

    return app
