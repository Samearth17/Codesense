def print_primes(start, end):
 for n in range(start, end + 1):
 if is_prime(n):
 print(n)
 
def is_prime(n):
 if n <= 1:
 return False
 elif n <= 3:
 return True
 elif (n % 2 == 0) or (n % 3 == 0):
 return False
 
 i = 5
 while i ** 2 <= n:
 if (n % i == 0) or (n % (i + 2) == 0):
 return False
 i += 6
 
 return True

print_primes(10, 25)