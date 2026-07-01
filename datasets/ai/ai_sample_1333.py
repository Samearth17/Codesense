def sum_of_primes(n):
    '''This function returns the sum of prime numbers below n.'''
    if n < 2:
        return 0
    primes = [True] * n
    primes[0] = False
    primes[1] = False
    for i in range(2,int(n**0.5)+1):
        if primes[i]:
            for j in range(i**2, n, i):
                primes[j] = False
    return sum(i for i in range(2, n) if primes[i])

if __name__ == '__main__':
    n = 10
    print(sum_of_primes(n))