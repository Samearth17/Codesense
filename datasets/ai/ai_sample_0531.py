def countCharacters(string): 
    # Create dictionary to return  
    # count of each character 
    str_dict = {} 
  
    # Count frequency of each 
    # character of the string 
    for i in string: 
        if i in str_dict: 
            str_dict[i] += 1
        else: 
            str_dict[i] = 1
  
    return str_dict 

# Driver code 
string = "String Counting"

# Print result 
print(countCharacters(string))