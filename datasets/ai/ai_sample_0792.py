def findLongestSubstring(string):
 
 # Initialize the result
 max_length = 0
 
 # Initialize substrings
 curr = ''
 
 for char in string:
  if char not in curr:
   curr += char
   max_length = max(max_length, len(curr))
  else:
   curr = char
 
 return max_length

string = 'abcaac'
print(findLongestSubstring(string))