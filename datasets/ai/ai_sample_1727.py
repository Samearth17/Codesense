import numpy as np
from sklearn.model_selection import train_test_split

# prepare the data
user_data = np.array(< array of user data >)
features = user_data[:,:-1]
labels = user_data[:,-1]

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)

# create the model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# make predictions
predictions = model.predict(X_test)

# evaluate the model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, predictions)
print('Model accuracy: ', accuracy)