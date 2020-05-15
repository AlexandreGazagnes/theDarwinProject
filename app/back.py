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
back = Blueprint("back", __name__)


def get_algo(request):
    """ get algo"""
    algoId = request.args.get("algoId")
    algo = ALGO[algoId]
    return algo


# init from model
@back.route("/initfrommodel", methods=["POST"])
def initFromModel():
    """load nathan Model"""

    logger.info("called")
    algo = NathanAlgo()
    global ALGO
    ALGO.update({algo.id: algo})
    return algo.id, 200


# init from user
@back.route("/initfromuser", methods=["POST"])
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
@back.route("/staticstate", methods=["GET"])
def get_static_state():
    """ """

    logger.info("called")
    # global ALGO
    algoId = request.args.get("algoId")
    logger.critical(f"algoId --> {algoId} ")
    algo = ALGO[algoId]
    resp = jsonify(algo.static_state)
    # logger.critical(resp)
    resp.status_code = 200
    return resp


# get dynamic state
@back.route("/dynamicstate", methods=["GET"])
def get_dynamic_state():
    """ """

    logger.info("called")
    # global ALGO
    algoId = request.args.get("algoId")
    algo = ALGO[algoId]
    resp = jsonify(algo.dynamic_state)
    resp.status_code = 200
    return resp


# run
@back.route("/run", methods=["POST"])
def run():

    logger.info("called")
    # form = RunForm(request.form)
    global ALGO
    algoId = request.args.get("algoId")
    algo = ALGO[algoId]
    algo.run(1)
    return "OK", 200


@back.route("/getxlim", methods=["GET"])
def get_x_lim():

    logger.info("called")
    # global ALGO
    algoId = request.args.get("algoId")
    algo = ALGO[algoId]
    xlim = algo.x_lim_original_population
    logger.info(xlim)
    return jsonify(xlim), 200


@back.route("/getylim", methods=["GET"])
def get_y_lim():

    logger.info("called")
    # global ALGO
    algoId = request.args.get("algoId")
    algo = ALGO[algoId]
    ylim = algo.y_lim_current_population
    logger.info(ylim)
    return jsonify(ylim), 200


@back.route("/getpopulation", methods=["GET"])
def get_population():
    """get current population coordonate"""

    logger.debug("called")
    algo = get_algo(request)
    pop = algo.pop
    return jsonify(pop), 200


@back.route("/dummycall", methods=["GET"])
def dummy_call():
    """Use this to get various info from braowser to logs"""

    logger.debug("called")
    logger.warning(ALGO)
    return "OK", 200
