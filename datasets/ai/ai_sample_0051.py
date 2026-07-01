def most_common_fruit(fruit_list):
 
    # Dictionary to get count of each fruit
    freq_dict = {}
 
    # Count frequency of each fruit
    for fruit in fruit_list:
        if fruit in freq_dict:
            freq_dict[fruit] += 1
        else:
            freq_dict[fruit] = 1
 
    # Get maximum frequency 
    max_freq = 0
    for freq in freq_dict.values():
        if freq > max_freq:
            max_freq = freq
 
    # Get the most common fruit
    most_common_fruit = None
    for fruit, freq in freq_dict.items():
        if freq == max_freq:
            most_common_fruit = fruit
            break
 
    return most_common_fruit