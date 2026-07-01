def longestCommonSubstring(string1, string2):
    n1=len(string1)
    n2=len(string2)
    
    L=[[0 for _ in range(n2+1)]for _ in range(n1+1)]
    longestSubstring=""
    longestSubstringLength=0
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if string1[i-1]==string2[j-1]:
                L[i][j]=L[i-1][j-1]+1
                if L[i][j]>longestSubstringLength:
                    longestSubstringLength=L[i][j]
                    longestSubstring=string1[i-1-longestSubstringLength+1:i]
            else:
                L[i][j]=0
    return longestSubstring