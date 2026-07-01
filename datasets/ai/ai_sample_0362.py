def print_list(list_1, list_2): 
    formatted_list = [list_1 + list_2 for i in range(len(list_1))] 
    for x in formatted_list: 
        for y in x: 
            print(y) 
    
list_1 = [1, 2, 3] 
list_2 = [4, 5, 6]
print_list(list_1, list_2)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6