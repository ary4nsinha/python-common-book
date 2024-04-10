#Heatmap, heatmap with different colour using cmap
import numpy as np
import matplotlib.pyplot as plt
data= np.random.random((12,12)) 
plt.imshow(data,cmap='winter')
plt.title("2-D Heat Map with or without different colours")
plt.colorbar()

plt.show()