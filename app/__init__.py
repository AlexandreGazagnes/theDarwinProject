import secrets
from flask import Flask
from flask import render_template, redirect, escape, request, session

from params import Params
from src.algo_child import NathanAlgo

ALGO = dict()


def make_app():
    """make app """

    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    from app.front import front
    from app.back import back

    app.register_blueprint(front)
    app.register_blueprint(back)
    return app
