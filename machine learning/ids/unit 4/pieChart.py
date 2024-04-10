import matplotlib.pyplot as plt
import numpy as np


cars = ["AUDI", "BMW", "JAGUAR", "BMW"]
data = [34,24,25,17]
plt.pie(data, labels=cars,autopct='%0.0f%%', explode=[0,0,0.2,0])
plt.show()


