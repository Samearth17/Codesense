def sort_list(mylist):
 for i in range(len(mylist)):
 
 min_index = i
 temp = mylist[i]
 
 for j in range(i + 1, len(mylist)):
 
  if mylist[min_index] > mylist[j]:
   min_index = j
 
 mylist[i] = mylist[min_index]
 mylist[min_index] = temp
 
 return mylist
 
mylist = [1, 5, 7, 8, 4, 10, 2]
 
print("Sorted list is:")
print(sort_list(mylist))