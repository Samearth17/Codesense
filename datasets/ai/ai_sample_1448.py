"""
Create a method in Python that takes a text string and determines whether the string is a palindrome.
"""

def is_palindrome(text):
    i = 0
    j = len(text) - 1
    while i <= j:
        if text[i] != text[j]:
            return False
        i += 1
        j -= 1
    return True

if __name__ == '__main__':
    text = "racecar"
    print(is_palindrome(text))