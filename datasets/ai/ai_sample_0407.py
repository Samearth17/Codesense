#import matplotlib.pyplot as plt 
import numpy as np 
import sympy as sym 
from scipy import optimize 

# define the function
def function(x, y):
	return 5*x + 3*y 

# define the inputs
x = sym.Symbol('x') 
y = sym.Symbol('y') 

# optimize the function
result = optimize.minimize(function, [0, 0]) 

# output the results
print('The optimal value of x is:', result.x[0]) 
print('The optimal value of y is:', result.x[1])