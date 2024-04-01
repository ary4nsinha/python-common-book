import matplotlib.pyplot as plt 
import numpy as np

x = ["IT","BPO"]
y = [14.18,18.04]

plt.bar(x,y,align="edge",  width=0.5,color="red" ,edgecolor="green")
plt.show()