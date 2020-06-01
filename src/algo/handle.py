from src import logger

from src.algo.easy import _EasyAlgo
from src.algo.medium import _MediumAlgo
from src.algo.expert import _ExpertAlgo
from src.algo.dummy import _DummyAlgo


from flask import session


class HandleAlgo(_Algo):
    def __init__(self, d):

        super().__init__(**d)


def _save(Obj):
    """save an algo in redis"""

    session["algo_dict"][session["current_algo"]] = Obj.serialized


def _load():
    """rebuild and return an Object from json data in redis"""

    _id = session["current_algo"]
    d = algo_dict[_id]
    algo = HandleAlgo(**d)
    return algo


def _run_1(id, n):
    """load run and save"""

    algo = _load()
    algo.run(n)
    _save(algo)


def _run_10(id, n):
    """load run and save"""

    algo = _load()
    algo.run(n * 10)
    _save(algo)


def _run_100(id, n):
    """load run and save"""

    algo = _load()
    algo.run(n * 100)
    _save(algo)


class algo:
    load = _load
    save = _save
    run_1 = _run_1
    run_10 = _run_10
    run_100 = _run_100
    DummyAlgo = _DummyAlgo
    EasyAlgo = _EasyAlgo
    MediumAlgo = _MediumAlgo
    ExpertAlgo = _ExpertAlgo
