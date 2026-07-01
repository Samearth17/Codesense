import math 
  
def isPerfectSquare(n): 
    # Find floating point value of 
    # square root of x. 
    sqr = math.sqrt(n) 
   
    # If square root is an integer 
    return (sqr - math.floor(sqr) == 0) 
  
# Driver program 
x = 25
if(isPerfectSquare(x)): 
    print(x, "is a perfect square") 
else: 
    print(x, "is not a perfect square")