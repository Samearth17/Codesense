def longest_common_substring(str1, str2): 
    # a 2D array to store the comparison 
    comparison = [[0 for i in range(len(str2)+1)] for j in range(len(str1)+1)] 
    
    result = "" # To store the result 
    print(comparison)
    # iterate through the 2D array comparing each character 
    for i in range(1, len(str1) + 1): 
        for j in range(1, len(str2) + 1): 
            # check if the characters match 
            if str1[i-1] == str2[j-1]: 
                comparison[i][j] = comparison[i - 1][j - 1] + 1
                # update the result if a longer common substring is found 
                if comparison[i][j] > len(result): 
                    result = str1[i - comparison[i][j]:i] 
            else: 
                comparison[i][j] = 0
  
    return result 

common_str = longest_common_substring(str1, str2)  
print("The longest common substring is: " + common_str)