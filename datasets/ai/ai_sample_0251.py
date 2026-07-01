"""Generate a python script that takes a list of random numbers as input and return only the even numbers from the list"""

# Take a list as input
lst = [1,6, 3,2 ,8,7, 0, 4, 9, 11, 22, 18, 33, 28, 26, 55, 49, 37, 63, 59]

# Create a new list that will contain only the even numbers from the input list
even_numbers = []

# Iterate through input list and append only even numbers to the new list 
for num in lst:
    if num % 2 == 0:
        even_numbers.append(num)
        
# Print out the new list containing only even numbers
print(even_numbers)