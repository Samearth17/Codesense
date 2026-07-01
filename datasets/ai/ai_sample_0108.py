def sieve_of_eratosthenes(start, end):
    prime = [True] * (end + 1)
    p = 2
    while p * p <= end:
        if prime[p]:
            for i in range(p * p, end + 1, p):
                prime[i] = False
        p += 1
    prime_numbers = []

    for p in range (start, end):
        if prime[p]:
            prime_numbers.append(p)

    return prime_numbers

print (sieve_of_eratosthenes(1, 20))