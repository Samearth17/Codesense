from sklearn.cluster import KMeans
import numpy as np
 
#create array of data points 
data_points = np.array([[0, 0], [5, 5], [10, 10], [15, 15], [20, 20]])
 
# Build and fit model
kmeans = KMeans(n_clusters=2).fit(data_points)
 
# Predict clusters
labels = kmeans.predict(data_points) 
 
# Label data points
labels_mapped = lables.tolist()
label_dict = dict(zip(data_points.tolist(),labels_mapped))
 
# Print result
for data_point, label in label_dict.items():
    print("Data point:", data_point, ", Label:", label)