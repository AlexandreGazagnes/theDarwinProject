import math


class _D1:
    x2 = lambda x: x ** 2
    sinFucker = lambda x: (math.sin(x) * (x * 2) - (10 * x)) ** 2
    nathanCos = lambda x: 10 + x ** 2 - (10 * math.cos(2 * math.pi * x))


class _D2:
    nathanBoite = lambda x, y: math.pi * (x ** 2 / 2) + (4 * y / x)


class Functs:
    d1 = _D1
    d2 = _D2
    as_dict = {
        "x2": _D1.x2,
        "sinFucker": _D1.sinFucker,
        "nathanCos": _D1.nathanCos,
    }
