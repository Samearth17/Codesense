import math 

def closestPair(arr, n): 
    min_dist = math.inf 
    for i in range(n):
        for j in range(i+1,n):
            dist = ((arr[i][0] - arr[j][0]) * 
                (arr[i][0] - arr[j][0]) + 
                  (arr[i][1] - arr[j][1]) * 
                  (arr[i][1] - arr[j][1])) 
            
            if (dist < min_dist):
                min_dist = dist
  
    return min_dist

arr = [(-2, -4), (0, 0), (-1, 1), (2,2), (3, 3), (-2,2), (4,4)] 
n = len(arr)
min_dist = closestPair(arr, n) 
print("The shortest distance is", min_dist)