import math

def findRoots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
  
    if discriminant < 0:
        print('No real roots.')
  
    elif discriminant == 0:
        root = -b / (2 * a)
        print('One root: ', root)
  
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print('Two roots: ', root1, root2)