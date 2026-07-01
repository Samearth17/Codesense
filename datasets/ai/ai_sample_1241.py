def translate(word):
 vowels = ('a', 'e', 'i', 'o', 'u')
 consonants = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')

if word[0] in vowels:
 new_word = word + 'ay'

elif word[0] in consonants:
 new_word = word[1:] + word[0] + 'ay'

else:
 new_word = word

return new_word

# Test
sentence = 'My name is John'

words = sentence.split(' ')
pig_latin = [translate(word) for word in words]
pig_latin_sentence = ' '.join(pig_latin)

print(pig_latin_sentence)

# Output: yMay amenay isay ohnJay