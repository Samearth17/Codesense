def isAnagram(s1, s2): 
 
    # Remove white spaces and convert strings to lowercase 
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    
    # Return boolean for sorted match. 
    return sorted(s1) == sorted(s2) 
  
# Driver code 
s1 = "apple"
s2 = "lepap"
if isAnagram(s1, s2):
    print("True, The strings are anagram of each other")
else:
    print("False, The strings are not anagram of each other")