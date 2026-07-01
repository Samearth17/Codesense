import re

# Input string
string = "My age is 25 and my friend's age is 30."

# Find all the numbers in the string
numbers = re.findall("\d+", string)

# Calculate the sum
sum = 0
for number in numbers:
 sum += int(number)

# Print the sum
print("The sum of the numbers is:", sum)