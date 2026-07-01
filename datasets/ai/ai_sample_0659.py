def intersection(list1, list2):
 result = []
 i = 0
 j = 0
 while i < len(list1) and j < len(list2):
 if list1[i] == list2[j]:
 result.append(list1[i])
 i += 1
 j += 1
 elif list1[i] < list2[j]:
 i += 1
 else:
 j += 1
 return result

print(intersection(list1, list2))
# Output: [7, 11]