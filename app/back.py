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

from flask import Blueprint

from app.forms import InitForm, RunForm
from app import ALGO
from src.functs import Functs
from src import EvolutionAlgo1D, NathanAlgo
from src import logger

# Blue prints
back = Blueprint("back", __name__)


def get_algo():
    """ get algo"""
    return ALGO[request.args.get("algoId")]


# init from model
@back.route("/initfrommodel", methods=["POST"])
def initFromModel():
    """load nathan Model"""

    logger.debug("called")
    algo = NathanAlgo()
    global ALGO
    ALGO.update({algo.id: algo})
    return algo.id, 200


# init from user
@back.route("/initfromuser", methods=["POST"])
def initFromUser():
    """just create the Algo Object"""

    logger.debug("called")
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
        logger.critical("form.funct.data " + str(form.funct.data))
        logger.critical("form.objective.data " + str(form.objective.data))
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


# get functs data
@back.route("/functsdata", methods=["GET"])
def get_functs_data():
    """ """

    logger.debug("called")
    functs = Functs.as_dict
    functs = {
        k: {kk: vv for kk, vv in v.items() if "funct" not in kk}
        for k, v in functs.items()
    }
    resp = jsonify(functs)
    resp.status_code = 200
    return resp


# get static state
@back.route("/staticstate", methods=["GET"])
def get_static_state():
    """ where is the  doctstring ? """

    logger.debug("called")
    algo = get_algo()
    resp = jsonify(algo.static_state)
    # logger.critical(resp)
    resp.status_code = 200
    return resp


# get dynamic state
@back.route("/dynamicstate", methods=["GET"])
def get_dynamic_state():
    """ where is the  doctstring ? """

    logger.debug("called")
    algo = get_algo()
    resp = jsonify(algo.dynamic_state)
    resp.status_code = 200
    return resp


# run
@back.route("/run", methods=["POST"])
def run():

    logger.debug("called")
    global ALGO
    algoId = request.args.get("algoId")
    algo = ALGO[algoId]
    algo.run(1)
    return "OK", 200


@back.route("/getxlim", methods=["GET"])
def get_x_lim():

    logger.debug("called")
    algo = get_algo()
    xlim = algo.x_lim_original_population
    return jsonify(xlim), 200


@back.route("/getylim", methods=["GET"])
def get_y_lim():

    logger.debug("called")
    algo = get_algo()
    ylim = algo.y_lim_current_population
    return jsonify(ylim), 200


@back.route("/getpopulation", methods=["GET"])
def get_population():
    """get current population coordonate"""

    logger.debug("called")
    algo = get_algo()
    return jsonify(algo.graph_pop), 200


@back.route("/getxs", methods=["GET"])
def get_xs():
    """WHERE IS THE DocString ?"""

    logger.debug("called")
    algo = get_algo()
    return jsonify(algo.graph_xs_last), 200


@back.route("/getys", methods=["GET"])
def get_ys():
    """get current ys coordonate"""

    logger.debug("called")
    algo = get_algo()
    return jsonify(algo.graph_ys_last), 200


@back.route("/getyears", methods=["GET"])
def get_years():
    """get current years coordonate"""

    logger.debug("called")
    algo = get_algo()
    return jsonify(algo.graph_years_last), 200


# @back.route("/dummycall", methods=["GET"])
# def dummy_call():
#     """Use this to get various info from braowser to logs"""

#     logger.debug("called")
#     algo = get_algo()
#     logger.warning()
#     return "OK", 200
