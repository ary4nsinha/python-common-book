#Wireframe Plot n Surface PLots
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
fig=plt.figure()
ax=fig.add_subplot(projection='3d')

x,y,z=axes3d.get_test_data(0.05)

ax.plot_surface(x,y,z,rstride=10,cstride=10) #or plot_wireframe
plt.show()