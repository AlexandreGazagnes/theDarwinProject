import json
import time

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

# Blue prints
home = Blueprint("home", __name__)


# static files
@home.route("/", methods=["GET"])
def just_static():
    """just return html and css"""

    logger.info("called")
    initForm = InitForm(request.form)
    runForm = RunForm(request.form)
    return render_template("home.html", initForm=initForm, runForm=runForm)


# init from model
@home.route("/initfrommodel", methods=["POST"])
def initFromModel():
    """load nathan Model"""

    logger.info("called")
    algo = NathanAlgo()
    global ALGO
    ALGO.update({algo.id: algo})
    return algo.id, 200


# init from user
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
        algo = EvolutionAlgo1D(
            funct=Functs.as_dict[form.funct.data],
            objective=form.objective.data,
            interval=[form.interval_down.data, form.interval_up.data],
            seed_parents=form.seed_parents.data,
            kill_rate=form.kill_rate.data,
            average_child_numb=form.average_child_numb.data,
        )
        global ALGO
        ALGO.update({algo.id: algo})
        return algo.id, 200

    logger.info("Error")
    return "Error", 500


# get static state
@home.route("/staticstate", methods=["GET"])
def static_state():
    """ """

    logger.info("called")
    global ALGO
    algoId = request.args.get("algoId")
    logger.critical(f"algoId --> {algoId} ")
    algo = ALGO[algoId]
    resp = jsonify(algo.static_state)
    # logger.critical(resp)
    resp.status_code = 200
    return resp


# get dynamic state
@home.route("/dynamicstate", methods=["GET"])
def dynamic_state():
    """ """

    logger.info("called")
    global ALGO
    algoId = request.args.get("algoId")
    algo = ALGO[algoId]
    resp = jsonify(algo.dynamic_state)
    resp.status_code = 200
    return resp


# run
@home.route("/run", methods=["POST"])
def run():

    logger.info("called")
    # form = RunForm(request.form)
    global ALGO
    algoId = request.args.get("algoId")
    algo = ALGO[algoId]
    algo.run(1)
    return "OK", 200


@home.route("/getxlim", methods=["GET"])
def get_x_lim():

    logger.info("called")
    global ALGO
    algoId = request.args.get("algoId")
    algo = ALGO[algoId]
    xlim = algo.x_lim_original_population
    logger.info(xlim)
    return jsonify(xlim), 200


@home.route("/getylim", methods=["GET"])
def get_y_lim():

    logger.info("called")
    global ALGO
    algoId = request.args.get("algoId")
    algo = ALGO[algoId]
    ylim = algo.y_lim_current_population
    logger.info(ylim)
    return jsonify(ylim), 200


@home.route("/getpopulation", methods=["GET"])
def get_population():

    logger.info("called")
    global ALGO
    global ALGO
    algoId = request.args.get("algoId")
    algo = ALGO[algoId]
    pop = algo.pop
    return jsonify(pop), 200
    # @home.route("/plotpopulation", methods=["POST"])
    # def plotpopulation():
    #     logger.info("called")
    #     # form = RunForm(request.form)
    #     global ALGO
    #     ALGO.plot_population()
    #     population_image = ALGO.population_images[-1].replace("app/", "")
    #     return population_image, 200
    # @home.route("/plotlearning", methods=["POST"])
    # def plotlearning():
    #     logger.info("called")
    #     # form = RunForm(request.form)
    #     global ALGO
    #     ALGO.plot_learning()
    #     learning_image = ALGO.learning_images[-1].replace("app/", "")
    return learning_image, 200


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


# @home.route("/dummycall/", methods=["GET"])
# def dummy_call():

#     global ALGO
#     logger.info("called")
#     data = request.args.get("id", "ERROR")
#     logger.warning(data)
#     logger.warning(ALGO)

#     return "OK", 200
