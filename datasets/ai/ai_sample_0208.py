import numpy as np
import matplotlib.pyplot as plt
import gzip
import pickle

# load training data
with gzip.open('./mnist_dataset/mnist.pkl.gz', 'rb') as f:
    train_data,valid_data,test_data  = pickle.load(f, encoding='latin1')

# prepare logistic regression
X_train, y_train = train_data[0], train_data[1]
X_valid, y_valid = valid_data[0], valid_data[1]
X_test, y_test = test_data[0], test_data[1]

X_train = np.hstack([np.ones([X_train.shape[0],1]), X_train])
X_valid = np.hstack([np.ones([X_valid.shape[0],1]), X_valid])
X_test = np.hstack([np.ones([X_test.shape[0],1]), X_test])

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

def LogisticRegression(X, y, max_iter, alpha):
    m, n = X.shape
    weights = np.zeros(n)
    
    for _ in range(max_iter):
        weights = weights - alpha * (1/m) * (X.T @ (sigmoid(X @ weights) - y))

    return weights

weights = LogisticRegression(X_train, y_train, 1000, 0.001)

# accuracy on training set
predictions = np.round(sigmoid(X_train @ weights))
train_accuracy = np.mean(predictions == y_train)

# accuracy on validation set
predictions = np.round(sigmoid(X_valid @ weights))
valid_accuracy = np.mean(predictions == y_valid)

# accuracy on test set
predictions = np.round(sigmoid(X_test @ weights))
test_accuracy = np.mean(predictions == y_test)

print('Train accuracy = ', train_accuracy)
print('Validation accuracy = ', valid_accuracy)
print('Test accuracy = ', test_accuracy)