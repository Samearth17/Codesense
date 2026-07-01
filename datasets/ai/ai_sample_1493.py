# Python program to generate 
# n random numbers within a given range 
import random 
  
# Function to generate random numbers 
def random_numbers(rangeStart, rangeEnd, numberOfNumbers): 
    res = [] 
    for j in range(numberOfNumbers): 
        res.append(random.randint(rangeStart, rangeEnd)) 
  
    return res 
  
# Driver Code 
rangeStart = -10
rangeEnd = 10
numberOfNumbers = 20

print(random_numbers(rangeStart, rangeEnd, numberOfNumbers))