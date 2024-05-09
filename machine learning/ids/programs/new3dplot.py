import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

z = np.random.randint(100, size= (50))
y = np.random.randint(80, size= (50))
x = np.random.randint(80, size=(50))

ax = plt.axes(projection = "3d")

ax.scatter3D(x,y,z, color = "green")
plt.title("simple 3d scatter plot")
plt.show()