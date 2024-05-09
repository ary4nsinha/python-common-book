import matplotlib.pyplot as plt 
import numpy as np 

#generate random data for the histogram

data = np.random.randn(1000)

#plotting a basic histogram

plt.hist(data, bins = 30, color='skyblue', edgecolor = 'black')

#adding labels and title 
