def find_anagrams(words):
    # create an empty list to store the anagrams
    anagrams = []

    # create a dictionary where the keys represent the sorted word and 
    # the values represent the original word
    anagram_map = {}

    # loop through the given list of words
    for word in words: 
        # sort the word alphabetically
        sorted_word = ''.join(sorted(word))

        if sorted_word in anagram_map:
            # if the sorted word is already present 
            # in the dictionary, add it to the anagrams list
            anagrams.append([word, anagram_map[sorted_word]])
        else:
            # if the sorted word is not present
            # in the dictionary, add it to the dictionary
            anagram_map[sorted_word] = word
            
    return anagrams

words = ["dog", "god", "cat", "act"]
print(find_anagrams(words)) # prints [["dog", "god"], ["cat", "act"]]