def n_primes(n):
    count = 0
    number = 2

    while count < n:
        is_prime = True

        for i in range (2, number): 
            if number % i == 0:
                is_prime = False
        
        if is_prime: 
            print(number, end=" ")
            count += 1

        number += 1


n_primes(10)