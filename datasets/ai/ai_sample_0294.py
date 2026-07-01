def replace_vowels(s): 
    # Initialize an empty string 
    new_s = '' 
  
    # Iterate through each character
    for ch in s: 
        # Check if the character is a vowel 
        if (ch == 'a' or ch == 'e' or ch == 'i' 
            or ch == 'o' or ch == 'u'): 
            # Replace it with '$'
            new_s = new_s + '$' 
        else: 
            # Copy the same character 
            new_s = new_s + ch 

    return new_s 


str = 'Python'
result = replace_vowels(str)
print(result)