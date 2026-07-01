# Python program to check if a given string consists of only numeric digits 

# making a string with only digits 
# and assigning it to a variable 
test_string = "123456"
  
# printing original string  
print("Original String: " + test_string) 
  
# using if condition to 
# Check if all values are numbers 
if test_string.isdigit(): 
    print("String contains only numbers") 
else : 
    print("String not contains only numbers")