"""
Calculate the maximum possible revenue from the items with given weights and values
"""

# given  weights and values 
weights = [2, 1, 3] 
values = [4, 2, 3] 

# number of items 
n = len(weights) 
  
# function to calculate the maximum revenue 
def knapsack(weights, values, n): 
  
    # total capacity of knapsack 
    W = 5
  
    # matrix to store solution matrix 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # build the solution matrix in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif weights[i-1] <= w: 
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
  
print (knapsack(weights, values, n))