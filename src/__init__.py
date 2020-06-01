import logging

from params import Params
from params.logs import setBasicConfig

setBasicConfig(Params)
logger = logging.getLogger()

from src.algo import *
from src.functs import *
