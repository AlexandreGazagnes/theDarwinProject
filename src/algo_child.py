from src.functs import Functs
from src.algo_parent import EvolutionAlgo1D
from src import logger


class NathanAlgo(EvolutionAlgo1D):
    def __init__(self):

        super().__init__(
            funct=Functs.d1.nathanCos,
            objective="min",
            winning_threshold=0.001,
            interval=[-5, 5],
            seed_parents=12,
            kill_rate=0.25,
            birth_rate=1,
            average_child_numb=0.66,
            _round=5,
        )
