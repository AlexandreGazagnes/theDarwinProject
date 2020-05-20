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

from flask import Blueprint

from app.forms import InitForm, RunForm
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
    return render_template("home2.html", initForm=initForm, runForm=runForm)


# static files
@front.route("/2", methods=["GET"])
def just_static2():
    """just return html and css"""

    logger.debug("called")
    initForm = InitForm(request.form)
    runForm = RunForm(request.form)
    return render_template("home.html", initForm=initForm, runForm=runForm)
