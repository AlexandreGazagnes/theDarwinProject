import logging

from params import Params
from params.logs import setBasicConfig

setBasicConfig(Params)
logger = logging.getLogger()


from src.algo_parent import EvolutionAlgo1D
from src.algo_child import NathanAlgo
from src.functs import Functs




