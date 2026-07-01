def findLongestIncreasingSubsequence(sequence): 
    n = len(sequence) 
  
    # LIS[i] stores the length of the longest increasing 
    # subsequence upto index i 
    # Initialize the sequence as 1
    LIS = [1 for i in range(n)] 
  
    # Compute LIS values for all indexes  
    for i in range (1 , n): 
        for j in range(0 , i): 
            if sequence[i] > sequence[j] and LIS[i]< LIS[j] + 1 : 
                LIS[i] = LIS[j]+1
  
    # Return  the maximum value 
    return max(LIS)