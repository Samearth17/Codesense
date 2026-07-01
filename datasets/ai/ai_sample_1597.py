"""
Generate random data and create a scatterplot
"""

import matplotlib.pyplot as plt
import numpy as np

# Generate 1000 random points
np.random.seed(0)
x = np.random.rand(1000)
y = np.random.rand(1000)

# Create a scatter plot
plt.scatter(x,y)
plt.show()