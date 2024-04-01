#Histograms
# The hist2d() function in pyplot module of the matplotlib library used to make a 2d Histogram
import matplotlib.pyplot as plt
import numpy as np

data=np.random.randn(1000)
plt.hist(data,bins=30,color="blue",edgecolor="black")
plt.xlabel('Density')
plt.ylabel('Values')
plt.title('Histogram')
plt.show()