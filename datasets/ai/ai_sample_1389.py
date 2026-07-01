def mergeSortedLists(list1, list2):
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3.append(list1[i])
            i += 1
        else:
            list3.append(list2[j])
            j += 1

    while i < len(list1):
        list3.append(list1[i])
        i += 1

    while j < len(list2):
        list3.append(list2[j])
        j += 1
    return list3

list3 = mergeSortedLists(list1, list2);
console.log(list3);