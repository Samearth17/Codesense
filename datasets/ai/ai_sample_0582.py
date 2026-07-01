def find_min_max(numbers):
 
 min_num = float('inf')
 max_num = float('-inf')
 
 for num in numbers:
  if num < min_num:
   min_num = num
  if num > max_num:
   max_num = num
 
 return [min_num, max_num]

numbers = [1, 10, 3, 8, 6]
print(find_min_max(numbers))

# Output: [1, 10]