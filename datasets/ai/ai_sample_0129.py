def auto_complete(dictionary, prefix):
    # list for words with the given prefix
    prefix_words = []

    # iterate through the dictionary
    for word in dictionary:
        # if the word starts with given prefix, 
        # add it to the list
        if word.startswith(prefix):
            prefix_words.append(word)

    return prefix_words


dictionary = ["dog", "deer", "deal", "dungeon", "dark", "dusk"]
prefix = "d"

prefix_words = auto_complete(dictionary, prefix)
print(prefix_words)

# Output:
# ['dog', 'deer', 'deal', 'dungeon', 'dark', 'dusk']