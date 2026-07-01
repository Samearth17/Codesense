def max_frequency_char(string):
    char_freq = {}
    for char in string:
        if char in char_freq.keys():
            char_freq[char] += 1 
        else:
            char_freq[char] = 1
    max_freq = 0 
    max_char = None
    for char, freq in char_freq.items():
        if freq > max_freq:
            max_freq = freq
            max_char = char 
    return max_char

print(max_frequency_char(sample_str))