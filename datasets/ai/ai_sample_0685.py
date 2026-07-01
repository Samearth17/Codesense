def linearSearch(sampleList, x):
 for i in range(len(sampleList)):
 if sampleList[i] == x:
 return i 

return -1

# Driver code
x = 5
result = linearSearch(sampleList, x)

if result == -1:
 print("Element not found")
else:
 print("Element found at index", result)