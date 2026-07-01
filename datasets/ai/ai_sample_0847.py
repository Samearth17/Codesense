import numpy as np

def gradient_descent(x, y, alpha=1e-4, tol=1e-4):
    n,m = x.shape
    weights = np.zeros(m)
    y_pred = np.matmul(x, weights)
    SSE = np.sum((y - y_pred)**2)
    prev_SSE = 0.
    weights_list=[]
    while np.abs(SSE - prev_SSE) > tol:        
        prev_SSE = SSE
        gradient = np.matmul(x.T,(y - y_pred))
        weights += alpha * gradient
        weights_list.append(weights)
        y_pred = np.matmul(x, weights)
        SSE = np.sum((y - y_pred)**2)

    return weights_list, SSE