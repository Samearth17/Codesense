def findLongestSubstring(inputString):
 longest = 0
 longestSubstring = ''
 
 for i in range(len(inputString)):
 current = inputString[i]
 count = 1
 currentSubstring = current
 
 for j in range(i + 1, len(inputString)):
 if current == inputString[j]:
 count += 1
 currentSubstring += inputString[j]
 else:
 break
 
 if count > longest:
 longest = count
 longestSubstring = currentSubstring
 
 return longestSubstring

longestSubstring = findLongestSubstring('abcdabca')
print(longestSubstring) # Output: 'abca'