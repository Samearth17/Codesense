def compare_strings(s1, s2):
 m = len(s1)
 n = len(s2)
 
 # Create a table to store results of subproblems
 dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
 
 # Fill d[][] in bottom up manner
 for i in range(m + 1):
  for j in range(n + 1):
   if i == 0 or j == 0:
    dp[i][j] = 0
   elif s1[i - 1] == s2[j - 1]:
    dp[i][j] = 1 + dp[i - 1][j - 1]
   else:
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
 
 # LCS will be last entry in the lookup table
 return dp[m][n]