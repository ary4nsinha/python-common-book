
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
ax = plt.axes(projection = "3d")

z = np.linspace(0,30,100)
x = np.sin(z)
y = np.cos(z)
ax.plot3D(x,y,z)
plt.show()

#vizualize 3d scatter plot with randomly generate 50 data points for x,y,z. set the point color as red and the size of the point is 70