import secrets
from flask import Flask
from flask import render_template, redirect, escape, request, session
from flask_login import LoginManager
from flask_session import Session
from flask_bcrypt import Bcrypt

# from flask_scss import Scss

from params import Params
from src import *
from app.config import ProdConfig, DevConfig

# replace by redis in next feature

sess = Session()
bcrypt = Bcrypt()


def create_app(config_class=DevConfig):
    """make app """

    logger.debug("called")

    app = Flask(__name__)

    # Application Configuration
    app.config.from_object(ProdConfig)

    # plugin
    sess.init_app(app)
    # bcrypt.init_app(app)

    # context manager
    with app.app_context():
        from app.front import front
        from app.back import back

        app.register_blueprint(front)
        app.register_blueprint(back)
        # Scss(app)
        # Scss(app, static_dir="static/css", asset_dir="assets/scss")
        return app
