from multiprocessing import Pool
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_numbers(n):
    primes = []
    with Pool(processes=4) as pool:
        primes = list(pool.map(is_prime, range(2, n)))
    return primes