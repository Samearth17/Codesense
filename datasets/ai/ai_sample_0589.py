# function to calculate edit distance
def edit_distance(s1, s2):
  if len(s1) == 0:
  return len(s2)
  if len(s2) == 0:
  return len(s1)
  if s1[-1] == s2[-1]:
  cost = 0
  else:
  cost = 1

  res = min([edit_distance(s1[:-1], s2)+1,
            edit_distance(s1, s2[:-1])+1,
            edit_distance(s1[:-1], s2[:-1]) + cost])
  return res

# example
s1 = 'cat'
s2 = 'cot'
print(edit_distance(s1, s2))  # output: 1