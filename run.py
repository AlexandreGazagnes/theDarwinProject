import os
import sys
import time

import matplotlib.pylab as plt
import seaborn as sns
# from bokeh.plotting import figure, output_file, show
sns.set()

from src import EvolutionAlgo1D
from src import Functs
%matplotlib

def define_n(): 
    try : 
        n = int(sys.argv[1])
    except Exception as e :
        n = 10
    return n


def main() : 
    """main """

    app = EvolutionAlgo1D(
                funct=Functs.sinFucker,
                interval = [-100, 10000],
                seed_parents = 200,
                kill_rate = 0.5,
                birth_rate = 1 ,
                average_child_numb = 0.75, 
                _round=5 )
    app.run(1000)
    app.plot_learning()



# print(app.current_population[:12])   
# AXS.append(ax.scatter(app.current_population_x, app.current_population_y))
    


# %matplotlib
# app.plot_learning()

# app = EvolutionAlgo1D()
# fig = plt.figure()
# ax = fig.add_subplot(111)

# AXS = list()
# AXS.append(ax.scatter(app.current_population_x, app.current_population_y))


# for _ in range(10) : 
#     AXS[-1].set_visible(False)
#     time.sleep(0.5)
#     app.run()
#     AXS.append(ax.scatter(app.current_population_x, app.current_population_y))
#     time.sleep(0.5)

if  __name__ == "__main__":
    main()