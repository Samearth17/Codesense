import numpy as np 

def kmeans(k, data): 
    """
    Perform k-means clustering on data
    """
    # randomly set initial centroids
    centroids = data[np.random.randint(low=0, high=len(data), size=k)]
    prev_centroids = np.zeros(centroids.shape)

    clusters = np.zeros(len(data))
    distances = np.zeros((len(data), k))
    
    # find the closest centroid for each sample
    while not np.allclose(centroids, prev_centroids):
        # save old centroids
        prev_centroids = centroids
    
        # get the distance between each point and each centroid
        for idx, centroid in enumerate(centroids):
            distances[:, idx] = np.linalg.norm(data - centroid, axis=1)
    
        # assign each sample to the closest centroids
        clusters = np.argmin(distances, axis=1)
    
        # update centroids 
        for idx in range(k):
            centroids[idx] = np.mean(data[clusters == idx], axis=0)
    
    return clusters, centroids