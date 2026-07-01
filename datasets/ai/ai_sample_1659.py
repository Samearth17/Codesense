import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Load the customer data
data = pd.read_csv('customer_data.csv')

# Extract relevant features
features = ['age', 'spending', 'income']
X = data[features]

# Create the model and determine the optimum number of clusters
model = KMeans(n_clusters=3)
model.fit(X)

# Add the predicted clusters back to the data
data['cluster'] = model.predict(X)

# Calculate the centroids of each cluster
centroids = model.cluster_centers_

# Get the labels of each cluster
labels = model.labels_

# Print the cluster centroids
print(centroids)