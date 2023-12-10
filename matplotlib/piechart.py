import numpy as np 
import matplotlib.pyplot as plt 

lang = ["Python", "C++", "Go", "Java","C#"]
votes = [50,34,12,44,28]
explodes = [0,0,0.3,0,0]
plt.pie(votes, labels =lang, explode=explodes)
plt.show()