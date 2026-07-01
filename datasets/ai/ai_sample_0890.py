# Defining the function
def count_positive_negative_zero(arr):
 # Keeping track of the counts
 positive_count = 0
 negative_count = 0
 zero_count = 0

 # Iterating over the array of integers
 for number in arr:
 if number > 0:
 positive_count += 1
 elif number == 0:
 zero_count += 1
 elif number < 0:
 negative_count += 1

 # Printing the results
 print('Number of positive elements:', positive_count)
 print('Number of zero elements:', zero_count)
 print('Number of negative elements:', negative_count)

# Testing the function
arr = [1, 0, -2, 3, 4, -6]
count_positive_negative_zero(arr)

# Output
# Number of positive elements: 3
# Number of zero elements: 1
# Number of negative elements: 2