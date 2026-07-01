def isPrime(n):
    """
    This function checks if a given number is a prime or not
    """
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def printPrime():
    """
    This function prints all the prime numbers in between 0 and 100
    """
    for i in range(0, 101):
        if isPrime(i):
            print(i)

printPrime()