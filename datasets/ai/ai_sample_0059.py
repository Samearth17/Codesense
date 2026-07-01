import math

def largest_prime_factor(n):

# Separate the list of larger factors of the number into prime and composite numbers 
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))
# Find the largest prime factor in the list
    prime_factors = []
    for potential_factor in factors:
        is_prime = True
        for j in range(2,int(math.sqrt(potential_factor))+1):
            if potential_factor % j == 0 and potential_factor != j: 
                is_prime = False
        if is_prime:
            prime_factors.append(potential_factor)

# Return the largest prime factor
    return max(prime_factors)

print(largest_prime_factor(331))