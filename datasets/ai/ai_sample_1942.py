def anagramCheck(word1, word2):
    # Removing whitespace characters
    w1 = word1.replace(" ", "")
    w2 = word2.replace(" ", "")
    
    # Check lengths
    if len(w1) != len(w2):
        return False
    
    # Convert to lowercase
    w1 = w1.lower()
    w2 = w2.lower()
    
    # Create dictionary to count frequency of each character
    count_dict1 = dict()
    count_dict2 = dict()
    for ch in w1:
        count_dict1[ch] = count_dict1.get(ch, 0) + 1
    for ch in w2:
        count_dict2[ch] = count_dict2.get(ch, 0) + 1
    
    # Check if character frequencies are equal
    if count_dict1 != count_dict2:
        return False        
    return True

word1 = 'rat'
word2 = 'art'
result = anagramCheck(word1, word2)
if result:
    print('The words are anagrams.')
else:
    print('The words are not anagrams.')