list1 = [2, 3, 4] 
list2 = [3, 5, 6, 4]

# create a set of elements in list1
s1 = set(list1)

# create a set of elements in list2
s2 = set(list2)

# find the intersection 
intersection = s1.intersection(s2)

# print the intersection 
print(intersection) 
# prints {3, 4}