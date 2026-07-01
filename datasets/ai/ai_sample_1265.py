"""
Create a function which reverses the characters in a string
"""

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string) -1, -1, -1):
        reversed_string += string[i]
    return reversed_string

string = "Python"
reversed_string = reverse_string(string)

print("The original string is:", string)
print("The reversed string is:", reversed_string)