from sklearn import tree
import pandas as pd

# Load the data
df = pd.read_csv("data.csv")

# Define the features and labels
features = ["Age", "Income", "Gender"]
labels = ["Credit"]

# Create a Decision Tree classifier
clf = tree.DecisionTreeClassifier()

# Train the model using the training sets
clf.fit(df[features], df[labels])

# Make predictions using the testing set
predictions = clf.predict(df[features])