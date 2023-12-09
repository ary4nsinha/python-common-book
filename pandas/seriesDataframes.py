import pandas as pd 
# Create a Series
# One Dimensional,

series_data = pd.Series([10, 20, 30, 40, 50], name='Numbers')
print("Series:")
print(series_data)
print("\n")

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 35, 28],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston']
}

data_frame = pd.DataFrame(data)
print("DataFrame:")
print(data_frame)
