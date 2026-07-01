"""
Implement gradient descent algorithm in Python
"""
import numpy as np

def gradient_descent(x,y,learning_rate=0.01,iterations=100): 
    m_curr = b_curr = 0
    n = len(x)
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print ("m {}, b {}, cost {} iteration {}".format(m_curr,b_curr,cost, i))
    return m_curr, b_curr