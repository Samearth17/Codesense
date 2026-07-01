def is_anagram(s1, s2):
    # Remove whitespace and covert strings to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        # An anagram should have the same length
        return False

    # Create dictionaries containing characters of each string
    char_count1 = {}
    char_count2 = {}

    # Fill the dictionaries
    for char in s1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1

    for char in s2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1

    # If dictionaries are equal, then both string are anagrams
    return char_count1 == char_count2