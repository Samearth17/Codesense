import numpy as np
from sklearn.svm import SVC 

# Dataset 
training_data = [
 {"label": "apple", "features": [1, 1, 0]}, 
 {"label": "banana", "features": [0, 1, 1]}, 
 {"label": "lemon", "features": [0, 0, 1]}, 
 {"label": "orange", "features": [1, 0, 0]}, 
 {"label": "pear", "features": [0, 1, 0]}, 
]

# Feature extraction 
X = []
y = []
for data in training_data:
 X.append(data['features'])
 y.append(data['label'])

# Model 
clf = SVC()
clf.fit(X, y) 

# Prediction 
predict_data = [1, 0, 1]
predicted_label = clf.predict([predict_data])

print(predicted_label[0])