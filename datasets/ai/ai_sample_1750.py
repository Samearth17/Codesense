import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load data into a dataframe
data = pd.read_csv("data.csv")

# Split data into features and target
X = data[['age','gender','income','marital_status','education']]
y = data['purchase']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

# Initialize model
rf = RandomForestClassifier(random_state=123)

# Train the model on the training set
rf.fit(X_train, y_train)

# Test the model on the testing set and calculate the accuracy
accuracy = rf.score(X_test, y_test)

# Print the accuracy
print("Accuracy: " + str(accuracy))