def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
 
def sum_primes(nums):
    prime_sum = 0
    for num in nums:
        if is_prime(num):
            prime_sum += num
    return prime_sum
 
nums = [2, 3, 9, 14]
 
result = sum_primes(nums)
print(result)