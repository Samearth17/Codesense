# import the necessary libraries for the ML workflow
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# load the data
iris = load_iris()
X = iris.data
y = iris.target

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# instantiate and train the model
model = GaussianNB()
model.fit(X_train, y_train)

# make predictions on the test data
predictions = model.predict(X_test)

# evaluate accuracy of the model
score = accuracy_score(y_test, predictions)
print(score)