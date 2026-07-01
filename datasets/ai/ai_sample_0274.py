def merge_lists(list1, list2):
 merged_list = []

 # Iterate over both the lists 
 # and compare their elements 
 while len(list1) > 0 and len(list2) > 0:
  if list1[0] < list2[0]:
   merged_list.append(list1.pop(0))
  else:
   merged_list.append(list2.pop(0))

# Check to see if any elements remain in one of the lists
# and add them to the end of the merged list
 merged_list += list1
 merged_list += list2

 return merged_list

list1 = [1, 5, 9]
list2 = [2, 6, 8]

merged_list = merge_lists(list1, list2)
print(merged_list) # prints [1, 2, 5, 6, 8, 9]