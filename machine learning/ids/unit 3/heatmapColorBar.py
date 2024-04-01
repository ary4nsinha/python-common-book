import numpy as np
import matplotlib.pyplot as plt
data=np.random.random((12,12))
plt.imshow(data,cmap='plasma',interpolation='nearest')

plt.colorbar()

plt.title("2-D Heat Map with color bar")
plt.show()