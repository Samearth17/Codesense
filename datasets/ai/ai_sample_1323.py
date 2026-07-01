import numpy as np
from scipy.optimize import minimize

def objective(x):
    return np.sum(np.power(x,2))

def constraint1(x):
    return x[0] * x[1] * x[2] * x[3] - 25.0

def constraint2(x):
    sum_sq = 40
    for i in range(4):
        sum_sq = sum_sq - np.power(x[i],2)
    return sum_sq

x0=[1,4,3,1]
b = (1.0,5.0)
bnds = (b, b, b, b)

con1 = {'type': 'ineq', 'fun': constraint1} 
con2 = {'type': 'eq', 'fun': constraint2}

cons = [con1,con2]

solution = minimize(objective,x0,method='SLSQP',bounds=bnds,constraints=cons)
print(solution)