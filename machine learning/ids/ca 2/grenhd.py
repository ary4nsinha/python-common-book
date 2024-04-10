# Pivot Table (using pandas)
# Creating a DataFrame
import pandas as pd
import numpy as np
df = pd.DataFrame({'Category': ['A', 'A', 'B', 'B', 'A', 'B'],'Value': [10, 15, 20, 25, 30, 35]})

pivot_table = pd.pivot_table(df, values='Value', index='Category', aggfunc=np.mean)
print("Pivot Table:")
print(pivot_table)