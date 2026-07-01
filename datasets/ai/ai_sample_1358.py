def mergeSortedLists(list1, list2):
 
 # Create variables
 result = []
 list1_index, list2_index = 0, 0
 
 # Iterate over both lists
 while list1_index < len(list1) and list2_index < len(list2):
   # Compare and add the lower value to the result
   if list1[list1_index] <= list2[list2_index]:
     result.append(list1[list1_index])
     list1_index += 1
   else:
     result.append(list2[list2_index])
     list2_index += 1
 
 # Add any remainder items from the two lists
 result.extend(list1[list1_index:])
 result.extend(list2[list2_index:])
 
 return result
 
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
 
print(mergeSortedLists(list1, list2))
# Output: [1, 2, 3, 4, 5, 6, 7, 8]