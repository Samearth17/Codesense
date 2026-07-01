def check(row, col):
  for (i, j) in zip(row[:col], range(col)):
    if abs(i - row[col]) == abs(j - col) or i == row[col]:
      return False
  return True

def nQueens(n, row=None):
  if row is None:
    row = [0] * n
  if len(row) == n and check(row, n - 1):
    return [list(x) for x in set(tuple(x) for x in solutions)]
  else:
    for i in range(n):
      row[len(row)] = i
      if check(row, len(row) - 1):
        solutions.append(row[:])
        x = nQueens(n, row[:])
        if x != None:
          return x

solutions = []
nQueens(8)
print(solutions[0])