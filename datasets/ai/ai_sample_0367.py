def calculate_std_deviation(numbers):
 mean = sum(numbers) / len(numbers)
 
 variance = 0
 for num in numbers:
 variance += (num - mean)**2
 variance = variance/len(numbers)
 
 std_deviation = variance**0.5
 return std_deviation
 
 
numbers = [2, 4, 4, 4, 5, 5, 7, 9]
std_deviation = calculate_std_deviation(numbers)
print('The standard deviation is: {}'.format(std_deviation))