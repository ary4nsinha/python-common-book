#3D scatter plot
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

ax=plt.axes(projection='3d')

x=np.random.randint(100,size=(80))
y=np.random.randint(80,size=(80))
z=np.random.randint(100,size=(80))

ax.scatter3D(x,y,z,color='blue')
plt.title("3D Scatter Plot")
plt.show()
