def isAnagram(str1, str2):
    # Convert the strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Sort the strings
    str1sorted = ''.join(sorted(str1))
    str2sorted = ''.join(sorted(str2))

    # Check if sorted strings are equal 
    if(str1sorted == str2sorted):
        return True
    else:
        return False

# Test
print(isAnagram('Hello', 'World'))