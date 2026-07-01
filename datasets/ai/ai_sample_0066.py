import numpy as np
class LinearRegressionModel:
    def __init__(self, input_dim, output_dim):
        ''' Initialises the weights and bias of the linear regression model
        Arguments:
            input_dim {int} -- Number of input features
            output_dim {int} -- Number of outputs
        '''
        self.weights = np.zeros((input_dim, output_dim))
        self.bias = np.zeros((1, output_dim))

    def forward(self, x):
        ''' Calculates the forward pass of the linear regression model
        Arguments:
            x {numpy array} -- Input data of size (N, input_dim)
        Returns:
            out {numpy array} -- Output of the linear regression model of size (N, output_dim)
        '''
        out = np.dot(x, self.weights) + self.bias
        return out