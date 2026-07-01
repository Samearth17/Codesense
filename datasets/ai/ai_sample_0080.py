def compress(s): 
    # Initialize results 
    output = "" 
  
    # Initialize count 
    count = 1
  
    # Traverse the string 
    for i in range(len(s)): 
          
        # If the current character is same 
        # as next one, increment its count 
        if (i+1 < len(s) and s[i] == s[i+1]): 
            count += 1
          
        else: 
            # Append the count and character 
            outputo + = str(count) + s[i] 
          
            # Reset the  count  
            count = 1
          
    # Append the last obtained characters 
    # and their count 
    output += str(count) + s[i] 
  
    return output

s = "aabbbbbbcccc"
print(compress(s))
# Output: 2a6b4c