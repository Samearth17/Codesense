def merge_sorted_lists(list1, list2):
    new_list = []

    i1 = 0
    i2 = 0
    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] < list2[i2]:
            new_list.append(list1[i1])
            i1 += 1
        else:
            new_list.append(list2[i2])
            i2 += 1
    
    while i1 < len(list1):
        new_list.append(list1[i1])
        i1 += 1
    
    while i2 < len(list2):
        new_list.append(list2[i2])
        i2 += 1

    return new_list

list1 = [2, 3, 5, 8]
list2 = [4, 6, 7]

merged = merge_sorted_lists(list1, list2)
print(merged)