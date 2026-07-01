def longestCommonSubstring(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
 
    ans = ""
    max_length = 0
 
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    ans = str1[i-max_length : i]
            else:
                dp[i][j] = 0
    return ans

print(longestCommonSubstring("Python", "Java"))