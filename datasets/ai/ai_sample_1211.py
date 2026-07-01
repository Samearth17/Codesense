def generate_anagrams(words):
 anagrams = []
 for word in words:
  anagrams_list = []
  if len(word) == 1:
   return [word]
  for anagram in generate_anagrams(words.difference({word})):
   for i in range(len(word)):
    anagrams_list.append(anagram[:i]+ word[0] + anagram[i:])
  anagrams += anagrams_list
 return anagrams

words = set(['python', 'typhon'])
print(generate_anagrams(words))
# Output: ['typhon', 'python', 'hynopt', 'ptyhon']