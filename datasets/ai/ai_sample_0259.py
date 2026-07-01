import math
 
def primes(n):
    if n < 2:
        return []
    
    size = int(math.sqrt(n)) + 1
    sieve = bytearray([True]) * size
    for i in range(2, size):
        if sieve[i]:
            for j in range(i*i, size, i):
                sieve[j] = False
  
    primes = [i for i in range(2, size) if sieve[i]]
    return [p for p in primes if p <= n]
 
if __name__ == '__main__':
    n = 15
    print(primes(n))

# Output: [2, 3, 5, 7, 11, 13]