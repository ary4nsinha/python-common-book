import numpy as np 
import matplotlib.pyplot as plt 

lang = ["IT", "BPO",]
votes = [82.84, 17.16]
explodes = [0,0]
plt.pie(votes, labels =lang, explode=explodes)
plt.show()