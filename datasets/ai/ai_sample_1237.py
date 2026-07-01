def is_anagram(s1, s2):
    # Remove whitespace and make strings lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # Check lengths. If lengths differ, strings cannot be anagrams
    if len(s1) != len(s2):
        return False
 
    # Check each letter. Strings are anagrams when there is a one-to-one mapping of characters.
    count = [0] * 26
    for i in range(len(s1)):
        index1 = ord(s1[i]) - ord('a')
        index2 = ord(s2[i]) - ord('a')

        count[index1] += 1
        count[index2] -= 1
 
    for i in range(26):
        if count[i] != 0:
            return False
 
    return True