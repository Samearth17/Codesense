def lcs(str1, str2):
    n = len(str1) 
    m = len(str2) 
  
    # Create a matrix to store 
    # results of subproblems 
    LCSuff = [[0 for k in range(m+1)] for l in range(n+1)] 
  
    # Fill the LCSuff matrix in 
    # bottom up manner 
    for i in range(n+1): 
        for j in range(m+1): 
            if (i == 0 or j == 0): 
                LCSuff[i][j] = 0
            elif (str1[i-1] == str2[j-1]): 
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
            else: 
                LCSuff[i][j] = max(LCSuff[i-1][j], LCSuff[i][j-1]) 
  
    # finding the common substring 
    index = LCSuff[n][m] 
  
    # Create a character array 
    # to store the lcs string 
    lcs = [""] * (index+1) 
    lcs[index] = "" 
  
    # Start from the right-most-bottom-most 
    # corner and one by one store characters 
    # in lcs[] 
    i = n 
    j = m 
    while (i > 0 and j > 0): 
  
        # If current character in str1 and 
        # str2 are same, then current
        # character is part of LCS 
        if (str1[i-1] == str2[j-1]): 
            lcs[index-1] = str1[i-1] 
            i -= 1
            j -= 1
            index -= 1
  
        # If not same, then find the larger 
        # of two and go in the direction 
        # of larger value 
        elif (LCSuff[i-1][j] > LCSuff[i][j-1]): 
            i -= 1
        else: 
            j -= 1
  
    return "".join(lcs) 
  
str1 = "abcdabcd"
str2 = "bcdee"

print(lcs(str1, str2)) #"bcd"