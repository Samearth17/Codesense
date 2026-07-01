def squareList(inputList): 
	# Returns a list of the squares of all the elements in inputList
	squaredList = [] 

	for num in inputList:
		squaredList.append(num ** 2) 

	return squaredList

# Example 
inputList = [1, 2, 3, 4, 5] 

squaredList = squareList(inputList) 

print(squaredList)

# Output: [1, 4, 9, 16, 25]