from scipy.optimize import minimize
import numpy as np

# define the parameters
a, b, c = <array of values for parameters a, b and c>

# define the objective function
def f(x):
 return a * x + b * np.sin(c * x)

# optimize
result = minimize(f, 0, method='BFGS')

# print the results
print(result.x)