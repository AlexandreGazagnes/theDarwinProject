from src import logger

from src.algo.algo_base import _Algo
from src.functs import *


class DummyAlgo(_Algo):
    """just a dummy algo for tests"""

    def __init__(self):
        """init method """

        d = {
            "_id": "fghjkl",
            "year": 0,
            "funct": Functs["x2"],
            "objective": "min",
            "interval": [-100, 100],
            "winning_threshold": 0.005,
            "seed_parents": 10,
            "kill_rate": 0.333,
            "demography": 1,
            "dimension": "1D",
            "level": "easy",
            "average_child_numb": 0.75,
            "kill_before_reproduce": 0,
            "social_system": "normal",
            "current_population": [],
            "learning_curve": [],
            "original_population": [],
            "_round": 7,
        }

        logger.warning(str(d))

        super().__init__(**d)
