"""
Extract all the words starting with a specific letter
"""

def extract_words(word, letter):
    words_list = []
    for w in word.split():
        if w[0] == letter:
            words_list.append(w)
    return words_list

if __name__ == '__main__':
    words = 'This is a sample sentence to test the program'
    letter = 's'
    print(extract_words(words, letter))