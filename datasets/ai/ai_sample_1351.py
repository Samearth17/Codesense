#Function for palindrome check
def isPalindrome(string): 
    # Initializing left and right pointer 
    left = 0
    right = len(string) - 1
  
    # run till left and right pointer are same
    while left < right: 
        # if both characters at left and right pointers are same
        if string[left] == string[right]:
            left += 1
            right -= 1
  
        # if the characters are not equal, return False 
        else: 
            return False
  
    # if the loop has ended without break, the string is a palindrome 
    return True

#Inputting a string
string = 'abccb'

#Check the string for palindrome
if (isPalindrome(string)): 
    print("Input string is palindrome")
else: 
    print("Input string is not a palindrome")