def sortByDivisible(numbers, integer):
 sortedList = []

 for num in numbers:
 if (num % integer == 0):
 sortedList.append(num)

 for num in numbers:
 if (num % integer != 0):
 sortedList.append(num)

 return sortedList

numbers = [10, 7, 3, 9, 12, 15]
integer = 3

print(sortByDivisible(numbers, integer))
# Output: [9, 12, 3, 10, 7, 15]