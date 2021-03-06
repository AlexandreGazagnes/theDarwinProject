from src import logger

from src.algo.base import _Algo
from src.functs import *


class _DummyAlgo(_Algo):
    """just a dummy algo for tests"""

    def __init__(self, id):
        """init method """

        d = {
            "_id": id,
            "year": 0,
            "funct": Functs["x2"],
            "objective": "min",
            "interval": [-100, 100],
            "winning_threshold": 0.005,
            "seed_parents": 12,
            "kill_rate": 0.33,
            "demography": 1,
            "dimension": "1D",
            "level": "easy",
            "average_child_numb": 0.5,
            "kill_before_reproduce": 1,
            "social_system": "normal",
            "current_population": [],
            "learning_curve": [],
            "original_population": [],
            "_round": 7,
            "is_won": 0,
            "won_year": -1,
            "kill_number": -1,
            "saved_people": -1,
            "new_people_number": -1,
            "new_people_composition": {},
        }

        logger.warning(str(d))

        super().__init__(**d)
