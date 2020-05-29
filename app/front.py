import secrets

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
    session,
)

from flask import Blueprint

from app.forms import InitForm, RunForm
from app.utils import manage_session
from src import logger

# Blue prints
front = Blueprint("front", __name__)


# static files
@front.route("/", methods=["GET"])
def just_static():
    """just return html and css"""

    logger.debug("called")
    manage_session("/")
    initForm = InitForm(request.form)
    runForm = RunForm(request.form)
    return render_template("pages/home.html", initForm=initForm, runForm=runForm)


# test files
@front.route("/test", methods=["GET"])
def just_test():
    """just return html and css"""

    manage_session("/test")
    return render_template("pages/test.html")


@front.route("/testsessionid", methods=["GET"])
def test_session_id():

    manage_session("/testsessionid")
    logger.info(session)
    return str([(k, v) for k, v in session.items()])
