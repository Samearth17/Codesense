def find_pattern(string, pattern): 
    n = len(string) 
    m = len(pattern) 
  
    # A loop to slide pat[]  
    # one by one 
    for i in range(n - m + 1): 
        j = 0
  
        # For current index i, 
        # check for pattern match 
        while(j < m): 
            if (string[i + j] != pattern[j]): 
                break
            j += 1
  
        if (j == m): 
            return i 
    return -1