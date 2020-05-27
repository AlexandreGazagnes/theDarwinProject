import secrets
from flask import Flask
from flask import render_template, redirect, escape, request, session
from flask_login import LoginManager
from flask_session import Session

# from flask_scss import Scss

from params import Params
from src import *

# replace by redis in next feature
ALGO = dict()
sess = Session()


def make_app():
    """make app """

    logger.info("called")

    app = Flask(__name__)

    # Application Configuration
    app.config.from_object("config.DevConfig")

    # plugin
    # sess.init_app(app)

    # context manager
    with app.app_context():
        from app.front import front
        from app.back import back

        app.register_blueprint(front)
        app.register_blueprint(back)
        # Scss(app)
        # Scss(app, static_dir="static/css", asset_dir="assets/scss")
        return app
