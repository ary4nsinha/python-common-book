# SUPERVISED(CLASSIFICATION-DECISION TREE)

import pandas as pd

# Dataset
data = {
    'No.': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'],
    'Age': [20, 40, 30, 18, 28, 35, 45],
    'Amount': [500, 1000, 800, 300, 1200, 1400, 1800],
    'Label': ['Low', 'Medium', 'Medium', 'Low', 'High', 'High', 'High']
}

df = pd.DataFrame(data)

# Selecting features and target
X = df[['Age', 'Amount']]
y = df['Label']

# Splitting data into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the decision tree classifier
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Making predictions
y_pred = clf.predict(X_test)

# Evaluating the model
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)