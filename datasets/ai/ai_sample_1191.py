def isPrime(n):
    # Edge case
    if n <= 1:
        return False
  
    # Check from 2 to n-1 
    for i in range(2, n): 
        if n % i == 0: 
            return False; 
  
    return True

# Function call 
res = isPrime(2) 
if(res): 
    print("Prime") 
else: 
    print("Not Prime")

# Iterative check in a given range 
for n in range(2, 5):
    res = isPrime(n) 
    if(res): 
        print(n, "is Prime") 
    else: 
        print(n, "is not Prime")