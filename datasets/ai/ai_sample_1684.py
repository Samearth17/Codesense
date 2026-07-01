def mostCommonElement(list):
    element_count = {}
    for i in list:
        if i in element_count:
            element_count[i] += 1
        else:
            element_count[i] = 1 
    
    max_element = None
    max_num = 0
    for i in element_count:
        if element_count[i] > max_num:
            max_element = i
            max_num = element_count[i]
    
    return max_element