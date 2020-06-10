from src import logger
from src.functs.dicts import _FunctsDict


_all_names = set([v["name"] for _, v in _FunctsDict.items()])
_all_levels = set([v["level"] for _, v in _FunctsDict.items()])
_all_dimensions = set([v["dimension"] for _, v in _FunctsDict.items()])


class _FunctsClass(dict):
    """Data class contains functions ordered """

    def __init__(self):
        super().__init__(_FunctsDict)

    @property
    def by_level(self):
        return {
            v: [{kk: vv} for kk, vv in self.items() if vv["level"] == v]
            for v in _all_levels
        }

    @property
    def by_dimension(self):
        return {
            v: [{kk: vv} for kk, vv in self.items() if vv["dimension"] == v]
            for v in _all_dimensions
        }

    @property
    def by_name(self):
        return dict(self)

    def __repr__(self):
        raise AttributeError(
            "Please do not call Funct directly, use by_name, by_dimension, by_level instead"
        )

    def __str(self):
        return self.__repr__()


Functs = _FunctsClass()
