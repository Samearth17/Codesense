def count_unique_chars(char_array):
    char_set = set() 
    for char in char_array: 
        char_set.add(char) 
    
    counting_dict = {} 
    for char in char_set: 
        counting_dict[char] = 0
        for character in char_array: 
            if char == character: 
                counting_dict[char] += 1
    
    return counting_dict

char_array = ["a", "b", "c", "a", "d", "e", "c"]

counting_dict = count_unique_chars(char_array)
print(counting_dict)
# {'c': 2, 'e': 1, 'a': 2, 'b': 1, 'd': 1}