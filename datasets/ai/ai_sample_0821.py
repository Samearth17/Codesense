def sumOfOdds(inputList):
 result = []
 for num in inputList: 
  if (num % 2 == 0): 
   for i in range(1, num): 
    if (i % 2 != 0): 
     if (num == i + (num - i)):
      result.append([i, num - i])
 
 return result
 
# Driver code
inputList = [4, 6, 10, 8]
 
print(sumOfOdds(inputList))