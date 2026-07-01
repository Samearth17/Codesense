def knapsack(items, weights, max_weight):
    n = len(items)
    dp = [[0 for x in range(max_weight + 1)] for x in range(n + 1)] 
    
    for i in range(1, n + 1): 
        for w in range(max_weight + 1): 
            if weights[i - 1] <= w: 
                dp[i][w] = max(items[i - 1] +  
                               dp[i - 1][w - weights[i - 1]], 
                               dp[i - 1][w]) 
            else: 
                dp[i][w] = dp[i - 1][w] 
                      
    value = dp[n][max_weight] 
                
    return value

items = ["hammer", "pliers", "screwdriver"]
weights = [4, 5, 2]
max_weight = 6

value = knapsack(items, weights, max_weight)
print("The maximum value of items that can be fitted in the knapsack is:", value)