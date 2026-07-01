num = int(input("Please enter a number: "))

# Check if num is a prime number

def is_prime(n):
    
    # Check if n is greater than 1
    if n > 1: 
       # Check for factors 
       for i in range(2,n): 
          if (n % i) == 0: 
              return False # n is not prime
       else:
           return True # n is prime
    
    else:
       return False

if is_prime(num): 
   print(num, "is a prime number")
else: 
   print(num, "is not a prime number")