def longest_common_substring(s1, s2):
  len1, len2 = len(s1), len(s2)
  table = [[0 for _ in range(len2+1)] for _ in range(len1+1)] #2-D array
  longest, x_longest = 0, 0

  for x in range(1, len1+1):
    for y in range(1, len2+1):
      if s1[x-1] == s2[y-1]:
        table[x][y] = table[x-1][y-1] + 1
        if table[x][y] > longest:
          longest = table[x][y]
          x_longest = x
      else:
        table[x][y] = 0

  return s1[x_longest - longest: x_longest]