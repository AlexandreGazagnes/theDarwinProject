"""
make a scatter plot with varying color and size arguments
code mostly from:
http://matplotlib.sourceforge.net/mpl_examples/pylab_examples/scatter_demo2.py
"""
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook


fig = plt.figure()
ax = fig.add_subplot(111)
## store the scatter in abc object
abc=ax.scatter(list(range(10)), list(range(10)), alpha=0.75)
### if you comment that line of set False to True, you'll see what happens.
# abc.set_visible(False)
#ticks = arange(-0.06, 0.061, 0.02)
#xticks(ticks)
#yticks(ticks)

ax.set_xlabel(r'$\Delta_i$', fontsize=20)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=20)
ax.set_title('Volume and percent change')
ax.grid(True)

plt.show()
