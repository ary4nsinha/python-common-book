import pandas as pd

# Sample DataFrame
data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Value1': [10, 20, 30, 40, 50, 60],
    'Value2': [100, 200, 300, 400, 500, 600]
}
df = pd.DataFrame(data)

# Creating a pivot table
pivot_table = pd.pivot_table(df, values=['Value1', 'Value2'], index='Category', aggfunc='sum')

print(pivot_table)
