def is_palindrome(s): 
    # Reverse the string 
    rev = s[::-1] 
  
    # Check if the string is equal to its reverse 
    if (s == rev): 
        return True
    return False
  
# Driver code 
s = "aba"
ans = is_palindrome(s) 
  
if ans == 1: 
    print("Yes") 
else: 
    print("No")