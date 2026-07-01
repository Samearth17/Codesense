def prime_numbers(x, y):
 
 prime_nums = {}
 
 for i in range(x, y+1):
 if(i > 1):
 for j in range(2, i):
 if(i % j == 0):
 break
 else:
 prime_nums[i] = i
 
 return prime_nums
 
print(prime_numbers(8, 20))
# { 8: 8, 11: 11, 13: 13, 17: 17, 19: 19 }