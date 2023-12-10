import matplotlib.pyplot as plt 
import numpy as np

x = ["C++","C#","Python","Java","Go"]
y = [20,50,140,1,45]

plt.bar(x,y,align="edge",  width=0.5,color="red" ,edgecolor="green")
plt.show()