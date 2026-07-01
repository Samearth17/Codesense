import numpy as np

def get_layer(input_dim, output_dim, activation='relu'):
    """
    This function creates a single layer neural network in a form of numpy array with given
    input and output dimensions and activation (default relu).
    """
    layer = np.random.rand(input_dim, output_dim)
    if activation == 'relu':
        layer = np.maximum(layer, 0)
    elif activation == 'softmax':
        layer = np.exp(layer) / np.sum(np.exp(layer))
    elif activation == 'sigmoid':
        layer = 1 / (1 + np.exp(-layer))
    return layer