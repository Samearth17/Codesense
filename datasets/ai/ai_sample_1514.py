def sieve_of_eratosthenes(n): 
    sieve = [True] * (n + 1) 
    sieve[0] = False
    sieve[1] = False
    for i in range(2, n + 1):  
        if (sieve[i] == True): 
            for j in range(2 * i, n + 1, i): 
                sieve[j] = False
    return sieve

numbers = [7, 9, 13, 27]
sieve = sieve_of_eratosthenes(50)
for num in numbers: 
    if sieve[num]: 
        print(num,"is prime number")
    else: 
        print(num,"is not a prime number")