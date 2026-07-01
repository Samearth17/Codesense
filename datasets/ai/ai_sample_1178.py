def palindrome_checker(string1, string2): 
    m = len(string1) 
    n = len(string2) 
  
    if m != n: 
        return False    
  
    string1 = string1.lower() 
    string2 = string2.lower() 
      
    # create empty 2-D matrix 
    C = [[0] * (n + 1) for i in range(m + 1)] 
  
    # palindromic substring of length 0 
    for i in range(m + 1): 
        C[i][0] = 0
  
    # palindromic substring of length 1 
    for j in range(n + 1): 
        C[0][j] = 0
  
    # fill the matrix in bottom-up manner 
    for i in range(1, m + 1): 
        for j in range(1, n + 1): 
            if string1[i - 1] == string2[j - 1]: 
                C[i][j] = C[i - 1][j - 1] + 1
    return m == n == C[m][n]