def Goldbach_conjecture(n):
    assert type(n) == int and n > 0, "n must be a positive integer."
    if n % 2 != 0:
        raise ValueError("n must be an even number.")
    
	# list to hold all the prime pairs that add to n
    prime_pairs = []
    # find all prime numbers less than n
    primes = [x for x in range(2, n+1) if isprime(x)]
    # loop through all prime numbers
    for prime_x in primes:
        # check if prime_x added to any prime number less than prime_x 
        # equals n. If true, add that prime pair to the prime_pairs list
        for prime_y in primes:
            if prime_y < prime_x and prime_x + prime_y == n:
                prime_pairs.append((prime_x, prime_y))
    return prime_pairs

def isprime(n):
    # check if n is prime
    if n < 2:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True