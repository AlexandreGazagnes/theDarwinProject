import logging

from params import Params
from params.logs import setBasicConfig

setBasicConfig(Params)
logger = logging.getLogger()


# try : 
#     %matplotlib
# except Exception as e : 
#     logger.error(e)

from src.algo_parent import EvolutionAlgo1D
from src.functs import Functs





app = EvolutionAlgo1D()