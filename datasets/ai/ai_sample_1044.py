def is_prime(n):
    """Check if a given number is prime."""
    # Corner case
    if n <= 1:
        return False

    # Check for divisibility
    for i in range(2, n):
        if n % i == 0:
            return False
    # Return true if it is not divisible by any number
    return True

# Output
print(is_prime(n))