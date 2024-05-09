import pandas as pd

# Dataset
data = {
    'No.': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'],
    'Age': [20, 40, 30, 18, 28, 35, 45],
    'Amount': [500, 1000, 800, 300, 1200, 1400, 1800],
}

df = pd.DataFrame(data)

# Selecting features and target
X = df[['Age']]
y = df['Amount']

# Splitting data into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the linear regression model
from sklearn.linear_model import LinearRegression

regression = LinearRegression()
regression.fit(X_train, y_train)

# Making predictions
y_pred = regression.predict(X_test)

# Evaluating the model
from sklearn.metrics import mean_squared_error, mean_absolute_error

mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)  # Calculating RMSE
mae = mean_absolute_error(y_test, y_pred)

print("Mean Squared Error:", mse)
print("Root Mean Squared Error:", rmse)
print("Mean Absolute Error:", mae)