import numpy as np 
import matplotlib.pyplot as plt 

# Load the data
x1 = np.loadtxt("dataset1.txt")
x2 = np.loadtxt("dataset1.txt")
y = np.loadtxt("dataset2.txt")

# Fit the linear model 
coefficients = np.polyfit(x1,x2,2)

# Plot the linear regression line
plt.scatter(x1, x2)
plt.plot(x1, np.polyval(coefficients, x1), 'r')
plt.show()