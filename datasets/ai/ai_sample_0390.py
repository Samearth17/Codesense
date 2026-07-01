def palindromic_substring(s):
  all_palindromes = []

  #  check for substrings of length 3
  for i in range(len(s) - 2):
    if s[i] == s[i + 2]:
      all_palindromes.append(s[i:i + 3])

  #  check for substrings of length 4
  for i in range(len(s) - 3):
    if s[i] == s[i + 3]:
      all_palindromes.append(s[i:i + 4])

  return all_palindromes

result = palindromic_substring("abc")
print(result)