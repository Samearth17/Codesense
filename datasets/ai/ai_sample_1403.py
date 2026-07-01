def longest_common_subsequence(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    dp_table = [[0]*(n2+1) for _ in range(n1+1)]
    for i in range(n1):
        for j in range(n2):
            if s1[i] == s2[j]: 
                dp_table[i+1][j+1] = dp_table[i][j] + 1
            else:
                dp_table[i+1][j+1] = max(dp_table[i][j+1], 
                                        dp_table[i+1][j])
    lcs_length = dp_table[-1][-1]
    lcs_string = "" 
    i, j = n1, n2
    while i > 0 and j > 0: 
        if dp_table[i][j] == dp_table[i-1][j]: 
            i -= 1
        elif dp_table[i][j] == dp_table[i][j-1]: 
            j -= 1
        else: 
            lcs_string = s1[i-1] + lcs_string 
            i -= 1
            j -= 1
    
    return lcs_string, lcs_length