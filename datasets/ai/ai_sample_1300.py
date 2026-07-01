import math

def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

prime_nums = []

for i in range(2, 1000):  
    if is_prime(i):
        prime_nums.append(i)
        if len(prime_nums) == 10:
            break

for item in prime_nums:
    print(item)