def merge_sorted_lists(list1, list2):
    sorted_list = []
    i = 0
    j = 0

    # loop through both lists and compare values
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        else:
            sorted_list.append(list2[j])
            j += 1

    # add the remaining elements
    while i < len(list1):
        sorted_list.append(list1[i])
        i += 1
    while j < len(list2):
        sorted_list.append(list2[j])
        j += 1

    return sorted_list

list1 = [6, 8, 15, 33]
list2 = [4, 15, 20, 25]

sorted_list = merge_sorted_lists(list1, list2)
print(sorted_list) # [4, 6, 8, 15, 15, 20, 25, 33]