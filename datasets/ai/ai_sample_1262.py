def most_common(lst):
    lst_set = set(lst)
    max_val = -1
    max_item = None
    most_common_num = []
    for x in lst_set:
        item_count = lst.count(x)
        if max_val < item_count:
            max_val = item_count
            max_item = x
            if len(most_common_num) == 3:
                most_common_num.pop(0)
            most_common_num.append(x)
    return most_common_num
  
a = [1, 4, 2, 6, 7, 5, 1, 10, 4]
most_common_elements = most_common(a)
print("The most common 3 elements are:", most_common_elements)