import math

def quadratic_x_intercept(a, b, c):
  discriminant = b**2 - 4*a*c
  if discriminant >= 0:
    x1_intercept = (-b+math.sqrt(discriminant))/(2*a)
    x2_intercept = (-b-math.sqrt(discriminant))/(2*a)
    return x1_intercept, x2_intercept
  else:
    return 'No real solutions exist!'

a = 1
b = 4
c = -5

intercepts = quadratic_x_intercept(a, b, c)
print(intercepts)
# Output (2.0, -2.5)