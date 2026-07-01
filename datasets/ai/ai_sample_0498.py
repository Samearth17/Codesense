from sklearn.cluster import KMeans
import numpy as np

# generate dataset
X = np.array([[2, 34], [3, 4], [7, 24], [5, 14], [8, 22], [10, 21]])

# train K-Means
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

# assign clusters
clusters = kmeans.predict(X)

# print data with respective clusters
print("Data | Cluster")
for i in range(len(X)):
 print(X[i], "|", clusters[i])