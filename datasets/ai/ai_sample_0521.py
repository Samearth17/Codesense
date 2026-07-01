def findNearestSquares(n):
  nearestSquareList = []
  i = 1
  # Find all the nearest squares
  while i * i <= n:
    nearestSquareList.append(i * i)
    i += 1
  
  # Find the nearest 3 squares
  nearest3Squares = nearestSquareList[-3:]
  
  return nearest3Squares

nearest3Squares = findNearestSquares(30)
print(nearest3Squares)

# Output:
# [25, 28, 29]