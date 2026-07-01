import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Read in data
data = pd.read_csv('data.csv')

# Train the classifier
features = ['location', 'size', 'bedrooms', 'bathrooms', 'price']
X = data[features]
y = data['label']
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X, y)

# Make predictions
predictions = clf.predict(X)
print(predictions)