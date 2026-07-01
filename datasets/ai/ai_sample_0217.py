def is_prime(list_of_numbers):
    # Iterate over the list of numbers
    for num in list_of_numbers:
        # Check if the number is divisible by any number
        # other than 1 and the number itself
        for divisor in range(2, num):
            if num % divisor == 0:
                # If there is any divisor, the
                # number is not a prime number
                return False
    # All the numbers in the list are prime numbers
    return True

list_of_numbers = [2, 3, 5, 7, 8, 11, 13, 15]
outcome = is_prime(list_of_numbers)
print(outcome)