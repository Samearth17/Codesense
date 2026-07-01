def is_prime(num):
    """Check if the given number is prime.

    Args:
        num (int): A number to check

    Returns:
        bool: True if num is prime, False otherwise.
    """

    if num < 2: 
        return False

    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

num = 20
result = is_prime(num)
print(f"Is {num} prime? {result}")