#Function to find the LCS of two strings
def find_lcs(x, y): 
    # Find lengths of the two strings 
    m = len(x) 
    n = len(y) 
    
    #To store the lengths of longest common subsequences
    lcs = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    #Fill the table in bottom up manner 
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                lcs[i][j] = 0
            elif x[i-1] == y[j-1]: 
                lcs[i][j] = lcs[i-1][j-1] + 1
            else: 
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1]) 
  
    #To store one of the possible common subsequence
    index = lcs[m][n] 
    lcs_str = [""] * (index+1) 
    lcs_str[index] = ""
  
    #Following loop code is used to find one of the longest common subsequence
    i = m 
    j = n 
    while i > 0 and j > 0: 
  
        #If current character in X and Y are same,then
        # reduce both the count and add the character to the result string
        if x[i-1] == y[j-1]: 
            lcs_str[index-1] = x[i-1] 
            i-=1
            j-=1
            index-=1
  
        # If not same, move to the left, top or corner (diagonal) cell 
        #Whichever has the max value
        elif lcs[i-1][j] > lcs[i][j-1]: 
            i-=1
        else: 
            j-=1
  
    # Return the longest common subsequence
    return "".join(lcs_str)

# Main function
x = "abcdaf"
y = "acbcf"
res = find_lcs(x,y)
print("The Longest Common Subsequence is:")
print(res)

# Output: The Longest Common Subsequence is: 
# abcf