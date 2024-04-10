import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import pandas as pd

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x,y,z = ax.axes3d.get_test_data(0.05)
ax.plot3d(x,y,z,rstride=10,cstride=10)
plt.show()