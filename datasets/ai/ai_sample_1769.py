# Import the required libraries
import numpy as np

# Define the objective function
def f(x):
 return np.square(x) + 2*x + 3

# Define the optimization algorithm
def opt(f, x0, lr, n_iter):
 x = x0
 for i in range(n_iter):
 x_prev = x
 grad = 2 * x + 2
 x = x - lr * grad
 if np.abs(x - x_prev) < 1e-5:
 break

# Print the results
print("Minimum at {} with value {}".format(x, f(x)))