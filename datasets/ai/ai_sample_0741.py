import re 

def find_vowel_words(string): 
    # split the string into words
    words = string.split() 
      
    # Define the regular expression to identify words starting with vowels
    regex = r"\b[aeiouAEIOU][a-zA-Z]*\b"
  
    # Initialize an empty list to store all the words
    vowel_words = [] 
  
    # Iterate over all the words 
    for word in words:
        
        # Check if the word starts with a vowel
        if re.match(regex, word): 
            
            # Append it to the vowel_words list
            vowel_words.append(word) 
  
    return vowel_words 

# Driver code  
string = "Apple, orange, banana" 
vowel_words = find_vowel_words(string)  
print(vowel_words)