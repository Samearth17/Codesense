"""
Write a python program that takes a string as input and check if it is palindrome or not
"""

def is_palindrome(string):
    # Reverse the string 
    rev_string = string[::-1]
    # Compare both strings 
    if string == rev_string:
        return True
    else:
        return False

if __name__ == '__main__':
    string = 'malayalam'
    print(is_palindrome(string))  # Output: True