"""
Find all prime numbers in a given list of numbers
"""

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True

numbers = [13, 19, 23, 5, 7]
for num in numbers:
    if is_prime(num):
        print(num,"is a prime number")