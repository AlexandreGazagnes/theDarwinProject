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

    TEMPLATE_INTERVAL = 3000
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
        "is_won",
        "won_year",
        "kill_number",
        "saved_people",
        "new_people_number",
        "new_people_composition",
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
        is_won: int,
        won_year: int,
        kill_number: int,
        saved_people: int,
        new_people_number: int,
        new_people_composition: dict,
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
        self.is_won = is_won
        self.won_year = won_year
        self.kill_number = kill_number
        self.saved_people = saved_people
        self.new_people_number = new_people_number
        self.new_people_composition = new_people_composition

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

            # self.kill_number = -1
            # self.saved_people = -1
            # self.new_people_number = -1
            # self.new_people_composition = {}

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
            "is_won": self.is_won,
            "won_year": self.won_year,
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
            "saved_people": self.saved_people,
            "new_people_number": self.new_people_number,
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

    def _compute_saved_and_killed_numb(self):
        """   """

        n_save = len(self.current_population) * (1 - self.kill_rate)
        self.saved_people = int(n_save)
        self.kill_number = len(self.current_population) - self.saved_people

    def _kill_looser(self):

        """regarding kill rate and sorted state make the selection """

        self._compute_saved_and_killed_numb()
        self.current_population = self.current_population[: self.saved_people]

    def _incr(self):
        """add one year"""

        logger.debug("called")
        self.year += 1

    def _eval_is_won(self):
        """ eval if best  elem in wining threshold interval"""

        logger.debug("called")
        target = float(self.funct["target"])
        if target:
            tt = target * self.winning_threshold
            target_interval = [
                (target - tt),
                (target + tt),
            ]
        else:
            target_interval = [-self.winning_threshold, self.winning_threshold]

        # logger.warning(self.best_current_population[0])
        is_won = (
            target_interval[1] > self.best_current_population[0][1] > target_interval[0]
        )
        if is_won:
            self.won_year = self.year
        self.is_won = int(is_won)

    def _eval(self):
        """eval the best elemand update lurning curve """

        logger.debug("called")
        self._sort_current_population()
        best = self.current_population[0]
        self.learning_curve.append(best)
        self._eval_is_won()

    def _compute_new_child_num(self):
        # N_childs new_people_number
        self.new_people_number = self.kill_number

    def _compute_normal_vs_random_child(self):
        # N_normal_child and N_normal_child
        N_normal_child = int(self.average_child_numb * self.new_people_number)
        N_random_childs = self.new_people_number - N_normal_child
        # logger.debug((f"N_childs {N_childs} "))
        # logger.debug((f"N_normal_child {N_normal_child} "))
        # logger.debug((f"N_random_childs {N_random_childs} "))
        # composition
        self.new_people_composition = {
            "normal_child_nb": N_normal_child,
            "random_child_nb": N_random_childs,
        }

    def _procreate(self):
        """procreate, ie make random and normal childs"""

        logger.debug("called")
        self._compute_new_child_num()
        self._compute_normal_vs_random_child()

        # rand childs
        random_childs_x = [  # xs of rand childs
            np.random.rand() + np.random.randint(*self.interval)
            for _ in range(self.new_people_composition["random_child_nb"])
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
        for _ in range(self.new_people_composition["normal_child_nb"] - 1):
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
        if not self.is_won:
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
            if self.is_won:
                break

    ####################################################
    # DUNDER
    ####################################################

    def __repr__(self):

        return f"Algo id : {self._id}\nfunct : {self.funct}\ninterval:  {self.interval}\nyear : {self.year}\nis_won : {self.is_won}\nbest_elem : {self.best_current_population[0]}"

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
