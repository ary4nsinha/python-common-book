import pandas as pd 
# Create a Series
# One Dimensional,
a = [10,20,30,40,50]
series_data = pd.Series(a, name='Numbers')
print("Series:")
print(series_data)
print("\n")
newVar = pd.Series(a, index=["a","b","c","d","e"])
print(newVar['c'])



# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 35, 28],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston']
}

data_frame = pd.DataFrame(data)
print("DataFrame:")
print(data_frame)

print(data_frame.loc[[1,2]])

newData = pd.DataFrame(data, index=["Naam", "Umar","Pata","x","c"])

print(newData)


