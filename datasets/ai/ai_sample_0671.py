import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Read in the dataset
data = pd.read_csv('data.csv')

# Prepare the dataset with feature scaling
X = data.values
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train a KMeans model
kmeans = KMeans(n_clusters=2).fit(X)

# Check the predictions for potential anomalies
predictions = kmeans.predict(X)
for i in range(len(predictions)):
 if predictions[i] == 1:
 print('Possible anomaly detected!')