list1 = [1, 4, 5, 6]
list2 = [2, 3, 7, 8]

def merge_lists(list1, list2):
    # sorted list to store the result
    sorted_list = []

    # counts to iterate over each list
    i = 0 
    j = 0

    # loop through both lists until one list ends
    while i < len(list1) and j < len(list2):
        # if first list has a smaller element, add it to the result
        if list1[i] < list2[j]:
            sorted_list.append(list1[i])
            i += 1
        # if second list has a smaller element, add it to the result
        else:
            sorted_list.append(list2[j])
            j += 1

    # if there are elements remaining in any of the lists, append them
    sorted_list.extend(list1[i:])
    sorted_list.extend(list2[j:])

    return sorted_list

list1 = [1, 4, 5, 6]
list2 = [2, 3, 7, 8]

result = merge_lists(list1, list2)
print(result)