def average(array):
 '''
 Finds the average of all numbers in an array

 Args:
 array (list): List of numbers

 Returns:
 float: The average of all values in the array
 '''

 total = 0
 for value in array:
 total += value

 return total / len(array)