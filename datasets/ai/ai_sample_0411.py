s1 = set(["pineapple" ,"mango","apple","orange"])
s2 = set(["grandfather","grandmother","father","mother"])

longest_common_string = ""

for word1 in s1:
  for word2 in s2:
    if word1 not in longest_common_string and word2 not in longest_common_string:
      common_string = ""
      for i in range(min(len(word1),len(word2))):
        if word1[i] == word2[i]:
          common_string += word1[i]
    
      if len(common_string) > len(longest_common_string):
        longest_common_string = common_string

print(longest_common_string)