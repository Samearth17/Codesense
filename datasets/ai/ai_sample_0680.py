# Import relevant packages
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv('patients_data.csv')

# Create the feature and target vectors
X = data[['fever', 'headache', 'sore throat', 'nausea']]
y = data['disease']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Create and fit the Decision Tree
tree = DecisionTreeClassifier()
tree.fit(X_train, y_train)

# Make predictions
predictions = tree.predict(X_test)

# Evaluate the model
accuracy = tree.score(X_test, y_test)
print('Accuracy: ', accuracy)