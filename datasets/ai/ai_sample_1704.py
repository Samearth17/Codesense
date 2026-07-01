import math
 
def quadratic_roots(a, b, c):
 
  # calculate the discriminant
  d = (b**2) - (4*a*c)
  
  # calculate the two roots
  root1 = (-b + math.sqrt(d)) / (2*a)
  root2 = (-b - math.sqrt(d)) / (2*a)
   
  print("The roots of x^2 - 5x - 6 are",root1,"and",root2)
  
# Driver Code
a = 2
b = -5
c = -3
quadratic_roots(a, b, c)