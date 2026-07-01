def levenshteinDistance(str1, str2): 
    m = len(str1) 
    n = len(str2) 
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
  
# base cases 
    for i in range(m + 1): 
        dp[i][0] = i 
    for j in range(n + 1): 
        dp[0][j] = j
  
    # fill the dp table 
    for i in range(1, m + 1): 
        for j in range(1, n + 1): 
            if str1[i - 1] == str2[j - 1]: 
                dp[i][j] = dp[i - 1][j - 1] 
            else: 
                dp[i][j] = 1 + min(dp[i][j - 1],        # Insert 
                                   dp[i - 1][j],        # Remove 
                                   dp[i - 1][j - 1])    # Replace 
  
    return dp[m][n]