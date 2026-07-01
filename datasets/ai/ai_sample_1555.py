def binary_search(numbers, number_to_find, low, high):
 
 if low > high:
 return False
 
 mid = (low + high) // 2
 
 if numbers[mid] == number_to_find:
 return True
 elif numbers[mid] > number_to_find:
 return binary_search(numbers, number_to_find, low, mid - 1)
 else:
 return binary_search(numbers, number_to_find, mid + 1, high)
 
 
if __name__ == '__main__':
 numbers = [1, 3, 8, 10, 12, 15, 17, 20, 22, 34, 38, 40]
 
 number_to_find = int(input('Enter a number: '))
 
 result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)
 
 if result is True:
 print('The number is in the list')
 else:
 print('The number is NOT in the list')