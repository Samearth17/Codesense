"""
Generate a python function to classify iris flowers
"""
import numpy as np
from sklearn import neighbors

def classify_iris(data):
    """Classifies the input data into one of the three species of iris flower.

    :param data: The data to be classified as an (N, 4) array of floats

    :returns: An array (N, ) of strings representing the species of the data
    """

    # Train the model
    x_train, y_train = get_iris_training_data()
    model = neighbors.KNeighborsClassifier()
    model.fit(x_train, y_train)

    # Classify the input data
    predictions = model.predict(data)

    return predictions
    
def get_iris_training_data():
    """Read the iris training and target data from a file

    :returns: Two NumPy arrays representing the training data
        and target values
    """

    x = np.genfromtxt('data/iris/x_train.csv', delimiter=',')
    y = np.genfromtxt('data/iris/y_train.csv', delimiter=',', dtype=str)

    return x, y