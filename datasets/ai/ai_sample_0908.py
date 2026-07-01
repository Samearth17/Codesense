def find_most_frequent(lst):
    max_count = 0
    most_frequent = None
    count_dict = {}
    for elem in lst:
        if elem not in count_dict:
            count_dict[elem] = 1
        else:
            count_dict[elem] += 1
            
        if count_dict[elem] > max_count:
            most_frequent = elem
            max_count = count_dict[elem]
            
    return most_frequent, max_count