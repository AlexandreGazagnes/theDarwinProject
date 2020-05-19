import secrets
from flask import Flask
from flask import render_template, redirect, escape, request, session

# from flask_scss import Scss

from params import Params
from src import *

# replace by redis in next feature
ALGO = dict()


def make_app():
    """make app """

    logger.info("called")

    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    from app.front import front
    from app.back import back

    app.register_blueprint(front)
    app.register_blueprint(back)
    # Scss(app)
    # Scss(app, static_dir="static/css", asset_dir="assets/scss")
    return app
