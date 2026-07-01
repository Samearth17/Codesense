import math
  
def solveQuadratic(a, b, c): 
    discriminant = (b**2) - (4*a*c);
    
    # If discriminant is negative there are no real roots.
    if (discriminant < 0): 
        return {
            "status": false,
            "roots": []
        }
    # If discriminant is zero, there is only one real roots.
    elif (discriminant == 0):
        x = -b/(2*a)
        return {
            "status": true,
            "roots": [x]
        }
    # Otherwise there are 2 real roots 
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a); 
        x2 = (-b - math.sqrt(discriminant)) / (2*a); 
        return {
            "status": true,
            "roots": [x1, x2]
        }

a = 1
b = 3
c = -4

print(solveQuadratic(a, b, c)) #{'status': True, 'roots': [-4.0, 1.0]}