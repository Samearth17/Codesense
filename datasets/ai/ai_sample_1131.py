def lcs(string1, string2):
 n = len(string1)
 m = len(string2)

 dp = [[0 for x in range(m + 1)] for x in range(n + 1)] 

# fill dp table in bottom up manner 
for i in range(n + 1): 
 for j in range(m + 1): 
   if i == 0 or j == 0: 
    dp[i][j] = 0
   elif string1[i-1] == string2[j-1]: 
    dp[i][j] = dp[i-1][j-1] + 1
   else: 
    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 

 index = dp[n][m] 

# Create an array of size of lcs 
longest_common_subsequence = [""] * (index + 1) 
longest_common_subsequence[index] = "" 

# Start from the right-most-bottom-most corner and 
# one by one store characters in lcs[] 
i = n 
j = m 
while i > 0 and j > 0: 

	# If current character in X[] and Y are same, then 
	# current character is part of LCS 
	if string1[i-1] == string2[j-1]: 
		longest_common_subsequence[index - 1] = string1[i-1] 
		i-=1
		j-=1
		index-=1

	# If not same, then find the larger of two and 
	# go in the direction of larger value 
	elif dp[i-1][j] > dp[i][j-1]: 
		i-=1
	else: 
		j-=1

return "".join(longest_common_subsequence)