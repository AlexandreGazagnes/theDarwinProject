import pytest

from src import logger
from src.algo_parent import EvolutionAlgo1D


class TestAglo() : 


    algos = list()

    def test_init(self) : 

        algo = EvolutionAlgo1D(
                funct = None,
                objective = "min",
                winning_threshold = 0.001,
                interval = [-100, 100],
                seed_parents = 30   ,
                kill_rate = 0.25,
                birth_rate = 1 ,
                average_child_numb = 0.25 )

        assert algo.len_current_population == 30
        self.algos.append(algo)

    def test_sort(self) : 

        algo = self.algos[-1]
        algo._sort_current_population()
        print(algo.current_population[:5])
        print(algo.current_population[-5:])

    def test_kill(self) : 

        algo = self.algos[-1]
        print(algo.len_current_population)
        algo._kill_looser()
        print(algo.len_current_population)
        print(algo.current_population[:5])
        print(algo.current_population[-5:])

    def test_procreate(self) : 

        algo = self.algos[-1]
        print(algo.len_current_population)
        algo._procreate()
        print(algo.len_current_population)
        assert algo.len_current_population == 30


    def test_run(self) : 
        algo = self.algos[-1]
        algo.run()

    def test_n_run(self)  : 

        algo = self.algos[-1]
        for _ in range(10) : 
            algo.run()

    def test_graph_learning(self)  : 

        algo = self.algos[-1]
        algo.plot_learning()