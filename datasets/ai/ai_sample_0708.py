def findCommonElements(listA, listB):
 commonElements = []

 for elementA in listA:
 for elementB in listB:
 if elementA == elementB:
 commonElements.append(elementA)

 return commonElements

listA = [1, 3, 5, 7, 9]
listB = [2, 3, 4, 5, 8]
commonElements = findCommonElements(listA, listB) 

print(commonElements)  # Output: [3, 5]