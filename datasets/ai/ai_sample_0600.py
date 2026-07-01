def isAnagram(word1, word2): 
  
    # Get lengths of both strings 
    n1 = len(word1) 
    n2 = len(word2) 
  
    # If both strings have different lengths, they 
    # cannot be anagrams 
    if (n1 != n2): 
        return False
  
    # Sort both strings 
    word1 = sorted(word1) 
    word2 = sorted(word2) 
  
    # Compare sorted strings 
    for i in range(n1): 
        if word1[i] != word2[i]: 
            return False
  
    return True
  
# Driver program 
words = ("dear", "read")
  
if isAnagram(words[0], words[1]): 
    print("The word", words[0], "and", words[1], "are anagrams") 
else: 
    print("The word", words[0], "and", words[1], "are not anagrams")