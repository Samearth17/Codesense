import numpy as np

def minimize(x):
  return np.power(x,4) + 7 * np.power(x,3) + 6 * np.power(x,2) - 6 * x

def optimize(f, x):
  best_x = x 
  best_val = f(x)

  while True:
    new_x = x - 1e-3 
    new_val = f(new_x)
    if new_val < best_val: 
      best_x = new_x 
      best_val = new_val 
      x = new_x
    else:
      break
  return best_x, best_val

x = 0 
x_min, val_min = optimize(minimize, x)
print(f'Minimum of function "f(x)" is at x={x_min}, with value {val_min}.')