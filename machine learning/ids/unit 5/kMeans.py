import pandas as pd

data = {
    'No.': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'],
    'Age': [20, 40, 30, 18, 28, 35, 45],
    'Amount': [500, 1000, 800, 300, 1200, 1400, 1800]
}
df = pd.DataFrame(data)

from sklearn.cluster import KMeans
# Selecting features for clustering
X = df[['Age', 'Amount']]
# Defining the number of clusters
k = 3

# Creating KMeans instance
kmeans = KMeans(n_clusters=k)

# Fitting the model
kmeans.fit(X)

# Adding cluster labels to the DataFrame
df['Cluster'] = kmeans.labels_
print(df)