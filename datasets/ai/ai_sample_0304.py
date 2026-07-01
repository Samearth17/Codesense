# Optimized Python code to find prime numbers in a range
# using primality tests

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if (num % i) == 0:
            return False

    return True


# Generate a range of consecutive numbers 
# and check for each if it is prime
def prime_numbers(n):
    for num in range(2, n+1):
        if is_prime(num):
            print(num, end=' ')


# Driver code
if __name__ == '__main__':
    n = 10
    prime_numbers(n)