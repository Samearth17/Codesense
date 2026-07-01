def anagram_grouping(words):
   anagrams = dict()
   #loop through the list and sort each word
   for word in words: 
      sorted_word = ''.join(sorted(word))
      # check if sorted word exists as a key in dictionary
      if sorted_word not in anagrams: 
         anagrams[sorted_word] = [word] #add key and word to dict
      else: 
         anagrams[sorted_word].append(word) #add word to existing anagrams

   #create a list of anagrams
   result = []
   for values in anagrams.values():
      result.append(values)

   return result


words = ["tea", "eat", "ate", "apple", "plea", "rat", "tar"]
ans = anagram_grouping(words)
print(ans)