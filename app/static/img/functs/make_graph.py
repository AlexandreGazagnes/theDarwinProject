from src.functs import *

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()


L = [
    ("x2", Functs.d1.x2),
    ("sinFucker", Functs.d1.sinFucker),
    ("nathanCos", Functs.d1.nathanCos),
]
interval = 10

for funct_name, funct in L:

    # funct_name, funct = ("nathanCos", Functs.d1.nathanCos)
    fig, ax = plt.subplots(1, 1)
    data = [(funct(i), i) for i in np.linspace(-interval, interval, 1000)]
    ys, xs = zip(*data)
    ax.plot(xs, ys)
    n = f"app/static/img/functs/{funct_name}.png"  # app/static/img/functs/
    fig.savefig(n)
