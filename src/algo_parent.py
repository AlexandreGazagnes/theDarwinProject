import secrets
import json
from collections import Iterable

from src.functs import Functs
from src import logger

import numpy as np


# THIS ONE SHOULD BE AN ABS CLASS
class EvolutionAlgo1D:
    """ """

    NAME = "EvolutionAlgo1D"

    ####################################################
    # INIT
    ####################################################

    def __init__(
        self,
        funct=None,
        objective="min",
        interval=[-100, 100],
        seed_parents=20,
        kill_rate=0.33,
        demography=1.0,
        average_child_numb=0.75,
        _round=5,
    ):

        logger.debug("called")
        self.id = secrets.token_hex(12)
        self.name = self.NAME
        self.funct = funct if funct else Functs.d1.sinFucker
        self.objective = objective
        self.interval = interval
        self.seed_parents = seed_parents
        self.kill_rate = kill_rate
        self.demography = demography
        self.average_child_numb = average_child_numb
        self.year = 0
        self._round = _round
        self.learning_curve = list()

        # find parents
        parents = [
            np.random.rand() + np.random.randint(*interval) for _ in range(seed_parents)
        ]
        self.current_population = [
            (
                round(x, self._round),
                round(self.funct["funct"](x), self._round),
                "first",
                self.year,
            )
            for x in parents
        ]
        self.original_population = [
            (i, j, k, l) for i, j, k, l in self.current_population
        ]
        self._sort_current_population()

    ####################################################
    # PROPERTIES
    ####################################################

    @property
    def len_current_population(self):
        """ """

        logger.debug("called")
        return len(self.current_population)

    @property
    def repartition_current_population(self):
        """ """

        logger.debug("called")
        l = [i[2] for i in self.current_population]
        return {k: l.count(k) for k in set(l)}

    @property
    def best_current_population(self):
        """ """

        logger.debug("called")
        self._sort_current_population()
        return self.current_population[:5]

    @property
    def current_population_x(self):
        """ """

        logger.debug("called")
        return [i[0] for i in self.current_population]

    @property
    def current_population_y(self):

        logger.debug("called")
        return [i[1] for i in self.current_population]

    @property
    def original_population_x(self):
        """ """

        logger.debug("called")
        return [i[0] for i in self.original_population]

    @property
    def original_population_y(self):
        """ """

        logger.debug("called")
        return [i[1] for i in self.original_population]

    @property
    def x_lim_current_population(self):
        """ """

        logger.debug("called")
        xs = sorted(self.current_population_x)
        return {"min": xs[0], "max": xs[-1]}

    @property
    def y_lim_current_population(self):
        """ """

        logger.debug("called")
        ys = sorted(self.current_population_y)
        return {"min": ys[0], "max": ys[-1]}

    @property
    def x_lim_original_population(self):
        """ """

        logger.debug("called")
        xs = sorted(self.original_population_x)
        return {"min": xs[0], "max": xs[-1]}

    @property
    def y_lim_original_population(self):
        """" """

        logger.debug("called")
        ys = sorted(self.original_population_y)
        return {"min": ys[0], "max": ys[-1]}

    @property
    def static_state(self):
        """ """

        logger.debug("called")
        d = {
            "id": self.id,
            "name": self.name,
            "funct": self.funct["expression"],
            "demography": self.demography,
            "objective": self.objective,
            "interval": self.interval,
            "seed_parents": self.seed_parents,
            "kill_rate": self.kill_rate,
            "average_child_numb": self.average_child_numb,
        }
        return d

    @property
    def dynamic_state(self):
        """ """

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
        }
        return d

    ####################################################
    # PRIVATE METHODS
    ####################################################

    def _sort_current_population(self):
        """ """

        logger.debug("called")
        # first # sort regarding the funct
        reverse = False if self.objective == "min" else True
        self.current_population = sorted(
            self.current_population, key=lambda i: i[1], reverse=reverse
        )

    def _kill_looser(self):
        """ """

        logger.debug("called")
        n_save = len(self.current_population) * (1 - self.kill_rate)
        n_save = int(n_save)
        self.current_population = self.current_population[: n_save + 1]

    def _procreate(self):
        """ """

        logger.debug("called")
        # numbers
        N_childs = len(self.original_population) - len(self.current_population)
        N_normal_child = int(self.average_child_numb * N_childs)
        N_random_childs = N_childs - N_normal_child
        logger.debug((f"N_childs {N_childs} "))
        logger.debug((f"N_normal_child {N_normal_child} "))
        logger.debug((f"N_random_childs {N_random_childs} "))

        # rand childs
        random_childs_x = [
            np.random.rand() + np.random.randint(*self.interval)
            for _ in range(N_random_childs)
        ]
        random_childs = [
            (
                round(x, self._round),
                round(self.funct["funct"](x), self._round),
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
                round(self.funct["funct"](x), self._round),
                "normal",
                self.year,
            )
            for x in normal_childs_x
        ]

        logger.debug((f"normal_childs {normal_childs} "))

        self.current_population.extend(random_childs)
        self.current_population.extend(normal_childs)

    def _incr(self):
        """ """

        logger.debug("called")
        self.year += 1

    def _eval(self):
        """ """

        logger.debug("called")
        self._sort_current_population()
        best = self.current_population[0]
        self.learning_curve.append(best)

    def _run(self):
        """ """

        logger.debug("called")
        self._kill_looser()
        self._procreate()
        best = self._eval()
        self._incr()
        return best

    ####################################################
    # PUBLIC METHODS
    ####################################################

    def run(self, n=10):
        """ """

        logger.debug("called")
        for _ in range(n):
            self._run()

    ####################################################
    # DUNDER
    ####################################################

    def __repr__(self):

        return f"{self.name}\nid : {self.id}\nfunct : {self.funct}\ninterval:  {self.interval}\n year : {self.year} "

    def __str__(self):

        return self.__repr__()

    ####################################################
    # PLOTS
    ####################################################

    @property
    def graph_pop(self):

        logger.debug("called")

        LL = [{"x": i, "y": j} for i, j, k, l in self.current_population]
        # list(zip(*LL))
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
