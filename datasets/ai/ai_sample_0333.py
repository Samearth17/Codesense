import math
 
def is_prime(num):
    # Check if the number is 1 or less than 1
    if num <= 1:
        return False
    # Check if the number is divisible by any number between 2 and the square root of the number
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
 
def sum_primes(n):
    prime_sum = 0
    count = 0
 
    i = 2
    while count < n:
        if is_prime(i):
            prime_sum += i
            count += 1
        i += 1
 
    return prime_sum

sum_primes(n)