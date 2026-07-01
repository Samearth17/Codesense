"""
Find the longest contiguous increasing subsequence 
"""

def long_increasing_subsequence(arr): 
    n = len(arr) 
    dp = [1 for x in range(n)] 
   
    for i in range (1 , n): 
        for j in range(0 , i): 
            print (i,j) 
            if (arr[i] > arr[j]) and (dp[i]< dp[j] + 1): 
                dp[i] = dp[j]+1
   
    maximum = 0
    for i in range(n): 
        maximum = max(maximum, dp[i])  

    return maximum 

arr =[3,6,9,1,2,3,4,5] 
longest_subsequence_length = long_increasing_subsequence(arr)
print(longest_subsequence_length) # prints 5