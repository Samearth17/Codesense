def find_number(lst, num):
  for i, v in enumerate(lst):
    if v == num:
      return i
  
  return -1

list_of_numbers = [2, 4, 9, 8, 10]
number_to_find = 8

# Find the given number in the list
index = find_number(list_of_numbers, number_to_find)
if index != -1:
  print(f'Number {number_to_find} found at index {index}.')
else:
  print('Number not found.')