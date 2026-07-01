"""
Generate a sentence based on the input text
"""

import random

#get the user input
user_input = "The quick brown fox jumps over the lazy dog."

#split the string into a list of words
word_list = user_input.split()

#shuffle the list
random.shuffle(word_list)

#convert the list back to a string
generated_sentence = ' '.join(word_list)

#print the generated sentence
print(generated_sentence)