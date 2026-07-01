"""
Write a Python program to generate random walk data.
"""

import numpy as np

def random_walk(n):
    """
    Generates a n-step random walk
    """
    steps = np.random.normal(0, 1, n)
    return np.cumsum(steps)

if __name__ == '__main__':
    n = 10
    random_walk_data = random_walk(n)
    print(random_walk_data)