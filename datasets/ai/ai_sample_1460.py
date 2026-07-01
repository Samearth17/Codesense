def most_common_char(string):
    char_dict = {}
    for char in string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    most_common_char = ""
    most_common_freq = 0
    for char in char_dict:
        if char_dict[char] > most_common_freq:
            most_common_freq = char_dict[char]
            most_common_char = char
    return most_common_char