def longest_palindromic_substring(s): 
	n = len(s) 
	L = [[0 for x in range(n)] 
			for y in range(n)] 
	# All substrings of length 1 are palindromes 
	for i in range(n): 
		L[i][i] = 1

	# check all substring of length 2
	for cl in range(2, n + 1): 
		for i in range(n - cl + 1): 
			j = i + cl - 1
			if s[i] == s[j] and cl == 2: 
				L[i][j] = 2
			elif s[i] == s[j]: 
				L[i][j] = L[i + 1][j - 1] + 2
			else: 
				L[i][j] = max(L[i][j - 1],L[i + 1][j]); 

	# start position of the longest palindromic substring 
	start = 0
	length = 1
	for i in range(n): 
		if (length < L[i][n - 1]): 
			length = L[i][n - 1] 
			start = i 
	return s[start - length + 1:start + length] 

print(longest_palindromic_substring("abracadabra"))