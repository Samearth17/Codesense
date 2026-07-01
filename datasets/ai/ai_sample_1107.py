# import libraries
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# load the dataset
dataset = datasets.load_iris()

# create the model
model = RandomForestClassifier()

# train the model
model.fit(dataset.data, dataset.target)

# make predictions
predictions = model.predict(dataset.data)

# check accuracy
accuracy = model.score(dataset.data, dataset.target)

print('Accuracy: {}%'.format(accuracy * 100))