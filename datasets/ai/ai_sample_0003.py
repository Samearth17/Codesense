# Load the dataset
import pandas as pd
csv_url = 'http://test.test/test.csv'
df = pd.read_csv(csv_url)

# Split the dataset into features and label
X = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values

# Import the ML model
from sklearn.tree import DecisionTreeClassifier

# Create and fit the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict the label
def predict(data):
    predicted_label = model.predict([data])
    return predicted_label