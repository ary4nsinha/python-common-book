import matplotlib.pyplot as plt
import numpy as np

# Generating sample data
x1 = np.random.rand(50)
y1 = np.random.rand(50)
x2 = np.random.rand(50)
y2 = np.random.rand(50)
x3 = np.random.rand(50)
y3 = np.random.rand(50)

# Creating scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(x1, y1, color='blue', label='Dataset 1')
plt.scatter(x2, y2, color='red', label='Dataset 2')
plt.scatter(x3, y3, color='green', label='Dataset 3')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatterplot of Multiple Datasets')

# Adding legend
plt.legend()

# Displaying the plot
plt.grid(True)
plt.show()
