def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    edit_table = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0: 
                edit_table[i][j] = j
            elif j == 0: 
                edit_table[i][j] = i
            elif str1[i-1] == str2[j-1]: 
                edit_table[i][j] = edit_table[i-1][j-1] 
            else: 
                edit_table[i][j] = 1 + min(edit_table[i][j-1], edit_table[i-1][j], edit_table[i-1][j-1]) 
  
    return edit_table[m][n]