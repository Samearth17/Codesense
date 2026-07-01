import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.decomposition import TruncatedSVD

# Load Data
data = pd.read_csv('ratings.csv')

# Split into training and test sets
train_data, test_data = train_test_split(data, test_size=0.2)

# Create user-item matrices
train_user_item = train_data.pivot(index='user', columns='item', values='rating').fillna(0)
test_user_item = test_data.pivot(index='user', columns='item', values='rating').fillna(0)

# Create model
model = TruncatedSVD(n_components=20)
model.fit(train_user_item)

# Make predictions on the test set
preds = model.predict(test_user_item)

# Calculate mean squared error
mse = mean_squared_error(test_user_item, preds)
print('MSE: ' + str(mse))

# Define Recommendations API
def recommend(user, num_recommend):
 user_item = train_data[train_data['user'] == user].pivot(
 index='user',
 columns='item',
 values='rating'
 ).fillna(0)
 recommendations = model.predict(user_item)

 # Get the item ids
 item_ids = np.argsort(-recommendations)[:num_recommend]

 # Return the top recommendations
 return train_user_item.columns.values[item_ids]