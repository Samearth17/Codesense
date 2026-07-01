def nth_prime_number(n):
    prime_numbers = [2]
    number = 3

    while len(prime_numbers) < n:
        is_prime = True
        for prime in prime_numbers:
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(number)
        number += 2
    return prime_numbers[-1]

print(nth_prime_number(5))