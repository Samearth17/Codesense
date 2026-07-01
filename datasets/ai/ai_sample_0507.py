def is_anagram(s1, s2):
    # Sort the strings 
    s1 = sorted(s1) 
    s2 = sorted(s2) 
  
    # If sorted strings are equal 
    return s1 == s2 
  
# Driver code 
s1 = "listen"
s2 = "silent"
if (is_anagram(s1, s2)): 
    print("The strings are anagrams.") 
else: 
    print("The strings aren't anagrams.")