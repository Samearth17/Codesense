def num_vowels(words):
    vowels = ["a", "e", "i", "o", "u"]
    word_dict = {}
    
    for word in words:
        word_vowels = 0
        
        for letter in word:
            if letter.lower() in vowels:
                word_vowels += 1
                
        word_dict[word] = word_vowels
    
    return word_dict

words_list = input("Enter a list of words: ").split()
print(num_vowels(words_list))