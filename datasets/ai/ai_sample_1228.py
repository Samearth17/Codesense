def is_anagram(s1, s2):
 s1 = s1.replace(" ", "")
 s2 = s2.replace(" ", "")
 if len(s1) != len(s2):
 return False
 s1_count = Counter(s1)
 s2_count = Counter(s2)
 for i in s1_count:
 if s1_count[i] != s2_count[i]:
 return False
 return True

s1 = "listen"
s2 = "silent"
print(is_anagram(s1, s2))
# Output: True.