def longest_common_subsequence(s1, s2):
  lengths = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
  for i, x in enumerate(s1):
    for j, y in enumerate(s2):
      if x == y:
        lengths[i+1][j+1] = lengths[i][j] + 1
      elif lengths[i+1][j] > lengths[i][j+1]:
        lengths[i+1][j+1] = lengths[i+1][j]
      else:
        lengths[i+1][j+1] = lengths[i][j+1]

  result = ""

  x, y = len(s1), len(s2)
  while x != 0 and y != 0:
      if lengths[x][y] == lengths[x-1][y]:
          x -= 1
      elif lengths[x][y] == lengths[x][y-1]:
          y -= 1
      else:
          assert s1[x-1] == s2[y-1]
          result = s1[x-1] + result
          x -= 1
          y -= 1

  return result