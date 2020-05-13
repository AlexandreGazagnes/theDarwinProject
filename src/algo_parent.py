import secrets

import json

import numpy as np

import matplotlib.pylab as plt
import seaborn as sns
from bokeh.plotting import figure, output_file, show

sns.set()

from src.functs import Functs
from src import logger


class EvolutionAlgo1D:

    NAME = "EvolutionAlgo1D"

    def __init__(
        self,
        funct=None,
        objective="min",
        winning_threshold=0.001,
        interval=[-100, 100],
        seed_parents=20,
        kill_rate=0.33,
        birth_rate=1,
        average_child_numb=0.75,
        _round=5,
    ):

        logger.debug("called")

        self.id = secrets.token_hex(8)
        self.name = self.NAME
        self.funct = funct if funct else Functs.d1.sinFucker
        self.objective = objective
        self.winning_threshold = winning_threshold
        self.interval = interval
        self.seed_parents = seed_parents
        self.kill_rate = kill_rate
        self.birth_rate = birth_rate
        self.average_child_numb = average_child_numb
        self.year = 0
        self._round = _round
        self.learning_curve = list()
        self.learning_images = [""]
        self.population_images = [""]
        # self.fig, self.ax = plt.subplots(1,1)

        parents = [
            np.random.rand() + np.random.randint(*interval) for _ in range(seed_parents)
        ]
        self.current_population = [
            (
                round(x, self._round),
                round(self.funct(x), self._round),
                "first",
                self.year,
            )
            for x in parents
        ]
        self.original_population = [
            (i, j, k, l) for i, j, k, l in self.current_population
        ]
        self._sort_current_population()

    @property
    def len_current_population(self):
        return len(self.current_population)

    @property
    def current_population_x(self):

        logger.debug("called")
        return [i[0] for i in self.current_population]

    @property
    def current_population_y(self):

        logger.debug("called")
        return [i[1] for i in self.current_population]

    # def plot(self) :

    #     logger.debug("called")
    #     self.ax.plot(self.current_population_x, self.current_population_y)

    def plot_population(self):

        logger.debug("called")
        fig, axs = plt.subplots(1, 1)
        axs.scatter(self.current_population_x, self.current_population_y)

        name = f"app/static/img/{self.id}-population-{self.year}.png"
        plt.savefig(name, dpi=150)
        self.population_images.append(name)

    def plot_learning(self):

        logger.debug("called")
        fig, axs = plt.subplots(1, 3)
        xs = [i[0] for i in self.learning_curve]
        ys = [i[1] for i in self.learning_curve]
        years = [i[3] for i in self.learning_curve]
        x = [i for i, _ in enumerate(xs)]
        ax0 = axs[0].plot(x, xs)
        # ax0.set_title("Xs")
        ax1 = axs[1].plot(x, ys)
        # ax1.set_title("Ys")
        ax2 = axs[2].plot(x, years)
        # ax1.set_title("Ys")

        name = f"app/static/img/{self.id}-learning-{self.year}.png"
        plt.savefig(name, dpi=150)
        self.learning_images.append(name)

    def _sort_current_population(self):

        logger.debug("called")
        # first # sort regarding the funct
        reverse = False if self.objective == "min" else True
        self.current_population = sorted(
            self.current_population, key=lambda i: i[1], reverse=reverse
        )

    def _kill_looser(self):

        logger.debug("called")
        n_save = len(self.current_population) * (1 - self.kill_rate)
        n_save = int(n_save)
        self.current_population = self.current_population[: n_save + 1]

    def _procreate(self):

        logger.debug("called")
        # numbers
        N_childs = len(self.original_population) - len(self.current_population)
        N_normal_child = int(self.average_child_numb * N_childs)
        N_random_childs = N_childs - N_normal_child
        logger.info((f"N_childs {N_childs} "))
        logger.info((f"N_normal_child {N_normal_child} "))
        logger.info((f"N_random_childs {N_random_childs} "))

        # rand childs
        random_childs_x = [
            np.random.rand() + np.random.randint(*self.interval)
            for _ in range(N_random_childs)
        ]
        random_childs = [
            (
                round(x, self._round),
                round(self.funct(x), self._round),
                "random",
                self.year,
            )
            for x in random_childs_x
        ]
        logger.info((f"random_childs {random_childs} "))

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
                round(self.funct(x), self._round),
                "normal",
                self.year,
            )
            for x in normal_childs_x
        ]

        logger.info((f"normal_childs {normal_childs} "))

        self.current_population.extend(random_childs)
        self.current_population.extend(normal_childs)

        # compute random childs, normal childs

    def _incr(self):

        logger.debug("called")
        self.year += 1

    def _eval(self):

        logger.debug("called")
        self._sort_current_population()
        best = self.current_population[0]
        self.learning_curve.append(best)

    def _run(self):

        logger.debug("called")
        self._kill_looser()
        self._procreate()
        best = self._eval()
        self._incr()
        return best

    @property
    def as_dict(self):
        d = {k: v for k, v in self.__dict__.items() if "population" not in k}
        logger.warning(f" d is {d} {type(d)}  ")
        # d = json.dumps(str(d))
        # logger.warning(f" d is {d} {type(d)}  ")
        return d

    def run(self, n=10):

        logger.debug("called")
        for _ in range(n):
            self._run()

    def __repr__(self):
        return f"{self.name}\nid : {self.id}\nfunct : {self.funct}\ninterval:  {self.interval}\n year : {self.year} "

    def __str__(self):
        return self.__repr__()
