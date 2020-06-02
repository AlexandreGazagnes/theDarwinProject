from src import logger

from src.algo.base import _Algo
from src.functs import *


class _EasyAlgo(_Algo):
    """just a dummy algo for tests"""

    def __init__(self, _id):
        """init method """

        _funct = Functs["x2"]

        d = {
            "_id": _id,
            "year": 0,
            "funct": _funct,
            "objective": _funct["objective"],
            "interval": _funct["interval"],
            "winning_threshold": 0.005,
            "seed_parents": 12,
            "kill_rate": 0.333,
            "demography": 1,
            "average_child_numb": 0.5,
            "kill_before_reproduce": 0,
            "social_system": "normal",
            "current_population": [],
            "original_population": [],
            "_round": 7,
        }

        logger.warning(str(d))

        super().__init__(**d)
