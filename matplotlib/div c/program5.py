import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker='o', ms=20, mec='r', mfc='r')
plt.show()