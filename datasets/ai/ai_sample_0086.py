def primeSieve(n): 
    prime_list = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime_list[p] == True): 
            for i in range(p * 2, n+1, p): 
                prime_list[i] = False
        p += 1
    primes=[] 
    for p in range(2, n): 
        if prime_list[p]: 
            primes.append(p) 
    return primes

print(primeSieve(10))  # [2, 3, 5, 7]