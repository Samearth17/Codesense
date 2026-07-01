def knapsack(n, W, weights, values): 
    # create a 2D array, dp[n+1][W+1], and fill with zeros 
    dp = [[0 for x in range(W+1)] for x in range(n+1)] 

　　#iterating over array rows 
    for i in range(n+1): 
        #iterating over array columns 
        for w in range(W+1): 
            if i==0 or w==0 : 
                dp[i][w] = 0
            elif weights[i-1] <= w: 
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]],  dp[i-1][w]) 
            else: 
                dp[i][w] = dp[i-1][w] 
  
    return dp[n][W] 

# test
print(knapsack(5, 8, [2, 3, 4, 5, 6], [2, 5, 6, 12, 9]))
# Output: 20