def check_prime_pair_addition(num1, num2):
    """Given two numbers, check if they add up to a prime number."""
    
    if not is_prime(num1) or not is_prime(num2):
        return False
        
    primeSum = num1 + num2
    if is_prime(primeSum):
        return primeSum
    else:
        return False
    
def is_prime(num):
    """Check if a number is a prime number"""
    if num <= 1:
        return False
    else:
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1 
        return True

print(check_prime_pair_addition(23, 59))