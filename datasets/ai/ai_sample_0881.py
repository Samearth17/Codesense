def get_chars_with_exact_freq(string, freq):
    # create a character count hashtable
    count = {}

    # loop through the characters in the given string
    for char in string:
        # if the character is present in count
        if char in count:
            # increase the count of the character
            count[char] += 1
        else:
            # set the count of the character to 1
            count[char] = 1

    # initialize a list to store the characters that appear with given frequency
    chars_with_freq = []

    # loop through the characters in the count
    for key in count:
        # if the count of the character is equal to given frequency
        if count[key] == freq:
            # append the character to chars_with_freq
            chars_with_freq.append(key)
    # return the list of characters
    return chars_with_freq

result = get_chars_with_exact_freq("mississippi", 3)
print(result)