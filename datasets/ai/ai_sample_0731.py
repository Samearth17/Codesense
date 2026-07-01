def are_anagrams(s1, s2): 
      
    # get lengths of both strings 
    n1 = len(s1) 
    n2 = len(s2) 
      
    # if lengths not equal, strings are not anagrams 
    if n1 != n2: 
        return False
  
    # sort both strings  
    s1 = sorted(s1) 
    s2 = sorted(s2) 
  
    # linearly compare characters of both strings 
    for i in range(0, n1): 
        if s1[i] != s2[i]: 
            return False
  
    return True 
  
s1 = "listen"
s2 = "silent"
if are_anagrams(s1,s2):
    print("The strings are anagrams of each other.")
else: 
    print("The strings are not anagrams of each other.")