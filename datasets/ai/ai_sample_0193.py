import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Read in data
data = pd.read_csv('product_data.csv')

# Create an item-based collaborative filter
cf = NearestNeighbors(metric='cosine', algorithm='brute')
cf.fit(data)

# Make recommendations
distances, indices = cf.kneighbors(data, n_neighbors=3)

# Print results 
for i in range(len(data)):
 print('Recommendations for item {}:'.format(i), indices[i])