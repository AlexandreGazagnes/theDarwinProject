import secrets
import json

from collections import Iterable

from abc import ABC
from math import cos, sin, pi, exp, sqrt

from src.functs import Functs
from src import logger

import numpy as np


class _Algo(ABC):
    """ ABC Algo"""

    def __init__(
        self,
        _id: str,
        year: int,
        funct: str,
        objective: str,
        interval: list,
        winning_threshold: float,
        seed_parents: int,
        kill_rate: float,
        demography: float,
        average_child_numb: float,
        kill_before_reproduce: int,
        social_system: str,
        current_population: list,
        original_population: list,
        _round: int = 7,
    ):
        """init method """

        self._id = _id
        self.year = year
        self.funct = funct
        self.objective = objective
        self.interval = interval
        self.winning_threshold = winning_threshold
        self.seed_parents = seed_parents
        self.kill_rate = kill_rate
        self.demography = demography
        self.average_child_numb = average_child_numb
        self.kill_before_reproduce = kill_before_reproduce
        self.social_system = social_system
        self.current_population = current_population
        self.original_population = original_population
        self._round = _round
