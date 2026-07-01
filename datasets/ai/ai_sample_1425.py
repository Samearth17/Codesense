import numpy as np
from scipy.optimize import minimize
 
def objective(x):
    return (x[0] * x[3] * (x[0] + x[1] + x[2]) + x[2])
 
def constraint1(x):
    return x[0]*x[1]*x[2]*x[3] - 25 
 
def constraint2(x):
    sum_sq = 40
    for i in range(4):
        sum_sq = sum_sq - x[i]**2 
    return sum_sq
     
# Initial Guess
x0 = np.array([1, 4, 10, 1])
 
# show initial objective
print('Initial SSE Objective: ' + str(objective(x0))) 

# Constraints
cons = ({'type': 'ineq', 'fun': constraint1}, 
    {'type': 'ineq', 'fun': constraint2})
 
# Solution
res = minimize(objective, x0, method='SLSQP', 
        constraints=cons, options={'disp': True})
     
# Show final objective
print('Final SSE Objective: ' + str(res.fun))
 
# Print final solution
print('x1 = ' + str(res.x[0]))
print('x2 = ' + str(res.x[1]))
print('x3 = ' + str(res.x[2]))
print('x4 = ' + str(res.x[3]))