def filter_prime(nums):
    # Keep track of the prime numbers
    primes = []
    
    # Iterate through each number
    for num in nums:
        is_prime = True
        # Check if the number is divisible by any number from 2 to itself
        for i in range(2, num):
            # If so, the number is not prime
            if num % i == 0:
                is_prime = False
                break
        # Add the number to the list of primes if it is prime
        if is_prime:
            primes.append(num)
            
    # Return the updated list
    return primes