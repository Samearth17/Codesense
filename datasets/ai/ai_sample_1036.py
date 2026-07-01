import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
data = pd.read_csv('iris.csv')

# Define X and y
X = data.drop('species', axis=1)
y = data['species']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Build the decision tree classifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

# Evaluate the classifier
score = classifier.score(X_test, y_test)
print('Classifier accuracy: ', score)