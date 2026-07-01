def is_anagram(str1, str2):
    if(len(str1) != len(str2)): 
        return False

    str1 = sorted(str1) 
    str2 = sorted(str2) 
  
    for i in range(0, len(str1)):
        if(str1[i] != str2[i]): 
            return False
    return True


str1 = "listen"
str2 = "silent" 

if(is_anagram(str1, str2)): 
    print("The strings are anagrams of each other")
else: 
    print("The strings are not anagrams of each other")