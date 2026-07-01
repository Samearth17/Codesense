def HammingDistance(str1,str2): 
    # find out the length of the longest string 
    l1 = len(str1) 
    l2 = len(str2) 
  
    # create a matrix of size l1 x l2 
    m = [[None]*(l2+1) for i in range(l1+1)] 
  
    # initialize the first row of the matrix 
    for i in range(l2+1): 
        m[0][i] = i 
  
    # initialize the first column 
    for i in range(l1+1): 
        m[i][0] = i 
  
    # traverse the matrix row by row 
    for i in range(1,l1+1): 
        for j in range(1, l2+1):
            if str1[i-1] == str2[j-1]: 
                m[i][j] = m[i-1][j-1] 
            else:
                m[i][j] = 1 + min(m[i][j-1], m[i-1][j], m[i-1][j-1]) 
  
    return m[l1][l2] 
  
# Driver code 
str1,str2 = "Random String1", "This is a random string"
print(HammingDistance(str1,str2))