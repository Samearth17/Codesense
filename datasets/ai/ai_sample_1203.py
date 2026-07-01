def levenshteinDistance(str1, str2): 
    n = len(str1)
    m = len(str2)
    dp = [[0 for x in range(m + 1)] for x in range(n + 1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(n + 1): 
        for j in range(m + 1): 
  
            # If first string is empty 
            if i == 0: 
                dp[i][j] = j
  
            # If second string is empty 
            elif j == 0: 
                dp[i][j] = i
  
            # If last characters are same 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last characters are not same 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1], # try adding to the right
                                   dp[i-1][j],  # try deleting 
                                   dp[i-1][j-1]) # try changing
  
    return dp[n][m]