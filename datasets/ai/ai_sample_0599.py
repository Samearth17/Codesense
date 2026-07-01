import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

data = [[120, 250], [110, 200], [140, 300]]

# Convert data to a numpy array
data = np.array(data)

# Train the KMeans model with the data
kmeans = KMeans(n_clusters=2).fit(data)

# Generate centroid coordinates
centroids = kmeans.cluster_centers_

# Plot the centroids for the clusters
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3, c='r')

# Plot all datapoints
plt.scatter(data[:, 0], data[:, 1], marker='*', s=100)

plt.show()