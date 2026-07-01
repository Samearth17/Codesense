import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.001, max_iter=1000):
        self.learning_rate = learning_rate
        self.max_iter = max_iter
        self.weights = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))


    def fit(self, X, y):
        # add bias term to X
        X = np.hstack([np.ones([X.shape[0], 1]), X])
        num_features = X.shape[1]
        self.weights = np.zeros(num_features)

        for _ in range(self.max_iter):
            # compute the linear combination of the input and weights (z)
            z = np.dot(X, self.weights)
            # compute the model output (a)
            a = self.sigmoid(z)
            # compute the cost of the model output
            cost = (-y * np.log(a) - (1 - y) * np.log(1 - a)).mean()
            # compute the derivatives of the cost for each weights
            dCost_dw = np.dot(X.T, (a - y)) / len(y)
            # update weights
            self.weights -= self.learning_rate * dCost_dw

    def predict(self, X):
        # add bias term to X
        X = np.hstack([np.ones([X.shape[0], 1]), X])
        z = np.dot(X, self.weights)
        a = self.sigmoid(z) 
        return np.round(a)