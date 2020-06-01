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

    TEMPLATE_INTERVAL = 1000
    SERIALIZED_KEYS = [
        "_id",
        "year",
        "funct",
        "objective",
        "interval",
        "dimension",
        "level",
        "winning_threshold",
        "seed_parents",
        "kill_rate",
        "demography",
        "average_child_numb",
        "kill_before_reproduce",
        "social_system",
        "current_population",
        "learning_curve",
        "original_population",
        "_round",
    ]

    def __init__(
        self,
        _id: str,
        year: int,
        funct: str,
        objective: str,
        interval: list,
        dimension: str,
        level: str,
        winning_threshold: float,
        seed_parents: int,
        kill_rate: float,
        demography: float,
        average_child_numb: float,
        kill_before_reproduce: int,
        social_system: str,
        current_population: list,
        learning_curve: list,
        original_population: list,
        _round: int = 7,
    ):
        """init method """

        logger.debug("called")

        self._id = _id
        self.year = year
        self.funct = funct
        self._funct = eval(self.funct["funct"])
        self.objective = objective
        self.interval = interval
        self.dimension = dimension
        self.level = level
        self.winning_threshold = winning_threshold
        self.seed_parents = seed_parents
        self.kill_rate = kill_rate
        self.demography = demography
        self.average_child_numb = average_child_numb
        self.kill_before_reproduce = kill_before_reproduce
        self.social_system = social_system
        self.current_population = current_population
        self.learning_curve = learning_curve
        self.original_population = original_population
        self._round = _round

        # year 0, init pop
        if not self.year:
            parents = [
                np.random.rand() + np.random.randint(*interval)
                for _ in range(seed_parents)
            ]

            # logger.warning(f"type : {type(parents)} --> {parents}")

            self.current_population = [
                (
                    round(x, self._round),  # x
                    round(self._funct(x), self._round),  # y
                    "first",  # class
                    self.year,  # birth year
                )
                for x in parents
            ]
            self.original_population = [
                (i, j, k, l) for i, j, k, l in self.current_population
            ]




    ####################################################
    # PROPERTIES
    ####################################################

    @property
    def len_current_population(self):
        """count  numb of people in current pop"""

        logger.debug("called")
        return len(self.current_population)

    @property
    def repartition_current_population(self):
        """render a dict with first, random and normal child"""

        logger.debug("called")
        l = [i[2] for i in self.current_population]
        return {k: l.count(k) for k in set(l)}

    @property
    def best_current_population(self):
        """render the best elem of the pop """

        logger.debug("called")
        self._sort_current_population()
        return self.current_population[:1]

    @property
    def is_won(self) : 
        """ eval if best  elem in wining threshold interval""" 

        logger.debug("called")
        target = float(self.funct.["target"])
        target_interval = [target * (1-self.winning_threshold), target * (1+ self.winning_threshold)]
        is_won = target_interval[1] > best_current_population > target_interval[0]
        return is_won

    @property
    def current_population_x(self):
        """get xs of current pop"""

        logger.debug("called")
        return [i[0] for i in self.current_population]

    # @property
    # def current_population_y(self):

    #     logger.debug("called")
    #     return [i[1] for i in self.current_population]

    # @property
    # def original_population_x(self):
    #     """ """

    #     logger.debug("called")
    #     return [i[0] for i in self.original_population]

    # @property
    # def original_population_y(self):
    #     """ """

    #     logger.debug("called")
    #     return [i[1] for i in self.original_population]

    # @property
    # def x_lim_current_population(self):
    #     """ """

    #     logger.debug("called")
    #     xs = sorted(self.current_population_x)
    #     return {"min": xs[0], "max": xs[-1]}

    # @property
    # def y_lim_current_population(self):
    #     """ """

    #     logger.debug("called")
    #     ys = sorted(self.current_population_y)
    #     return {"min": ys[0], "max": ys[-1]}

    # @property
    # def x_lim_original_population(self):
    #     """ """

    #     logger.debug("called")
    #     xs = sorted(self.original_population_x)
    #     return {"min": xs[0], "max": xs[-1]}

    # @property
    # def y_lim_original_population(self):
    #     """" """

    #     logger.debug("called")
    #     ys = sorted(self.original_population_y)
    #     return {"min": ys[0], "max": ys[-1]}

    @property
    def static_state(self):
        """render a dict with all non variable attributes """

        logger.debug("called")
        d = {
            "id": self._id,
            "level": self.level,
            "dimension": self.dimension,
            "funct": self.funct["expression"],
            "demography": self.demography,
            "objective": self.objective,
            "interval": f"[ {self.interval[0]} - {self.interval[1]} ]",
            "seed_parents": self.seed_parents,
            "kill_rate": self.kill_rate,
            "average_child_numb": self.average_child_numb,
            "funct_template": self._make_template(),
        }
        return d

    @property
    def dynamic_state(self):
        """render a dict with all non static params"""

        logger.debug("called")
        d = {
            "year": self.year,
            "len_current_population": self.len_current_population,
            "repartition_current_population": self.repartition_current_population,
            "best_current_population": self.best_current_population,
            "graph": {
                "current_population": self.graph_pop,
                "xs_last": self.graph_xs_last,
                "ys_last": self.graph_ys_last,
                "years_last": self.graph_years_last,
            },
            "kill_number": self.kill_number,
            "new_people_number": self.new_people_number,
            "saved_people": self.saved_people,
            "new_people_composition": self.new_people_composition,
        }
        return d

    @property
    def serialized(self):
        """return a serialized json state of the funct to be stored in redis """

        return {k: v for k, v in self.__dict__.items() if k in self.SERIALIZED_KEYS}

    ####################################################
    # PRIVATE METHODS
    ####################################################

    def _make_template(self):
        """create paris x, y to have a graph template of the funct """
        return [
            {"x": i, "y": self._funct(i)}
            for i in np.linspace(*self.interval, self.TEMPLATE_INTERVAL)
        ]

    def _sort_current_population(self):
        """ sort values regardin objective"""

        logger.debug("called")
        # first # sort regarding the funct
        reverse = False if self.objective == "min" else True
        self.current_population = sorted(
            self.current_population, key=lambda i: i[1], reverse=reverse
        )

    def _kill_looser(self):
        """regarding kill rate and sorted state make the selection """

        logger.debug("called")
        n_save = len(self.current_population) * (1 - self.kill_rate)
        n_save = int(n_save)
        self.saved_people = n_save
        self.kill_number = len(self.current_population) - n_save
        self.current_population = self.current_population[:n_save]

    def _incr(self):
        """add one year"""

        logger.debug("called")
        self.year += 1

    def _eval(self):
        """eval the best elemand update lurning curve """

        logger.debug("called")
        self._sort_current_population()
        best = self.current_population[0]
        self.learning_curve.append(best)

    def _procreate(self):
        """procreate, ie make random and normal childs"""

        logger.debug("called")

        # N_childs new_people_number
        N_childs = len(self.original_population) - len(self.current_population)
        self.new_people_number = N_childs

        # N_normal_child and N_normal_child
        N_normal_child = int(self.average_child_numb * N_childs)
        N_random_childs = N_childs - N_normal_child
        # logger.debug((f"N_childs {N_childs} "))
        # logger.debug((f"N_normal_child {N_normal_child} "))
        # logger.debug((f"N_random_childs {N_random_childs} "))
        # composition
        self.new_people_composition = {
            "normal_child_nb": N_normal_child,
            "random_child_nb": N_random_childs,
        }

        # rand childs
        random_childs_x = [  # xs of rand childs
            np.random.rand() + np.random.randint(*self.interval)
            for _ in range(N_random_childs)
        ]
        random_childs = [  # xs, ys of rand childs + random + year
            (
                round(x, self._round),
                round(self._funct(x), self._round),
                "random",
                self.year,
            )
            for x in random_childs_x
        ]
        logger.debug((f"random_childs {random_childs} "))

        # normal childs
        normal_childs_x = []
        x_0 = sum(self.current_population_x) / self.len_current_population
        normal_childs_x.append(x_0)
        for _ in range(N_normal_child - 1):
            numb_parents = np.random.randint(1, self.len_current_population)
            random_parents = np.random.choice(
                self.current_population_x, size=numb_parents
            )
            x_n = sum(random_parents) / len(random_parents)
            normal_childs_x.append(x_n)
        normal_childs = [
            (
                round(x, self._round),
                round(self._funct(x), self._round),
                "normal",
                self.year,
            )
            for x in normal_childs_x
        ]

        # logger.debug((f"normal_childs {normal_childs} "))

        # add to current pop
        self.current_population.extend(random_childs)
        self.current_population.extend(normal_childs)

    def _run(self):
        """run one time """

        logger.debug("called")
        # kill or procreate first
        if self.kill_before_reproduce:
            self._kill_looser()
            self._procreate()
        else:
            self._procreate()
            self._kill_looser()
        # learning curve
        best = self._eval()
        # one year
        self._incr()
        # return best

    ####################################################
    # PUBLIC METHODS
    ####################################################

    def run(self, n=10):
        """run n times for n years"""

        logger.debug("called")
        for _ in range(n):
            self._run()

    ####################################################
    # DUNDER
    ####################################################

    def __repr__(self):

        return f"Algo id : {self._id}\nfunct : {self.funct}\ninterval:  {self.interval}\nyear : {self.year} "

    def __str__(self):

        return self.__repr__()

    ####################################################
    # PLOTS
    ####################################################

    @property
    def graph_pop(self):

        logger.debug("called")

        LL = {}
        for kk in ["normal", "first", "random"]:
            LL.update(
                {
                    kk: [
                        {"x": i, "y": j}
                        for i, j, k, l in self.current_population
                        if (k == kk)
                    ]
                }
            )
        return LL

    @property
    def graph_xs(self):

        logger.debug("called")
        L = [
            ["years", "x"],
        ]
        xs = [i[0] for i in self.learning_curve]
        x = [i for i, _ in enumerate(xs)]

        LL = [[i, j] for i, j in zip(x, xs)]
        L.extend(LL)
        return L

    @property
    def graph_xs_last(self):

        logger.debug("called")
        return self.graph_xs[-1]

    @property
    def graph_ys(self):

        logger.debug("called")
        L = [
            ["years", "y"],
        ]
        ys = [i[1] for i in self.learning_curve]
        x = [i for i, _ in enumerate(ys)]

        LL = [[i, j] for i, j in zip(x, ys)]
        L.extend(LL)
        return L

    @property
    def graph_ys_last(self):

        logger.debug("called")
        return self.graph_ys[-1]

    @property
    def graph_years(self):

        logger.debug("called")
        L = [
            ["years", "year"],
        ]
        years = [i[3] for i in self.learning_curve]
        x = [i for i, _ in enumerate(years)]

        LL = [[i, j] for i, j in zip(x, years)]
        L.extend(LL)
        return L

    @property
    def graph_years_last(self):

        logger.debug("called")
        return self.graph_years[-1]
