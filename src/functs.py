from math import cos, sin, pi, exp, sqrt


class _D1:

    x2 = {
        "level": "beginner",
        "name": "x2",
        "expression": "y = x ** 2",
        "funct": lambda x: x ** 2,
        "dim": "1D",
        "objective": "min",
        "target": 0.0,
        "interval": [-10, 10],
    }

    sinFucker = {
        "level": "intermediate",
        "name": "sinFucker",
        "expression": "y = (sin(x) * (x * 2) - (10 * x)) ** 2",
        "funct": lambda x: (sin(x) * (x * 2) - (10 * x)) ** 2,
        "dim": "1D",
        "objective": "min",
        "target": 0.0,
        "interval": [-10, 10],
    }

    nathanCos = {
        "level": "intermediate",
        "name": "nathanCos",
        "expression": "y = 10 + (x ** 2) - (10 * cos(2 * pi * x))",
        "funct": lambda x: 10 + (x ** 2) - (10 * cos(2 * pi * x)),
        "dim": "1D",
        "objective": "min",
        "target": 0.0,
        "interval": [-5, 5],
    }

    easom = {
        "level": "expert",
        "name": "easom",
        "expression": "y = - cos(x) * cos(pi) * exp (-(x-pi)**2)",
        "funct": lambda x: -cos(x) * cos(pi) * exp(-((x - pi) ** 2)),
        "dim": "1D",
        "objective": "min",
        "target": -1.0,
        "interval": [-30, 30],
    }

    eggholder = {
        "level": "expert",
        "name": "Eggholder",
        "expression": "y = -(47 * sin(sqrt(abs((0.5 * x) + 47)))) - (x * sin(sqrt(abs(x - 47))))",
        "funct": lambda x: -(47 * sin(sqrt(abs((0.5 * x) + 47))))
        - (x * sin(sqrt(abs(x - 47)))),
        "dim": "1D",
        "objective": "min",
        "target": -118.0,
        "interval": [-200, 200],
    }

    holder = {
        "level": "expert",
        "name": "holder",
        "expression": "y = - abs(sin(x) * cos(0) * exp(abs( 1 - ( (sqrt(x**2 + 0**2)) / pi) ) ) )",
        "funct": lambda x: (x / 40)
        - abs(sin(x) * cos(0) * exp(abs(1 - ((sqrt(x ** 2 + 0 ** 2)) / pi)))),
        "dim": "1D",
        "objective": "min",
        # "target" : -118.0,
        "interval": [-9.4, 9.4],
    }


# class _D2:
#     nathanBoite = lambda x, y: pi * (x ** 2 / 2) + (4 * y / x)


class Functs:
    d1 = _D1
    # d2 = _D2
    as_dict = {
        "x2": _D1.x2,
        "sinFucker": _D1.sinFucker,
        "nathanCos": _D1.nathanCos,
        "easom": _D1.easom,
        "eggholder": _D1.eggholder,
        "holder": _D1.holder,
    }
