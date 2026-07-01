def all_substrings(string):
# Create empty list to store all substrings 
substrings = []

# Find all possible substrings using two nested loops 
for i in range(len(string)):
 for j in range(i, len(string)):
  substring = string[i : j + 1]
  substrings.append(substring)

# Sort the list and return
substrings.sort()
return substrings

# Test
print(all_substrings('hello'))
# Output: ['h', 'he', 'hel', 'hell', 'hello', 'e', 'el', 'ell', 'ello', 'l', 'll', 'llo', 'l', 'lo', 'o']