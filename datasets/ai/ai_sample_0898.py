def longest_substring(input_string1, input_string2): 
    
     # Create empty list to store all substrings 
    substr = [] 
      
    # we will find the length of strings 
    len1 = len(input_string1) 
    len2 = len(input_string2) 
      
    # Iterate through the string 
    for i in range(len1): 
        tmp = "" 
        for j in range(len2): 
            if (i + j < len1 and input_string1[i + j] == input_string2[j]): 
                tmp += input_string2[j] 
            else: 
                if (len(tmp) > len(substr)): 
                    substr = tmp  
                tmp = "" 
      
    # check for lastest substring  
    if len(tmp) > len(substr): 
        substr = tmp 
          
    # return longest substring  
    return substr