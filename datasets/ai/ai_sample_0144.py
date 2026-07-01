def num_unique_paths(m, n):
    dp = [[0 for x in range(m)] for y in range(n)] 
  
    # Count of paths to reach any
    # cell in first column is 1  
    for i in range(n): 
        dp[i][0] = 1
  
    # Count of paths to reach any
    # cell in first column is 1  
    for j in range(m): 
        dp[0][j] = 1
  
    # Calculate count of paths for other 
    # cells in bottom-up manner using
    # the recursive solution 
    for i in range(1, n): 
        for j in range(1, m): 
  
            # By uncommenting the last
            # part the code calculatest he total
            # possible paths if the diagonal 
            # Movements are allowed 
            dp[i][j] = dp[i-1][j] + dp[i][j-1]# + dp[i-1][j-1]
  
    return dp[n-1][m-1]