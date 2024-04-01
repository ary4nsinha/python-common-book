import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({"Box1": np.random.rand(10), "Box2": np.random.rand(10)})
ax = data [['Box1','Box2']].plot(kind='box', title='boxplot')
plt.show()

