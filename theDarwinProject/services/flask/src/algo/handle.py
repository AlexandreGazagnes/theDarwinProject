from src import logger

from src.algo.base import _Algo
from src.algo.easy import _EasyAlgo
from src.algo.medium import _MediumAlgo
from src.algo.expert import _ExpertAlgo
from src.algo.dummy import _DummyAlgo


from flask import session


class _HandleAlgo(_Algo):
    def __init__(self, d):

        super().__init__(**d)


def _save(Obj):
    """save an algo in redis"""

    session["algo_dict"][session["current_algo"]] = Obj.serialized


def _load():
    """rebuild and return an Object from json data in redis"""

    d = session["algo_dict"][session["current_algo"]]
    logger.warning(d)
    obj = _HandleAlgo(d)
    return obj


def _dynamic_state():
    """rebuild and return an Object from json data in redis"""

    return _load().dynamic_state


def _static_state():
    """rebuild and return an Object from json data in redis"""

    return _load().static_state


def _run_1(n):
    """load run and save"""

    obj = _load()
    obj.run(n)
    _save(obj)
    return obj.dynamic_state


def _run_10(n):
    """load run and save"""

    obj = _load()
    obj.run(n * 10)
    _save(obj)
    return obj.dynamic_state


def _run_100(n):
    """load run and save"""

    obj = _load()
    obj.run(n * 100)
    _save(obj)
    return obj.dynamic_state


class algo:
    load = _load
    save = _save
    static_state = _static_state
    dynamic_state = _dynamic_state
    run_1 = _run_1
    run_10 = _run_10
    run_100 = _run_100
    DummyAlgo = _DummyAlgo
    EasyAlgo = _EasyAlgo
    MediumAlgo = _MediumAlgo
    ExpertAlgo = _ExpertAlgo


# ############################"
# # test
# ############################""


# def fakeSession():
#     """ """
#     d = {}
#     _id = "aze"
#     d["algo_dict"] = {_id: algo.DummyAlgo(_id)}
#     d["current_algo"] = _id
#     return d

# session = fakeSession()
# ag = session["algo_dict"][session["current_algo"]]

# ag.run(3)
# algo.save(ag)
