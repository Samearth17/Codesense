"""
Construct a program in Python that finds the nth prime number
"""
# A function used to calculate whether a given number is prime
def is_prime(n): 
    # Corner cases  
    if (n <= 1): 
    	return False
    if (n <= 3): 
    	return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop  
    if (n % 2 == 0 or n % 3 == 0): 
    	return False
  
    i = 5
    while(i * i <= n): 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
        i = i + 6
  
    return True

# Function to find the nth prime number
def find_nth_prime_number(n): 
    # Initialize counter to 1 
    prime_count = 1
  
    # Initialize number to 2 
    num = 2
  
    while(prime_count < n): 
    	num += 1
    	if (is_prime(num)): 
    		prime_count += 1
    return num

nth_prime_number = find_nth_prime_number(n)
print("The nth prime number is",nth_prime_number)