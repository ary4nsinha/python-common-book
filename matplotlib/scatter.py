import matplotlib.pyplot as plt
import numpy as np 

x_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

plt.scatter(x_data, y_data, c="red", marker="*", s=150, alpha=0.3)
plt.show()
