"""
A Python function to determine whether two given strings are anagrams of each other
"""
def check_anagram(string1, string2): 
    # If the strings are not of equal length, they cannot be anagrams
    if len(string1) != len(string2): 
        return False

    # Dictionary to store characters and their frequencies
    dictionary = {} 

    # Store the frequency of the characters of the first string to the dictionary
    for char in string1:  
        if char in dictionary: 
            dictionary[char] += 1
        else: 
            dictionary[char] = 1

    # Iterate over the characters in the second string 
    for char in string2:  
        # If the character is not in the dictionary, then the string cannot an anagram
        if char in dictionary:  
            dictionary[char] -= 1
        else: 
            return False

    # Check if all the frequencies have been reduced to 0
    for i in dictionary.values(): 
        if i != 0: 
            return False

    return True
    
if __name__ == '__main__':
    string1 = "Stop"
    string2 = "post"
    print(check_anagram(string1, string2))