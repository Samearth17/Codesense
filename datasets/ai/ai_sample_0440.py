def print_common_elements(list1, list2):
    result = [] 
    i = 0
    j = 0
    while i < len(list1) and j < len(list2): 
        if list1[i] < list2[j]: 
            i += 1
        elif list2[j] < list1[i]: 
            j += 1
        else: 
            result.append(list1[i])
            i += 1
            j += 1
      
    for i in range(len(result)):
        print(result[i],end=" ")