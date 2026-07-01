def prime_factors(num):
 prime_list = []
 i = 2
 while i * i <= num:
 if num % i:
 i += 1
 else:
 num //= i
 prime_list.append(i)
 if num > 1:
 prime_list.append(num)
 return prime_list

n = int(input('Enter a positive integer: '))
print(prime_factors(n))