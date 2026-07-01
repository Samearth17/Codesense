from collections import defaultdict

# Create dictionary to hold all anagrams
anagrams = defaultdict(list)

# Loop through each word
for word in ["mister", "buster", "tired", "tries", "mines"]:
    # Sort all characters
    sorted_word = ''.join(sorted(word))
    # Add word to anagrams list
    anagrams[sorted_word].append(word)

# Print all anagrams
for anagram in anagrams.values():
    print(*anagram, sep=' ')