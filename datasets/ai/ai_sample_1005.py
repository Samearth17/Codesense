def find_prime_numbers(num):
 prime_numbers = []
 for x in range(2, num):
 flag = True
 for y in prime_numbers:
 if x % y == 0:
 flag = False
 break
 if flag:
 prime_numbers.append(x)
 if len(prime_numbers) == 10
 break

return prime_numbers
 
# Usage
find_prime_numbers(100)
# Output
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]