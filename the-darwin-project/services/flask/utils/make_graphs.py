from src.functs import *

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set()

PRECISION = 10000


def main():
    for funct_name, funct in Functs.as_dict.items():
        fig, ax = plt.subplots(1, 1)
        data = [
            (funct["funct"](i), i) for i in np.linspace(*funct["interval"], PRECISION)
        ]
        ys, xs = zip(*data)
        ax.plot(xs, ys)
        n = f"app/static/img/functs/{funct_name}.png"  # app/static/img/functs/
        fig.savefig(n)


if __name__ == "__main__":
    main()
