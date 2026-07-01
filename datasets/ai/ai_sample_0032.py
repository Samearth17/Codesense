def sieve_eratosthenes(n): 
    prime_list = [True] * (n+1) 
    prime_list[0] = False
    prime_list[1] = False
    primes = [] 
      
    for i in range(2, n+1): 
        if prime_list[i] == True: 
            primes.append(i) 
            for j in range(i*i, n+1, i): 
                prime_list[j] = False
    return primes 
  
n = 100
print("The Prime numbers from 1 to 100 are:")
print(sieve_eratosthenes(n))