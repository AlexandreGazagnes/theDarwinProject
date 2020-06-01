from math import cos, sin, pi, exp, sqrt


_FunctsDict = {
    "x2": {
        "level": "beginner",
        "name": "x2",
        "expression": "y = x ** 2",
        "funct": "lambda x: x ** 2",
        "dimension": "1D",
        "objective": "min",
        "target": 0.0,
        "interval": [-10, 10],
    },
    "sinFucker": {
        "level": "intermediate",
        "name": "sinFucker",
        "expression": "y = (sin(x) * (x * 2) - (10 * x)) ** 2",
        "funct": "lambda x: (sin(x) * (x * 2) - (10 * x)) ** 2",
        "dimension": "1D",
        "objective": "min",
        "target": 0.0,
        "interval": [-10, 10],
    },
    "alexCos": {
        "level": "intermediate",
        "name": "alexCos",
        "expression": "y = cos(x**0.5) + x**0.333",
        "funct": "lambda x: cos(x ** 0.5) + x ** 0.333",
        "dimension": "1D",
        "objective": "min",
        "target": 1.0,
        "interval": [1, 200],
    },
    "manuCos": {
        "level": "intermediate",
        "name": "manuCos",
        "expression": "y = (cos(x**2) + abs(1.5* x) )**2",
        "funct": "lambda x: (cos(x ** 2) + abs(1.5 * x)) ** 2",
        "dimension": "1D",
        "objective": "min",
        "target": 1.0,
        "interval": [-5, 5],
    },
    "nathanCos": {
        "level": "intermediate",
        "name": "nathanCos",
        "expression": "y = 10 + (x ** 2) - (10 * cos(2 * pi * x))",
        "funct": "lambda x: 10 + (x ** 2) - (10 * cos(2 * pi * x))",
        "dimension": "1D",
        "objective": "min",
        "target": 0.0,
        "interval": [-5, 5],
    },
    "easom": {
        "level": "expert",
        "name": "easom",
        "expression": "y = - cos(x) * cos(pi) * exp (-(x-pi)**2)",
        "funct": "lambda x: -cos(x) * cos(pi) * exp(-((x - pi) ** 2))",
        "dimension": "1D",
        "objective": "min",
        "target": -1.0,
        "interval": [-30, 30],
    },
    "eggholder": {
        "level": "expert",
        "name": "eggholder",
        "expression": "y = -(47 * sin(sqrt(abs((0.5 * x) + 47)))) - (x * sin(sqrt(abs(x - 47))))",
        "funct": "lambda x: -(47 * sin(sqrt(abs((0.5 * x) + 47))))\
        - (x * sin(sqrt(abs(x - 47))))",
        "dimension": "1D",
        "objective": "min",
        "target": -118.0,
        "interval": [-200, 200],
    },
    "holder": {
        "level": "expert",
        "name": "holder",
        "expression": "y = - abs(sin(x) * cos(0) * exp(abs( 1 - ( (sqrt(x**2 + 0**2)) / pi) ) ) )",
        "funct": "lambda x: (x / 40) \
        - abs(sin(x) * cos(0) * exp(abs(1 - ((sqrt(x ** 2 + 0 ** 2)) / pi))))",
        "dimension": "1D",
        "objective": "min",
        "target": -118.0,
        "interval": [-9.4, 9.4],
    },
}


_all_names = set([v["name"] for _, v in _FunctsDict.items()])
_all_levels = set([v["level"] for _, v in _FunctsDict.items()])
_all_dimensions = set([v["dimension"] for _, v in _FunctsDict.items()])


class _FunctsClass(dict):
    """Data class contains functions ordered """

    def __init__(self):
        super().__init__(_FunctsDict)
        # super().__init__()

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


Functs = _FunctsClass()
