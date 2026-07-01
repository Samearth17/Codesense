# Function to generate prime numbers between 1 and a given number n 
def generate_prime_numbers(n): 
  
    # Array for checking if a number is prime or not
    prime_list = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime_list[p] is not changed, then it is a prime 
        if (prime_list[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime_list[i] = False
        p += 1
  
    # Collecting prime numbers 
    for p in range(2, n): 
        if prime_list[p]: 
            print(p)