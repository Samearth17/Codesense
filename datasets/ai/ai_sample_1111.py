def is_palindrome(number): 
num = number  
   
# initializing a reverse number  
reverse = 0
  
# Reverse the given number 
while(number > 0): 
   remainder = number % 10
   # Create reverse 
   reverse = (reverse * 10) + remainder 
   number = number // 10 
 
# check if original and reverse numbers are same
if (num == reverse): 
  return True
else: 
  return False