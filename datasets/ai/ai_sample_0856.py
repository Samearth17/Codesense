def prime_factorization(n):
    # list to store prime factors
    prime_factors = [] 
  
    # remove any factors of 2 first
    while n % 2 == 0: 
        prime_factors.append(2) 
        n = n / 2
  
    # n must be odd at this point 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            prime_factors.append(int(i)) 
            n = n / i 
      
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        prime_factors.append(int(n)) 
    
    return prime_factors