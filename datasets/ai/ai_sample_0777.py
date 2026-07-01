from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load and split the dataset
iris_data = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2)

# Train the classifier
clf = RandomForestClassifier(n_estimators=100)
clf.fit(x_train, y_train)

# Make predictions
preds = clf.predict(x_test)

from sklearn.metrics import confusion_matrix

# Output confusion matrix
confusion_matrix(y_test, preds)