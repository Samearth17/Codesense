def find_longest_common_substring(text1,text2): 
  answer = "" 
  len1, len2 = len(text1), len(text2) 
  for i in range(len1): 
    match = "" 
    for j in range(len2): 
      if (i + j < len1 and 
          text1[i + j] == text2[j]): 
        match += text2[j] 
      else: 
        if (len(match) > len(answer)): 
          answer = match
        match = "" 
  return answer

text1 = 'abcdefghi'
text2 = 'acelgghi'

print(find_longest_common_substring(text1, text2))