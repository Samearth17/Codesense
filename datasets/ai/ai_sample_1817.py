def find_primes(n):
    numbers = [True] * (n + 1)
    numbers[0] = False
    numbers[1] = False
    
    for i in range(2, n + 1):
        if numbers[i] == True:
            for j in range(2 * i, n + 1, i):
                numbers[j] = False
    
    primes = []
    for i in range(2, n + 1):
        if numbers[i] == True:
            primes.append(i)
    
    return primes

print(find_primes(100))