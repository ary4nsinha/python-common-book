import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.DataFrame({"Box1": [12,34,5,67,4,3,4,5,44,43],"Box2": [12,23,43,22,67,89,76,54,33,21]})
ax = data[['Box1', 'Box2']].plot(kind='box', title='boxplot')
plt.show()