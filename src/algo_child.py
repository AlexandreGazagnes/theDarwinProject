from src.functs import Functs
from src.algo_parent import EvolutionAlgo1D
from src import logger


class NathanAlgo(EvolutionAlgo1D):
    """ """

    def __init__(self):
        """ """

        logger.debug("called")
        super().__init__(
            funct=Functs.d1.nathanCos,
            objective="min",
            interval=[-50, 50],
            seed_parents=12,
            kill_rate=0.25,
            demography=1,
            average_child_numb=0.66,
            _round=5,
        )
