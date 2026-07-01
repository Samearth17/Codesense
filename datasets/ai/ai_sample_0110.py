def editDistance(string1, string2, m, n):
    # Create an empty matrix
    dp = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Filling the first column of the matrix
    for i in range(m+1): 
        dp[i][0] = i 
  
    # Filling the second column of the matrix 
    for j in range(n+1): 
        dp[0][j] = j 
  
    # Populate the matrix
    for i in range(1, m+1): 
        for j in range(1, n+1): 
  
            if string1[i-1] == string2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],        # Insert
                                   dp[i-1][j],        # Remove 
                                   dp[i-1][j-1])      # Replace
  
    return dp[m][n] 
  
  
# Driver program 
string1 = "kitten"
string2 = "sitting"
m = len(string1) 
n = len(string2) 
print(editDistance(string1, string2, m, n))