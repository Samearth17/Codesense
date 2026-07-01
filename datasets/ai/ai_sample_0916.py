import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

# Read in the data
data = pd.read_csv('flowers.csv')
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Scale the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train the neural network
clf = MLPClassifier(hidden_layer_sizes=(20, 20), max_iter=1000)
clf.fit(X, y)

# Test the model
preds = clf.predict(X)

# Evaluate the model
accuracy = np.mean(preds == y)
print('Model accuracy: {:.2f}%'.format(accuracy*100))