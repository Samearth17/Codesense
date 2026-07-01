def objective_function(x):
 return x**2 + 6*x - 4

def find_local_minima(func):
 x = 0
 delta = 0.01

while True:
 x_new = x + delta
 if objective_function(x_new) < objective_function(x):
 x = x_new
 else:
 return x

print('The local minima is', find_local_minima(objective_function))