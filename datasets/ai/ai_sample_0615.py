import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)

X_new = np.array([[5.2,3.5,1.4,0.2]])
prediction = knn.predict(X_new)

if int(prediction) == 0:
 print('The flower is a Setosa.')
elif int(prediction) == 1:
 print('The flower is a Versicolor.')
else:
 print('The flower is a Virginica.')