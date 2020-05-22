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
    return render_template("pages/home.html", initForm=initForm, runForm=runForm)


# test files
@front.route("/test", methods=["GET"])
def just_test():
    """just return html and css"""

    return render_template("test.html")
