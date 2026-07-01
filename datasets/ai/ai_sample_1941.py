# Function to check if the number is prime or not
def is_prime(n):
 
    # Corner case
    if n <= 1:
        return False
 
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
 
# Driver Code
num = 11
 
# Check if prime
if is_prime(num):
    print("{} is a prime number".format(num))
else:
    print("{} is not a prime number".format(num))