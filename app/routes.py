import json


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

from app import ALGO

from src.functs import Functs
from src import EvolutionAlgo1D, NathanAlgo
from src import logger

home = Blueprint("home", __name__)


@home.route("/", methods=["GET"])
def just_static():
    """just return html and css"""

    logger.info("called")
    initForm = InitForm(request.form)
    runForm = RunForm(request.form)
    return render_template("home.html", initForm=initForm, runForm=runForm)


@home.route("/initfrommodel", methods=["POST"])
def initFromModel():
    """load nathan Model"""

    logger.info("called")
    global ALGO
    ALGO = NathanAlgo()

    print(ALGO.as_dict)
    print(type(ALGO.as_dict))
    # data = {"data": ALGO.as_dict}
    # resp = jsonify(data)
    # resp.status_code = 200
    # return resp
    return str(ALGO.as_dict)


@home.route("/initfromuser", methods=["POST"])
def initFromUser():
    """just create the Algo Object"""

    logger.info("called")
    form = InitForm(request.form)

    # feats = [
    #     "funct",
    #     "objective",
    #     "interval_up",
    #     "interval_down",
    #     "seed_parents",
    #     "kill_rate",
    #     "average_child_numb",
    # ]
    # for f in feats:
    #     _val = getattr(form, f).data
    #     print(f"{f} : {type(_val)} is {_val} ")

    # print(request.method)

    if request.method == "POST":
        global ALGO
        ALGO = EvolutionAlgo1D(
            funct=Functs.as_dict[form.funct.data],
            objective=form.objective.data,
            interval=[form.interval_down.data, form.interval_up.data],
            seed_parents=form.seed_parents.data,
            kill_rate=form.kill_rate.data,
            average_child_numb=form.average_child_numb.data,
        )

        print(ALGO.as_dict)
        print(type(ALGO.as_dict))
        # data = {"data": ALGO.as_dict}
        # resp = jsonify(data)
        # resp.status_code = 200
        # return resp
        return str(ALGO.as_dict)

    return "error"


# @home.route("/state", methods=["GET"])
# def return_state():
#     """ """

#     global ALGO
#     return ALGO.as_dict


# @home.route("/run", methods=["GET", "POST"])
# def run():

#     form = RunForm(request.form)
#     global ALGO
#     print(ALGO)

#     if request.method == "POST":
#         ALGO.run(1)
#         ALGO.plot_population()
#         ALGO.plot_learning()
#         return redirect(url_for("home.run"))

#     algo = str(ALGO)
#     pop = str(ALGO.current_population[:10])
#     learning_image = ALGO.learning_images[-1].replace("app/", "")
#     population_image = ALGO.population_images[-1].replace("app/", "")
#     return render_template(
#         "run.html",
#         algo=algo,
#         pop=pop,
#         form=form,
#         learning_image=learning_image,
#         population_image=population_image,
#     )


# @home.route("/hello", methods=["GET"])
# def ajax_hello():
#     return "hello world"
