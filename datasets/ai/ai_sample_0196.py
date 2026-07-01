def is_prime(num):
 for i in range(2, num // 2 + 1):
 if num % i == 0:
 return False
 return True

def prime_list(lst):
 prime_lst = []
 for num in lst:
 if is_prime(num):
 prime_lst.append(num)
 return prime_lst

lst = [2, 8, 3, 6, 10, 7, 14, 11, 17, 15]
prime_lst = prime_list(lst)
print(prime_lst) # Output: [2, 3, 7, 11, 17]