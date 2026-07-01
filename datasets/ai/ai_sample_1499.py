def knapsack(weights, values, maxWeight):
 if len(weights) == 0 or len(values) == 0 or len(weights) != len(values):
 return 0
 
 if maxWeight == 0:
 return 0
 
 if len(weights) == 1:
 if weights[0] <= maxWeight:
 return values[0]
 else:
 return 0
 
 if weights[0] > maxWeight:
 return knapsack(weights[1:], values[1:], maxWeight)
 
 return max(values[0] + knapsack(weights[1:], values[1:], maxWeight - weights[0]),
 knapsack(weights[1:], values[1:], maxWeight))

# Test
weights = [2, 3, 5, 1, 6]
values = [3, 8, 7, 2, 8]
maxWeight = 6

knapsack(weights, values, maxWeight) # Output: 15