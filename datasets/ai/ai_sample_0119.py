def merge_sorted_lists(listA, listB): 
    merged_list = []
    ptrA = 0
    ptrB = 0
    while ptrA < len(listA) and ptrB < len(listB): 
        if listA[ptrA] <= listB[ptrB]: 
            merged_list.append(listA[ptrA]) 
            ptrA += 1
        else: 
            merged_list.append(listB[ptrB]) 
            ptrB += 1
    while ptrA < len(listA): 
        merged_list.append(listA[ptrA]) 
        ptrA += 1
    while ptrB < len(listB):
        merged_list.append(listB[ptrB])
        ptrB += 1
    return merged_list