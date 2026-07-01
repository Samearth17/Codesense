def most_common_word(string):
    string_list = string.split()
    word_dict = {}
    for word in string_list:
        word_dict[word] = word_dict.get(word, 0) + 1
    max_count = 0
    most_common_word = None
    for word, count in word_dict.items():
        if count > max_count:
            max_count = count
            most_common_word = word
    return most_common_word

print(most_common_word(string))
# Output: the