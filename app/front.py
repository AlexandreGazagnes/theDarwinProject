# import json
# import time

from flask import (
    Flask,
    escape,
    request,
    flash,
    url_for,
    render_template,
    Response,
    abort,
    redirect,
    jsonify,
)

# from flask import session, Session
#
# from flask_sqlalchemy import SQLAlchemy
# # from flask.ext.session import Session
# from flask_bcrypt import Bcrypt
# from flask_login import LoginManager, UserMixin
# from flask_mail import Mail

from flask import Blueprint

from app.forms import InitForm, RunForm

# from app import ALGO
# from src.functs import Functs
# from src import EvolutionAlgo1D, NathanAlgo
from src import logger

# Blue prints
front = Blueprint("front", __name__)


# static files
@front.route("/", methods=["GET"])
def just_static():
    """just return html and css"""

    logger.debug("called")
    initForm = InitForm(request.form)
    runForm = RunForm(request.form)
    return render_template("home.html", initForm=initForm, runForm=runForm)
